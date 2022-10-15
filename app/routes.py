from app.api import airquality
from flask import render_template
from app import app
from app.models import AirQuality
from app.models import Settings
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
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_dashboard.html', airquality = data['items'])

@app.route('/main_temperature')
def main_temp():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_temperature.html', main_temperature_data = data['items'])

@app.route('/main_humidity')
def main_humid():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_humidity.html', main_humidity_data = data['items'])

@app.route('/main_co2')
def main_co2():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_co2.html', main_co2_data = data['items'])

@app.route('/main_particles')
def main_part():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_particles.html', main_particles_data = data['items'])

@app.route('/main_dust')
def main_dust():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template('main_dust.html', main_dust_data = data['items'])

@app.route('/main_settings')
def main_settings():
    settings = Settings.query.filter_by(id=0).first()
    return render_template('main_settings.html', main_settings_data=settings)


@app.route('/post_settings', methods=['POST'])
def post_settings():

    data = request.form

    settings = Settings.query.filter_by(id=0).first()
    # temperature bounds
    settings.temperature_lower_bound = form['temperature_lower_bound']
    settings.temperature_lower_bound = form['temperature_upper_bound']
    # humidity bounds
    settings.humidity_lower_bound = form['humidity_lower_bound']
    settings.humidity_upper_bound = form['humidity_upper_bound']
    # particles bounds
    settings.particles_lower_bound = form['particles_lower_bound']
    settings.particles_lower_bound = form['particles_upper_bound']
    # co2 bounds
    settings.co2_lower_bound = form['co2_lower_bound']
    settings.co2_lower_bound = form['co2_upper_bound']
    # tvoc bounds
    settings.co2_lower_bound = form['tvoc_lower_bound']
    settings.co2_lower_bound = form['tvoc_upper_bound']

    db.session.commit()

    return redirect(url_for('main_settings'))


"""
    @app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')
"""