# -*- coding: utf8 -*-
"""
Ceci est le programme principal qui va faire la liaison entre la manette
et l helicoptere
"""

import time
import cwiid
import os
import subprocess
from fonction import *


if __name__ == '__main__':
	print "Press 1+2"
	wm=cwiid.Wiimote()
	time.sleep(1)
	wm.rpt_mode=cwiid.RPT_NUNCHUK | cwiid.RPT_BTN
	time.sleep(1)
	print wm.state

	origin=calibrate(wm)



	count=0
	light=0
	while 1 :
		count%=10000
		if count==0: update_batt(wm)
		roll  = get_roll(wm,origin)
		pitch = get_pitch(wm,origin)
		x     = get_x(wm,origin)
		y     = get_y(wm,origin)
		command=str(pitch)+'_'+str(roll)+'_'+str(x)+'_'+str(y)+'_'+str(light)
		print "sent ",command
		subprocess.call("irsend SEND_ONCE SILVERLIT HELI_"+command+"_"+str(gen_check(pitch,roll,x,y,light)), shell=True)

		#Début des commandes
		if wm.state['nunchuk']['buttons'] == 2 :
			print "C pressed"
			light = (light+1)%2
		elif wm.state['nunchuk']['buttons'] == 1 :
			print "Z pressed"
			origin=pause(wm,origin)
			time.sleep(0.2)
		time.sleep(0.05)
		count+=1
