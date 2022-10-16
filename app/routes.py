from app.api import airquality
from flask import render_template
from app import app
from app.models import AirQuality
from app.models import Settings
from alembic import op
from app import db
from flask import jsonify, request, url_for, redirect, flash

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
    
@app.route("/")
@app.route("/main_dashboard")
def main_dashboard():

    settings = Settings.query.filter_by(id=0).first()

    if(not settings):

        settings = Settings()

        settings.id = 0
        # temperature bounds
        settings.temperature_lower_bound =  0
        settings.temperature_upper_bound =  100
        # humidity bounds
        settings.humidity_lower_bound = 0
        settings.humidity_upper_bound = 100
        # particles bounds
        settings.particles_lower_bound = 200
        settings.particles_upper_bound = 300
        # co2 bounds
        settings.co2_lower_bound = 1000
        settings.co2_upper_bound = 2000
        # tvoc bounds
        settings.tvoc_lower_bound = 20
        settings.tvoc_upper_bound = 40

        db.session.add(settings)
        db.session.commit()

    airqualityList = AirQuality.query.all()[-1]

    check = list(airqualityList.to_dict().values())[2:] == [0,0,0,0,0]
    
    if(check):
        airqualityList = AirQuality.query.all()[-2]
        flash('Displaying Results From {date}'.format(date=list(airqualityList.to_dict().values())[0]))

    timestamp = airqualityList.timestamp
    if(not timestamp):
        timestamp=0
    temp = airqualityList.temp
    if(not temp):
        temp=0
    humidity = airqualityList.humidity
    if(not humidity):
        humidity=0
    particles = airqualityList.particles
    if(not particles):
        particles=0
    eco2 = airqualityList.eco2
    if(not eco2):
        eco2=0
    tvoc = airqualityList.tvoc
    if(not tvoc):
        tvoc=0

    alert_count = 0
    warning_count = 0
    low_count = 0 

    # if the temperature is outside of the range flash a warning
    if (temp >= settings.temperature_upper_bound):
        warning_count+=1

    if (temp <= settings.temperature_lower_bound):
        low_count+=1
    
    # if the humidity is outside of the range flash a warning
    if (humidity >= settings.humidity_upper_bound):
        warning_count+=1

    if (humidity <= settings.humidity_lower_bound):
        low_count+=1

    # if the particles is outside of the range flash a warning
    if (particles >= settings.particles_upper_bound):
        alert_count+=1

    # if the particles is outside of the range flash an alert
    elif(particles >= settings.particles_lower_bound):
        warning_count+=1

    # if the co2 is outside of the range flash a warning
    if (eco2 >= settings.co2_upper_bound):
        alert_count+=1

    # if the co2 is outside of the range flash an alert
    elif(eco2 >= settings.co2_lower_bound):
        warning_count+=1

    # if the tvoc is outside of the range flash a warning
    if (tvoc >= settings.tvoc_upper_bound):
        alert_count+=1

    # if the tvoc is outside of the range flash an alert
    elif(tvoc >= settings.tvoc_lower_bound):
        warning_count+=1

    # flash a low temp or humidity warning
    if(low_count != 0):
        flash("Low Temp / Humidity Warning", 'low')

    if(warning_count == 0 and alert_count == 0 and low_count == 0):
        flash("The Air Quality is Good", 'success')

    elif(warning_count != 0 and alert_count != 0):
        flash("There is {alerts} alert(s) and {warnings} warning(s)".format(alerts=alert_count, warnings=warning_count), 'danger')

    elif(alert_count == 0):
        flash("There is {warnings} warning(s)".format(warnings=warning_count), 'warning')

    else:
        flash("There is {alerts} alert(s)".format(alerts=alert_count),'danger')
   

    return render_template('main_dashboard.html', 
    timestamp=timestamp,temp = temp, humidity = humidity, 
    particles = particles, eco2 = eco2, tvoc = tvoc,
    settings_data = settings)

@app.route("/main_temperature")
def main_temp():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template("main_temperature.html", main_temperature_data=data["items"])


@app.route("/main_humidity")
def main_humid():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template("main_humidity.html", main_humidity_data=data["items"])


@app.route("/main_co2")
def main_co2():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template("main_co2.html", main_co2_data=data["items"])


@app.route("/main_particles")
def main_part():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template("main_particles.html", main_particles_data=data["items"])


@app.route("/main_dust")
def main_dust():
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 20000, type=int), 20000)
    data = AirQuality.to_collection_dict(
        AirQuality.query, page, per_page, "api.get_airqualitys"
    )

    return render_template("main_dust.html", main_dust_data=data["items"])


@app.route("/main_settings")
def main_settings():
    settings = Settings.query.filter_by(id=0).first()
    return render_template("main_settings.html", settings_data=settings)


@app.route("/post_settings", methods=["GET", "POST"])
def post_settings():

    query = Settings.query.filter_by(id=0).first()

    if not (query and request.method == "GET"):

        if not query:
            # calling database instead of editing row
            # and adding a row
            query = Settings()

            # id of first row
            settings.id = 0
        
        data = request.form

        for key_pair in data:
            if(not data.get(key_pair) or str(data.get(key_pair)).strip()==''):
                flash('Values not updated', 'error')
                flash('Empty value entered for {key} Alert / Warning'.format(key=key_pair.replace("_"," ").split(" ")[0].title()))
                return render_template('main_settings.html', settings_data=query)

        else:
            # temperature bounds
            query.temperature_lower_bound = data["temperature_lower_bound"]
            query.temperature_upper_bound = data["temperature_upper_bound"]
            # humidity bounds
            query.humidity_lower_bound = data["humidity_lower_bound"]
            query.humidity_upper_bound = data["humidity_upper_bound"]
            # particles bounds
            query.particles_lower_bound = data["particles_lower_bound"]
            query.particles_upper_bound = data["particles_upper_bound"]
            # co2 bounds
            query.co2_lower_bound = data["co2_lower_bound"]
            query.co2_upper_bound = data["co2_upper_bound"]
            # tvoc bounds
            query.tvoc_lower_bound = data['tvoc_lower_bound']
            query.tvoc_upper_bound = data['tvoc_upper_bound']

            db.session.add(query)
            db.session.commit()
            
            flash('Settings successfully added')

    return render_template("main_settings.html", settings_data=query)
