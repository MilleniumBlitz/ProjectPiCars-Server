# coding: utf-8

import sys
sys.path.append('/home/pi/thunderborg')
from flask import Flask, render_template
from flask import request
import ThunderBorg
app = Flask(__name__)


#ThunderBorg init
TB = ThunderBorg.ThunderBorg()
TB.Init()
TB.SetLedShowBattery(1)  

@app.route("/")
def hello():
	return "alive"

@app.route("/batteryVoltage")
def get_battery_voltage():
	return str(round(TB.GetBatteryReading(), 2))

@app.route("/direction/Gauche")
def direction_gauche():
    TB.SetMotor1(-1)
    return "gauche"
	
@app.route("/direction/Droite")
def direction_droite():
    TB.SetMotor1(1)
    return "droite"

@app.route("/direction/Aucune")
def direction_aucune():
    TB.SetMotor1(0)
    return "tout droit"

# Controle la puissance et le sens de rotation
@app.route("/power/<duty>")
def power(duty):
    TB.SetMotor2(-float(duty) / 100)
    return "Changement puissance"

if __name__ == "__main__":
	app.run(host= '0.0.0.0', port=80, debug=True)




