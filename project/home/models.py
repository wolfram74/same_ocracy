from project import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Figure(db.Model):

    __tablename__ = 'figures'

    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, handle, name):
        self.handle = handle
        self.name = name

    def __repr__(self):
        return '<figure %s>' % self.handle

# class Impersonation(db.Model):

#     __tablename__ = 'impersonations'
#     id = db.Column(db.Integer, primary_key=True)
#     guesses = dbColumn(db.Integer, default=0)
#     corrects = dbColumn(db.Integer, default=0)
#     figure_id = db.Column(db.Integer, ForeignKey('figures.id'))
# class Confusion(db.Model):

#     __tablename__ = 'confusions'
#     id = db.Column(db.Integer, primary_key=True)
#     guesses = dbColumn(db.Integer, default=0)
#     corrects = dbColumn(db.Integer, default=0)
#     source_figure_id =  db.Column(db.Integer, ForeignKey('figures.id'))
#     other_figure_id =  db.Column(db.Integer, ForeignKey('figures.id'))
