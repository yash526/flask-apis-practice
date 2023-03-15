from db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)

    stores = db.relationship("StoreModel", backref="tag")
    items = db.relationship("ItemModel", backref="tag", secondary="items_tags")