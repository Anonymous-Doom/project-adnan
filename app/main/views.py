from datetime import datetime
from flask import render_template, session, redirect, url_for,flash     #Flask modules for for view functions
from . import main                                                      #Import main blueprint from package constructor
from .forms import LoginForm, RegistrationForm                          #Import form classes for use in views
from .. import db                                                       #Import database models 
from ..models import User

#
# App Routes below [Home, About, Register, Login]
# ^^ Using main blueprint
#

@main.route('/')
@main.route('/home')
def home():                                             #route for site homepage
    return render_template('home.html',posts=None)

@main.route('/about')                                   
def about():                                                            #route for site about page
    return render_template('about.html',title='About')

@main.route('/register', methods=['GET','POST'])                        #form requires GET and POST requests
def register():                                                         #route for user registration page
    form = RegistrationForm()
    if form.validate_on_submit():                                       #Action to take on form submit + validate.
        email = User.query.filter_by(email=form.email.data).first()     #Post-Validation: Confirm if email is in DB already.
        if email is None:                                               #Add new user
            db.session.add(User(username=form.username.data, email=form.email.data, password=form.password.data))
            db.session.commit()
            # send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', recipients=[db.session.query(User).filter_by(email=form.email.data).first()])
        else:                                                           #Else: request new email or to login instead.
            flash(f'{form.username.data} is not available! Try a different name or log into your account!')
        session['username'] = form.username.data                        #Store user info in session object
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('.home'))                               #Redirect to homepage on success
    return render_template('register.html',title='Register',form=form)  #Outside of submit/validate . Render template first.

@main.route('/login', methods=['GET','POST'])                           #Login Form requires GET and POST methods
def login():                                                            #route for login page
    form = LoginForm()
    if form.validate_on_submit():                                       #Process login attempts on form submit
        if db.session.query(User).filter(User.email == form.email.data, User.password == form.password.data):
            flash(f"You're IN!! Hey :)!", 'success')                    #Query db (preceeding line) Needs major fixing.
            return redirect(url_for('.home'))                           #Currently redirect to home... maybe members area instead?
        else:
            flash('Login Failed', 'danger')
    return render_template('login.html',title='Login',form=form)