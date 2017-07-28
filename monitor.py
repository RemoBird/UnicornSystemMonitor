#!/usr/bin/python
import unicornhat as unicorn
import os
import time
import datetime
from gpiozero import CPUTemperature


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)

cpu = CPUTemperature()
var = 1
t_min=65
t_max=85
t_steps=(t_max-t_min)/8

curv=[0,0,0,0,0,0,0,0]

while var == 1:
	print(cpu.temperature)
        time.sleep(2)
	pegel = int((cpu.temperature-t_min)/t_steps)-1
	print(pegel)
	curv.insert(0,pegel)
	curv.pop()
	unicorn.clear()
	for i in range(0, len(curv)):
		#print(i)
		#print(curv[i])
		for j in range(0, curv[i]):
			unicorn.set_pixel(i,j,256,0,128)
        	unicorn.set_pixel(i,curv[i],0,255,0)
	unicorn.show()
