from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", backref="store", lazy="dynamic", cascade="all, delete")

    tags = db.relationship("TagModel", backref="store", lazy="dynamic", cascade="all, delete")