from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, Email, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=25)])
    
class CreateUserForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=25)])

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                        validators=[DataRequired(), EqualTo("password")])