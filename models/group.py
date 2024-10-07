from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from asset_management.db import db

class Group(db.Model):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    users = relationship('User', back_populates='group', lazy=True)
