from app.api import bp
from flask import jsonify
from app.models import AirQuality

# change to timestamp
@bp.route("/airquality/<string:timestamp>", methods=["GET"])
def get_airquality(timestamp):
    return jsonify(AirQuality.query.get_or_404(timestamp).to_dict())


@bp.route("/airquality", methods=["GET"])
def get_airqualitys():
    pass


@bp.route("/airqualitys", methods=["POST"])
def create_airquality():
    pass


# change to timestamp
@bp.route("/airqualitys/<string:timestamp>", methods=["PUT"])
def update_airquality(id):
    pass
