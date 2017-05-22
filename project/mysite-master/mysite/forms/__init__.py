from flask.ext.wtf import Form
from wtforms import (BooleanField, DateField, FloatField, StringField, IntegerField,
                     DateTimeField, PasswordField, SelectField, TextAreaField, SelectMultipleField)
from wtforms import widgets
from wtforms.validators import DataRequired, InputRequired


class LoginForm(Form):
    core_id = StringField("CoreID:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    remember_me = BooleanField()
