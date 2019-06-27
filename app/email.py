#
#Script to define application email server
#

from flask_mail import Message
from flask import render_template
from . import mail, app


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)         #Renders template for text based email
    msg.html = render_template(template + '.html', **kwargs)        #Renders template for HTML based email
    mail.send(msg)