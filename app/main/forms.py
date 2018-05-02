from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from ..models import User
from wtforms import ValidationError
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(1,36)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("Log in")


  