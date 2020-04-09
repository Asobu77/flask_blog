from flask_blog import db
from datetime import datetime

class User(db.Model):
    __tabname__ = 'users'
    id           = db.Column(db.Integer, primary_key = True)
    user_name    = db.Column(db.String(30))
    mail_address = db.Column(db.String(50), unique = True)
    password     = db.Column(db.String(30))
    created_at   = db.Column(db.DateTime)

    def __init__(self, user_name = None, mail_address = None, password = None):
        self.user_name    = user_name
        self.mail_address = mail_address
        self.password     = password
        self.created_at   = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} user_name:{} mail_address:{} password:{}>'.format(self.id, self.user_name, self.mail_address, self.password)
