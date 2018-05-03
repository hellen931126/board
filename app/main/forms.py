from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import User
from wtforms import ValidationError
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(),Length(1,36)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("Log in")

class RegisterationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(1,64)])
    password = PasswordField("Password", validators=[DataRequired(),EqualTo("password2","Passwords must match")])
    password2 = PasswordField("Comfirm password", validators=[DataRequired(),EqualTo("password","Passwords must match")])
    submit = SubmitField("Sign up")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError("Username already in use")

class CommentForm(FlaskForm):
    content = TextAreaField("What's on your mind?", validators=[DataRequired()],render_kw = {"placeholder":"Write down your message here"})
    submit = SubmitField("Submit")
  