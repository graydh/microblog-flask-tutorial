from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


def send_user_invite_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Micro-Blog] New User Invite'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/invite_user.txt',
                                         user=user, token=token),
               html_body=render_template('email/invite_user.html',
                                         user=user, token=token))
