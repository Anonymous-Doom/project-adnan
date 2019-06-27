from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Each Class attribute in the form class is rendered as a form field when instantiated
#param is form field label
class RegistrationForm(FlaskForm):                                              #Regisration Form inherits from FlaskForm
    username = StringField('Username',                                          #string for username
                        validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',                                                #string for email + validatoin of format
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                        validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')                                            

class LoginForm(FlaskForm):                                                     #Login form inherits from FlaskForm
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')                                      #Remember me checkbox
    submit = SubmitField('Login')