from app.api import airquality
from flask import render_template
from app import app
from app.models import AirQuality
from alembic import op
from app import db
from flask import jsonify, request, url_for, redirect



@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Admin"}

    return render_template("index.html", title="Home", user=user)


@app.route('/post_user', methods=['POST'])
def post_user():
    data = request.form
    print(data.to_dict())
    print(request.form)
    
    airquality = AirQuality()
    airquality.from_dict(data)
    db.session.add(airquality)
    db.session.commit()  
    
    return redirect(url_for('dashboard'))
    

@app.route('/dashboard')
def dashboard():

    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('graph.html', airquality = data)


@app.route('/charts')
def charts():

    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )
    
    return render_template('charts.html', airquality = data['items'][0:5])


@app.route('/temperature_chart')
def temp_chart():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )
    
    return render_template('temperature_chart.html', airquality = data['items'][0:5])

@app.route('/basic_xy')
def basic_xy():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )
    
    return render_template('basic_xy.html', airquality = data['items'][0:5])