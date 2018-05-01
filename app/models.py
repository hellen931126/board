from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__="users"
    id = db.Column(db.Integer)
    uuid = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(36), unique=True, index=True)
    created_at = db.Column(db.DateTime(),default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(),default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.Text, default="user/default.png", nullable=True)
    comments = db.relationship('Comment', backref='user')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
   
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)
    
    def update_profile(self):
        self.updated_at = datetime.utcnow()
        db.session.add(self)


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer)
    uuid = db.Column(db.String(36), primary_key=True)    
    content = db.Column(db.Text)
    user_uuid = db.Column(db.String(36), db.ForeignKey('users.uuid'))   
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    