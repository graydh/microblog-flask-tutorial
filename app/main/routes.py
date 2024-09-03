from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_babel import _, get_locale
from flask_login import current_user, login_required

from datetime import datetime, timezone
from langdetect import detect, LangDetectException
import sqlalchemy as sa

from app import db

from app.main.forms import EditProfileForm, EmptyForm, PostForm, SearchForm, MessageForm, RegistrationFrom
from app.models import User, Post, Message, Notification
from app.translate import translate
from app.main import bp
from app.main.email import send_user_invite_email


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        try:
            language = detect(form.post.data)
        except LangDetectException:
            language = ''
        post = Post(body=form.post.data, author=current_user, language=language)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = db.paginate(
        current_user.following_posts(), page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url, prev_url = None, None
    if posts.has_next: next_url = url_for('main.index', page=posts.next_num)
    if posts.has_prev: prev_url = url_for('main.index', page=posts.prev_num)
    delete_form = EmptyForm()
    return render_template('index.html', title=_('Home page'),
                           posts=posts, form=form, delete_form=delete_form, prev_url=prev_url, next_url=next_url)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    page = request.args.get('page', 1, type=int)
    query = user.posts.select().order_by(Post.timestamp.desc())
    posts = db.paginate(query, page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url, prev_url = None, None
    if posts.has_next: next_url = url_for('main.user', username=user.username, page=posts.next_num)
    if posts.has_prev: prev_url = url_for('main.user', username=user.username, page=posts.prev_num)
    form = EmptyForm()
    delete_form = EmptyForm()
    return render_template('user.html', user=user,
                           posts=posts, form=form, delete_form=delete_form, prev_url=prev_url, next_url=next_url)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'), form=form)


@bp.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username)
        )
        if user is None:
            flash(_(f'User %(username)s not found.', username=username))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash(_('You cannot follow yourself'))
            return redirect(url_for('main.user', username=username))
        current_user.follow(user)
        db.session.commit()
        flash(_(f'Following %(username)s', username=username))
        return redirect(url_for('main.user', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
    form = EmptyForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == username)
        )
        if user is None:
            flash(_(f'User %(username)s not found.', username=username))
            return redirect(url_for('main.index'))
        if user == current_user:
            flash(_('You cannot unfollow yourself'))
            return redirect(url_for('main.user', username=username))
        current_user.unfollow(user)
        db.session.commit()
        flash(_(f'Not following %(username)s', username=username))
        return redirect(url_for('main.user', username=username))
    else:
        return redirect(url_for('main.index'))


@bp.route('/remove_post/<post_id>', methods=['POST'])
@login_required
def remove_post(post_id):
    form = EmptyForm()
    if form.validate_on_submit():
        post = db.session.query(Post).filter(Post.id == post_id).first()
        if current_user.email not in current_app.config['ADMINS']:
            # check a user should be deleting own post
            if post.author != current_user:
                flash("You can only delete your own posts!")
                return redirect(url_for('main.index'))
        else:
            # an admin is deleting
            msg = Message(author=current_user, recipient=post.author,
                          body="Your post: '" + post.body + "' was removed for violating the content policy")
            db.session.add(msg)
            post.author.add_notification('unread_message_count', post.author.unread_message_count())
        db.session.query(Post).filter(Post.id == post_id).delete()  # picky syntax for delete
        flash('The post no longer exists: ' + post.body)
        db.session.commit()
    return redirect(url_for('main.index'))


@bp.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    query = sa.select(Post).order_by(Post.timestamp.desc())
    posts = db.paginate(
        query, page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url, prev_url = None, None
    if posts.has_next: next_url = url_for('main.explore', page=posts.next_num)
    if posts.has_prev: prev_url = url_for('main.explore', page=posts.prev_num)
    delete_form = EmptyForm()
    return render_template("index.html", title=_('Explore'),
                           posts=posts, delete_form=delete_form, next_url=next_url, prev_url=prev_url)


@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    data = request.get_json()
    return {'text': translate(data['text'],
                              data['source_language'],
                              data['dest_language'])}


@bp.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    delete_form = EmptyForm()
    return render_template('search.html', title=_('Search'), posts=posts,
                           delete_form=delete_form, next_url=next_url, prev_url=prev_url)


@bp.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    form = EmptyForm()
    return render_template('user_popup.html', user=user, form=form)


@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = db.first_or_404(sa.select(User).where(User.username == recipient))
    form = MessageForm()
    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)
        user.add_notification('unread_message_count',
                              user.unread_message_count())
        db.session.commit()
        flash(_('Your message has been sent.'))
        return redirect(url_for('main.user', username=recipient))
    return render_template('send_message.html', title=_('Send Message'),
                           form=form, recipient=recipient)


@bp.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.now(timezone.utc)
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    query = current_user.messages_received.select().order_by(
        Message.timestamp.desc())
    messages = db.paginate(query, page=page,
                           per_page=current_app.config['POSTS_PER_PAGE'],
                           error_out=False)
    next_url = url_for('main.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('main.messages', page=messages.prev_num) \
        if messages.has_prev else None
    delete_form = EmptyForm()
    return render_template('messages.html', messages=messages.items, delete_form=delete_form,
                           next_url=next_url, prev_url=prev_url)


@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    query = current_user.notifications.select().where(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    notifications = db.session.scalars(query)
    return [{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications]


@bp.route('/export_posts')
@login_required
def export_posts():
    if current_user.get_task_in_progress('export_posts'):
        flash(_('An export task is currently in progress'))
    else:
        current_user.launch_task('export_posts', _('Exporting posts...'))
        db.session.commit()
    return redirect(url_for('main.user', username=current_user.username))


@bp.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        flash(_('Congratulations they are now a registered user!'))
        # select user for invite email
        user = db.session.scalar(sa.select(User).where(User.email == form.email.data))
        if user:
            send_user_invite_email(user)
        return redirect(url_for('main.register'))
    return render_template('register.html', title=_('Invite'), form=form)

