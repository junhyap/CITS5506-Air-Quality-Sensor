from app.api import bp


@bp.route("/airquality/<int:id>", methods=["GET"])
def get_airquality(id):
    pass


@bp.route("/airquality", methods=["GET"])
def get_airqualitys():
    pass


@bp.route("/airqualitys", methods=["POST"])
def create_airquality():
    pass


# change to timestamp
@bp.route("/airqualitys/<int:id>", method=["PUT"])
def update_airquality(id):
    pass
