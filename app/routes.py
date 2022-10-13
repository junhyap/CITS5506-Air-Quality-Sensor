from app.api import airquality
from flask import render_template
from app import app
from app.models import AirQuality
from alembic import op
from app import db
from flask import jsonify, request, url_for, redirect



@app.route("/")
@app.route("/dashboard")
def index():
    user = {"username": "Admin"}

    return render_template("main_dashboard.html", title="Home", user=user)


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

    return render_template('graph.html', airquality = data['items'])


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

@app.route('/temp_db')
def temp_db():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('temperature_chart_db.html', temperature_data = data['items'])


@app.route('/main')
def main_paige():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main__single.html', airquality = data['items'][0:5])

@app.route('/main_dashboard')
def main_dash():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_dashboard.html', airquality = data['items'][0:5])

@app.route('/main_temperature')
def main_temp():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_temperature.html', main_temperature_data = data['items'])

@app.route('/main_humidity')
def main_humid():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_humidity.html', main_humidity_data = data['items'])

@app.route('/main_co2')
def main_co2():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_co2.html', main_co2_data = data['items'])

@app.route('/main_particles')
def main_part():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_particles.html', main_particles_data = data['items'])

@app.route('/main_dust')
def main_dust():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 100)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_dust.html', main_dust_data = data['items'])

@app.route('/main_settings')
def main_set():
    #page = request.args.get("page", 1, type=int)
    #per_page = min(request.args.get("per_page", 20000, type=int), 100)
    #data = AirQuality.to_collection_dict(
    #    AirQuality.query, page, per_page, "api.get_airqualitys"
    #)

    airqualityList = AirQuality.query.filter(AirQuality.timestamp.like('%2022-%')).limit(10).all()

    return render_template('main_settings.html', main_settings_data = airqualityList)
