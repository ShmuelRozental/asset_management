from sqlalchemy import Integer, Column, String, DateTime

from asset_management.db import db


class Nachsal(db.Model):
    __tablename__ = 'nachsal'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    details = Column(String(255), nullable=True)
    date = Column(DateTime, nullable=False)


    user_nachsal = db.relationship('UserNachsal', back_populates='nachsal', lazy=True)


