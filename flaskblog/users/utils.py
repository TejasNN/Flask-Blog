import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)

    output_size = (125, 125)
    resize_image = Image.open(form_picture)
    resize_image.thumbnail(output_size)
    resize_image.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request',
                       sender='noreply@demo.com', 
                       recipients=[user.email])
    message.body = f'''To reset your password, click on the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made
'''
    mail.send(message)