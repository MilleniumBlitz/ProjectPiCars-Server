# coding: utf-8

import sys
sys.path.append('/home/pi/thunderborg')
from flask import Flask, render_template
from flask import request
import ThunderBorg

import threading

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

def activate_failsafe():
    print("activation fail safe")
    # Disable all motors
    TB.SetMotor1(0)
    TB.SetMotor2(0)
    # Enable failsafe led color
    TB.SetLedShowBattery(False)
    TB.SetLed1(255, 0, 0)

thread1 = threading.Timer(3, function = activate_failsafe)

@app.route("/failsafe")
def update_fail_safe():

    global thread1

    if thread1:
        thread1.cancel()
    thread1 = threading.Timer(3, function = activate_failsafe)
    thread1.start()

    #Enable the led to show the battery level
    TB.SetLedShowBattery(True)
    
    return "failsafe updated"


    
    



if __name__ == "__main__":
	app.run(host= '0.0.0.0', port=80, debug=True)




