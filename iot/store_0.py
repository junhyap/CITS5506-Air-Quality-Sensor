import json
import requests

URL = "http://127.0.0.1:5000/api/airqualitys"

sensor_data = {'temp': 0, 'humidity': 0, 'particles': 0, 'eco2': 0, 'tvoc': 0}

r = requests.post(URL, json = sensor_data)

print(r.status_code, r.text)

