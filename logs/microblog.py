2024-04-02 12:15:14,279 ERROR: Unhandled exception [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py:56]
Traceback (most recent call last):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 427, in send
    connection.send(self)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 188, in send
    self.host.sendmail(sanitize_address(envelope_from or message.sender),
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 872, in sendmail
    self.ehlo_or_helo_if_needed()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 611, in ehlo_or_helo_if_needed
    if not (200 <= self.ehlo()[0] <= 299):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 451, in ehlo
    self.putcmd(self.ehlo_msg, name or self.local_hostname)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py", line 46, in export_posts
    send_email(
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/email.py", line 21, in send_email
    mail.send(msg)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 152, in __exit__
    self.host.quit()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 1004, in quit
    res = self.docmd("quit")
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 431, in docmd
    self.putcmd(cmd, args)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first
2024-04-02 12:22:40,807 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:22:45,876 ERROR: Unhandled exception [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py:56]
Traceback (most recent call last):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 427, in send
    connection.send(self)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 188, in send
    self.host.sendmail(sanitize_address(envelope_from or message.sender),
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 872, in sendmail
    self.ehlo_or_helo_if_needed()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 611, in ehlo_or_helo_if_needed
    if not (200 <= self.ehlo()[0] <= 299):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 451, in ehlo
    self.putcmd(self.ehlo_msg, name or self.local_hostname)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py", line 46, in export_posts
    send_email(
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/email.py", line 21, in send_email
    mail.send(msg)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 152, in __exit__
    self.host.quit()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 1004, in quit
    res = self.docmd("quit")
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 431, in docmd
    self.putcmd(cmd, args)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first
2024-04-02 12:23:35,571 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:23:57,782 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:25:37,204 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:25:42,378 ERROR: Unhandled exception [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py:56]
Traceback (most recent call last):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 427, in send
    connection.send(self)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 188, in send
    self.host.sendmail(sanitize_address(envelope_from or message.sender),
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 872, in sendmail
    self.ehlo_or_helo_if_needed()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 611, in ehlo_or_helo_if_needed
    if not (200 <= self.ehlo()[0] <= 299):
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 451, in ehlo
    self.putcmd(self.ehlo_msg, name or self.local_hostname)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/tasks.py", line 46, in export_posts
    send_email(
  File "/Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/email.py", line 21, in send_email
    mail.send(msg)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 492, in send
    message.send(connection)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/site-packages/flask_mail.py", line 152, in __exit__
    self.host.quit()
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 1004, in quit
    res = self.docmd("quit")
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 431, in docmd
    self.putcmd(cmd, args)
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 378, in putcmd
    self.send(f'{s}{CRLF}')
  File "/Users/dgraymullen/miniconda3/envs/microblog-flask-tutorial/lib/python3.9/smtplib.py", line 365, in send
    raise SMTPServerDisconnected('please run connect() first')
smtplib.SMTPServerDisconnected: please run connect() first
2024-04-02 12:30:39,180 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:44:13,034 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/app/__init__.py:97]
2024-04-02 12:45:40,339 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/app/__init__.py:97]
2024-04-02 12:46:07,742 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:46:36,317 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:47:53,087 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
2024-04-02 12:50:40,947 INFO: Microblog startup [in /Users/dgraymullen/Documents/GitHub/microblog-flask-tutorial/./app/__init__.py:97]
