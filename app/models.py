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

    def to_dict(self):
        data = {
            "timestamp": self.timestamp,
            "temp": self.temp,
            "humidity": self.humidity,
            "particles": self.particles,
            "eco2": self.eco2,
            "tvoc": self.tvoc,
        }

        return data

    def from_dict(self, data):
        for field in ["temp", "humidity", "particles", "eco2", "tvoc"]:
            if field in data:
                setattr(self, field, data[field])
