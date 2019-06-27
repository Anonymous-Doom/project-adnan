#
# Script to define DB models for application
#

from . import db
from datetime import datetime


class User(db.Model):                                                               #User Model
    __tablename__ = 'users'                                                         #Table Name
    id = db.Column(db.Integer, primary_key=True)                                    #Primary Key
    username = db.Column(db.String(20), unique=True, nullable=False)                
    email = db.Column(db.String(70), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')    #Image for user profile
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)                      #Relationship (User to Posts)

    def __repr__(self):
        return 'User: {u}, {e}, {i}'.format(u=self.username,e=self.email,i=self.image_file)

class Post(db.Model):                                                               #Post Model
    __tablename__ = 'posts'                                                         #Table Name
    id = db.Column(db.Integer, primary_key=True)                                    #Primary Key
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)                                     #Post Content
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)       #Foriegn Key (Post to User)

    def __repr__(self):
        return 'Post: {t} - {d}'.format(t=self.title,d=self.date_posted)