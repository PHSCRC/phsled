#!/usr/bin/env python

import time
import datetime
from Adafruit_8x8 import EightByEight
from LEDLetterValues import *

grids = [EightByEight(address=i) for i in range(0x70, 0x74)]

scrolled = 0

text = raw_input("What should I scroll: ").upper()
printcon = textTo2D(text)
print "Press CTRL+C to exit"

def outputPixel(x, y):
  if x < len(grids) * 16:
    grids[x // 16].setPixel(x % 16, y)


while(True):
  for y, v in enumerate(printcon):
    for x, i in enumerate(v):
      if i:
        a = x - scrolled
        if a >= 0:
          outputPixel(a, y)

  time.sleep(.05)
  for i in grids:
          i.clear()
  scrolled += 1
  if scrolled >= len(printcon[0]):
    scrolled = -5
