#
# Package constructor for application
# Script with factory function for application
# Instantiate DB and Mail objects and then define factory function
#

from flask import Flask, render_template, url_for, flash, redirect, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()   #create SQLAlchemy database object without paramaters to allow for flexible configuration when app is generated -- vs SQLAlchemy(app)
mail = Mail()       #create (flask) Mail object without paramaters to allow for flexible configuration when app is generated -- vs Mail(app)

def create_app(config_name):                    #application factory function. Instantiate Flask app with target config options, 
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)           #further customization of configs via static method in configs file. Optional.

    mail.init_app(app)                          #further customization of mail configs via static method in configs file. Optional.
    db.init_app(app)                            #further customization of db configs via static method in configs file. Optional.

    from .main import main as main_blueprint    #import main blueprint from "Main" package constructor 
    app.register_blueprint(main_blueprint)      #register main blueprint for application (which itself brings views, errors, and has templates)

    return app                                  #return the initialized application