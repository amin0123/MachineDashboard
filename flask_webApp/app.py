from flask import Flask, render_template
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

app = Flask(__name__)


@app.route('/on')
def on():
    toarduino = "<ledon>"
    toarduinoencoded = toarduino.encode()
    ser.write(toarduinoencoded)
    return render_template('on.html')



@app.route('/off')
def off():
    toarduino2 = "<ledoff>"
    toarduinoencoded2 = toarduino2.encode()
    ser.write(toarduinoencoded2)
    return render_template('off.html')