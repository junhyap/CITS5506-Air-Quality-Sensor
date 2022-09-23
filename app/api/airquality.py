from app.api import bp

# change to timestamp
@bp.route("/airquality/<string:timestamp>", methods=["GET"])
def get_airquality(id):
    pass


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
