from wtforms import (TextField, TextAreaField, SubmitField, validators,
                     PasswordField, StringField, BooleanField, SelectField)
from .models import User
from flask_wtf import Form
# from .models import Project


class UploadScenarios(Form):
    projects = SelectField('Project Name', [validators.DataRequired()],
                           coerce=int)

class ContactForm(Form):
    name = TextField("Name", [validators.Required("Please enter your name.")])
    email = TextField("Email",
                      [validators.Required("Please enter your email address."),
                       validators.Email("Please enter your email address.")])
    subject = TextField(
        "Subject", [validators.Required("Please enter a subject.")])
    message = TextAreaField(
        "Message", [validators.Required("Please enter a message.")])
    submit = SubmitField("Send")


class RegistrationForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])
    # confirm = PasswordField('Repeat Password')
    projects = SelectField('Project Name', [validators.DataRequired()],
                           coerce=int)
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            print("Form Validation failed")
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False

        return True


class SigninForm(Form):
    email = TextField("Email",
                      [validators.Required("Please enter your email address."),
                       validators.Email("Please enter your email address.")])
    password = PasswordField(
        'Password', [validators.Required("Please enter the password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False
