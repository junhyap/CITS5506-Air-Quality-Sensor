from app import db
from datetime import datetime


class AirQuality(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.String(64),
        index=True,
        default=str(datetime.now()).replace(" ", "-"),
        nullable=False,
        primary_key=True,
    )
    temp = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    particles = db.Column(db.Integer)
    eco2 = db.Column(db.Integer)
    tvoc = db.Column(db.Integer)

    def __repr__(self):
        return "<Air Quality {}>".format(self.string)
