from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from asset_management.db import db

# User model definition
class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(255), nullable=True)
    role = Column(String(20), nullable=False)  # 'soldier' or 'commander'
    group_id = Column(Integer, ForeignKey('groups.id'), nullable=True)  # optional, only for soldiers

    # Relationships
    group = relationship("Group", back_populates="users")
    responses = relationship("UserNachsal", back_populates="user")
