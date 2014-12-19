#!/usr/bin/python

import time
import datetime
from Adafruit_LEDBackpack.Adafruit_8x8 import EightByEight
from LEDListCreate import EightBySixteen


grid = EightByEight(address=0x70)
grid2 = EightByEight(address=0x71)
grid3 = EightByEight(address=0x72)
grid4 = EightByEight(address=0x73)
currentgrid= 0
scrolllen=0
phrase = EightbySixteen()
text = input ('What should I scroll: ' )
printcon = phrase.textToArray(text)
print "Press CTRL+Z to exit"

# Continually update the 8x8 display one pixel at a time
while(True):
  for x in range(len(printcon)):
  	for y in range(len(printcon[x])):
  		for z in range(len(printcon[x][y])):
  			if printcon[x][y][z] == 1:
  				a = z+(5*x)-scrolllen
  				if a >= 0:
  					currentgrid =1
  				if a >= 16:
  					currentgrid =2
  				if a >= 32:
  					currentgrid =3
  				if a >= 48:
  					currentgrid =4
  				if a >= 64:
  					currentgrid =5
  				if currentgrid==1:
	  				grid.setPixel(a,y)
  				if currentgrid==2:
  					grid2.setPixel(a-16,y)
  				if currentgrid==3:
  					grid3.setPixel(a-32,y)
  				if currentgrid==4:
  					grid4.setPixel(a-48,y)
  				if a== -5:
  					wait = printcon[x]
  					printcon.remove(printcon[x])
  					printcon.append(wait)
  					scrolllen = 0
  			elif printcon[x][y][z] != 0:
  				a = z+(5*x)-scrolllen
  				if a >= 0:
  					currentgrid =1
  				if a >= 16:
  					currentgrid =2
  				if a >= 32:
  					currentgrid =3
  				if a >= 48:
  					currentgrid =4
  				if a >= 64:
  					currentgrid =5
  				if currentgrid==1:
	  				grid.clearPixel(a,y)
  				if currentgrid==2:
  					grid2.clearPixel(a-16,y)
  				if currentgrid==3:
  					grid3.clearPixel(a-32,y)
  				if currentgrid==4:
  					grid4.clearPixel(a-48,y)
  				if a == -5:
  					wait = printcon[x]
  					printcon.remove(printcon[x])
  					printcon.append(wait)
  					scrolllen = 0
  time.sleep(.1)
  scrolllen += 1