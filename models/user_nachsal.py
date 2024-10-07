from asset_management.db import db


class UserNachsal(db.Model):
    __tablename__ = 'user_nachsal'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    nachsal_id = db.Column(db.Integer, db.ForeignKey('nachsal.id'), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    user = db.relationship("User", back_populates="responses")
    nachsal = db.relationship('Nachsal', back_populates='user_nachsal')


