from extensions import db


class URL(db.Model):
    __tablename__ = 'url'

    id = db.Column(db.Integer(), primary_key=True)
    domain = db.Column(db.String(), nullable=False)
    path = db.Column(db.String())
    hash = db.Column(db.String(), unique=True, nullable=False)
    original_url = db.Column(db.String(), nullable=False)
