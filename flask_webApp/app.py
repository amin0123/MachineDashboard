from flask import Flask, render_template
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)
case =""
toarduino=""
@app.route('/')
@app.route('/on2')
def on():
    if toarduino = "<ledon>":
        case = "True"
    elif toarduino
        case ="False"
    
    toarduinoencoded = toarduino.encode()
    ser.write(toarduinoencoded)
    return render_template('on2.html',case=case)


@app.route('/off2')
def off():
    toarduino2 = "<ledoff>"
    toarduinoencoded2 = toarduino2.encode()
    ser.write(toarduinoencoded2)
    return render_template('off2.html')


 
if __name__ == '__main__':
    app.run(debug = True)   
