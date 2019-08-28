from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),])
    password = PasswordField('Password', validators=[DataRequired(),])
    remember_me = BooleanField('Remember me' )
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')


    def validate_username(self, username):
        user = User.query.filter_by(name=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists. Please try another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists. Please try another one')