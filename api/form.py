from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired, Length


class LoginForm(FlaskForm):
    email = StringField(
        'email',
        validators=[InputRequired(), Email(), Length(7, 64)]
    )
    username = StringField('password', validators=[InputRequired(), Length(8, 80)])
    password = PasswordField('password', validators=[InputRequired(), Length(8, 80)])


class LoginForm(FlaskForm):
    email = StringField(
        'email',
        validators=[InputRequired(), Email(), Length(7, 64)]
    )
    username = StringField('password', validators=[InputRequired(), Length(8, 80)])
    password = PasswordField('password', validators=[InputRequired(), Length(8, 80)])


