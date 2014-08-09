#! /usr/bin/python2.7
# -*- coding: utf8 -*-

"""
Ce programme permet de tester la connexion a la Nunchuk en faisant varier
l'intensité lumineuse d'une LED reliée au pin GPIO PIN_LED selon l'inclinaison
verticale de la Nunchuk
"""

import RPi.GPIO as GPIO
import time
import cwiid

PIN_LED=17

def get_pitch(wm):
	a=wm.state['nunchuk']['acc'][1]
	a-=70
	if a>100:
		return 100
	else:
		return a

print "Press 1+2"
wm=cwiid.Wiimote()
time.sleep(1)
wm.rpt_mode=cwiid.RPT_NUNCHUK
time.sleep(1)
print wm.state

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

p = GPIO.PWM(PIN_LED, 50)
p.start(0)
p.ChangeDutyCycle(50)

while 1:
	a=get_pitch(wm)
	p.ChangeDutyCycle(a)
	print a
	time.sleep(0.1)
