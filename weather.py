from flask import Flask, render_template
from sense_hat import SenseHat

app = Flask(__name__)
@app.route('/')

def index():
    sense = SenseHat()
    
    celcius = round(sense.get_temperature(), 1)
    fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)
    direction = sense.get_orientation()
    roll = direction["roll"]
    
    windDirection = ""
    if roll < 45:
        windDirection = "North"
    elif roll < 90:
        windDirection = "North East"
    elif roll < 135:
        windDirection = "East"
    elif roll < 180:
        windDirection = "South East"
    elif roll < 225:
        windDirection = "South"
    elif roll < 270:
        windDirection = "South West"
    elif roll < 315:
        windDirection = "West"
    elif roll < 360:
        windDirection = "North West"
    
    return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit, humidity=humidity, pressure=pressure, windDirection=windDirection)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')