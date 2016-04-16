# coding: utf-8

from flask import Flask, render_template
from flask import request
import wiringpi2
import RPi.GPIO as GPIO
import psutil
import os
app = Flask(__name__)

# Mise en route de WiringPi
wiringpi2.wiringPiSetup()

# Initialisation du GPIO
wiringpi2.pinMode(1, 2)  # PWM

wiringpi2.pinMode(2, 1)  # Premier moteur
wiringpi2.pinMode(3, 1)

wiringpi2.pinMode(4, 1)  # Deuxieme moteur
wiringpi2.pinMode(5, 1)

wiringpi2.pwmSetMode(0)  # Mode PWM


@app.route("/")
def hello():
	return render_template('index.html', cpuUsage=psutil.cpu_percent(interval=None), cpuTemp=int(float(getCPUtemperature())), rpiversion=GPIO.RPI_REVISION)
	
	
@app.route("/alive")
def alive():
    return "alive"


@app.route("/direction/Gauche")
def direction_gauche():
    wiringpi2.digitalWrite(4, 0)
    wiringpi2.digitalWrite(5, 1)
    return "gauche"


@app.route("/direction/Droite")
def direction_droite():
    wiringpi2.digitalWrite(4, 1)
    wiringpi2.digitalWrite(5, 0)
    return "droite"


@app.route("/direction/Aucune")
def direction_aucune():
    wiringpi2.digitalWrite(4, 0)
    wiringpi2.digitalWrite(5, 0)
    return "tout droit"

# Controle la puissance et le sens de rotation


@app.route("/power/<duty>/<sens>")
def power(duty, sens):
    if int(sens) < 90:
        wiringpi2.digitalWrite(2, 1)
        wiringpi2.digitalWrite(3, 0)
        print "sens normal"
    elif int(sens) > 90:
        wiringpi2.digitalWrite(2, 0)
        wiringpi2.digitalWrite(3, 1)
        print "sens inverse"
    wiringpi2.pwmWrite(1, int(duty))
    return "Changement puissance"
	
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))
        return True
	

if __name__ == "__main__":
	app.run(host= '0.0.0.0', port=80, debug=True)




