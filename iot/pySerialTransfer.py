from urllib.error import URLError
import serial
import requests
import json

URL = "http://127.0.0.1:5000/api/airqualitys"

Arduino = serial.Serial('/dev/ttyACM0',9600)

def main():
    i = 0
    while True:
        data = Arduino.readline()[:-2]
        i += 1
        if i < 4:
            continue
        else:
            if data:
                # Cleaning data
                temp, humidity, particles, eco2, tvoc = get_data(data)
                # Sending data to server
                try:
                    sensor_data = {'temp': temp, 'humidity': humidity, 'particles': particles, 'eco2': eco2, 'tvoc': tvoc}
                    # print(sensor_data)
                    r = requests.post(URL, json = sensor_data)
                    print(r.status_code, r.text)
                except URLError as e:
                    print(e.reason)


def get_data(this_data):
    data = this_data.decode('utf-8').split(';')
    if len(data) == 5:
        temp = data[0]
        humidity = data[1]
        particles = data[2]
        eco2 = data[3]
        tvoc = data[4]
        return temp, humidity, particles, eco2, tvoc
    else:
        return 'N','N','N','N','N'        

main()

