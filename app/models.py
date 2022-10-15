from datetime import datetime
import time
from flask import url_for
from app import db


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": resources.pages,
                "total_items": resources.total,
            },
            "_links": {
                "self": url_for(endpoint, page=page, per_page=per_page, **kwargs),
                "next": url_for(endpoint, page=page + 1, per_page=per_page, **kwargs)
                if resources.has_next
                else None,
                "prev": url_for(endpoint, page=page - 1, per_page=per_page, **kwargs)
                if resources.has_prev
                else None,
            },
        }
        return data


class AirQuality(PaginatedAPIMixin, db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(
        db.String(64),
        index=True,
        default=str(datetime.now()).replace(" ", "-"),
        nullable=False,
        primary_key=True,
    )
    js_timestamp = db.Column(
        db.Integer,
        default=time.mktime(datetime.now().timetuple()) * 1000,
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
            "js_timestamp": self.js_timestamp,
            "temp": self.temp,
            "humidity": self.humidity,
            "particles": self.particles,
            "eco2": self.eco2,
            "tvoc": self.tvoc,
        }

        return data

    def from_dict(self, data):
        for field in ["timestamp", "js_timestamp", "temp", "humidity", "particles", "eco2", "tvoc"]:
            if field in data:
                setattr(self, field, data[field])


class Settings(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature_lower_bound = db.Column(
        db.Integer,
        default=0)
    temperature_upper_bound = db.Column(
        db.Integer,
        default=100)
    humidity_lower_bound = db.Column(
        db.Integer,
        default=0)
    humidity_upper_bound = db.Column(
        db.Integer,
        default=100)
    co2_lower_bound = db.Column(
        db.Integer,
        default=1000)
    co2_upper_bound = db.Column(
        db.Integer,
        default=2000)
    particles_lower_bound = db.Column(
        db.Integer,
        default=50)
    particles_upper_bound = db.Column(
        db.Integer,
        default=100)
    tvoc_lower_bound = db.Column(
        db.Integer,
        default=3)
    tvoc_upper_bound = db.Column(
        db.Integer,
        default=5)
    
    def __repr__(self):
        return "<Settings {}>".format(self.string)

    def to_dict(self):
        data = {
            "id": self.id,
            "temperature_lower_bound": self.temperature_lower_bound,
            "temperature_upper_bound": self.temperature_upper_bound,
            "humidity_lower_bound": self.humidity_lower_bound,
            "humidity_upper_bound": self.humidity_upper_bound,
            "particles_lower_bound": self.particles_lower_bound,
            "particles_upper_bound": self.particles_upper_bound,
            "co2_lower_bound": self.co2_lower_bound,
            "co2_upper_bound": self.co2_upper_bound,
            "tvoc_lower_bound": self.tvoc_lower_bound,
            "tvoc_upper_bound": self.tvoc_upper_bound,
        }

        return data

    def from_dict(self, data):
        fields = ["id",
                    'temperature_lower_bound',
                    'temperature_upper_bound',
                    'humidity_lower_bound',
                    'humidity_upper_bound',
                    'particles_lower_bound',
                    'particles_upper_bound',
                    'co2_lower_bound',
                    'co2_upper_bound',
                    'tvoc_lower_bound',
                    'tvoc_upper_bound']

        for field in fields: 
            if field in data:
                setattr(self, field, data[field])
