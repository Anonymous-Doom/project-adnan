#
# Configurations Module
# Script to load various application configurations depending on chosen context
#

import os                                                                               #OS will grab environ variables
basedir = os.path.abspath(os.path.dirname(__file__))                                    #var to shorten pathways for db configs

class Config:                                                                           #Set environment variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6fdb3a25e8d9c6a4b3cf9c61bcfa3974'     #set on server
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.googlemail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true',1,'on']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')                                     #set on server
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')                                     #set on server
    PROJECT__MAIL_SUBJECT_PREFIX = '[ProjectAdnan]'
    PROJECT_MAIL_SENDER = 'ProjectAdnan Admin <adnanhasic.ah@gmail.com>'
    PROJECT_ADMIN = os.environ.get('PROJECT_ADMIN')                                     #set on server
    SQLALCHEMY_TRACK_MODIFICATIONS = False                                              #false will speed up db queries

    @staticmethod                                                                       #perform custom actions that apply to the configuration at initialization time
    def init_app(app):
        pass

class DevelopmentConfig(Config):                                                        #development server configs
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):                                                               #test server configs
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///'

class ProductionConfig(Config):                                                         #prod server configs
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {                                                                              #dictionary holding the above configuration options
    'development':DevelopmentConfig,
    'testing':TestConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}