from flask_blog import db
from datetime import datetime

class Weight(db.Model):
    __tabname__ = 'weights'
    id       = db.Column(db.Integer,  primary_key = True)
    user_id  = db.Column(db.Integer,  nullable = False)
    date     = db.Column(db.DateTime, nullable = False)
    weight   = db.Column(db.Float,    nullable = False)

    def __init__(self, user_id = None, date = None, weight = None):
        self.user_id = user_id
        self.date    = date
        self.weight  = weight

    def __repr__(self):
        return '<Entry user_id:{} date:{} weight:{}>'.format(self.user_id, self.date, self.weight)
