#!/usr/bin/env python

import time, sys
from Adafruit_LEDBackpack import LEDBackpack
from LEDLetterValues import *
from timeit import default_timer
grids = [LEDBackpack(address=i) for i in range(0x70, 0x74)]

wait_time = float(sys.argv[2] if len(sys.argv) > 2 else raw_input("Wait time: "))
text = sys.argv[1] if len(sys.argv) > 1 else raw_input("What should I scroll: ")
printcon = textTo2D(text)

print "Press CTRL+C to exit"

def main():
  scrolled = 0
  while True:
    start = default_timer()
    for y, v in enumerate(printcon):
      buffers = [0x00, 0x00, 0x00, 0x00]
      for x, i in enumerate(v):
        if i:
          a = x - scrolled
          if a >= 0 and a < len(grids) * 16:
            buffers[a // 16] = buffers[a // 16] | 1 << (a % 16)
      for i, grid in enumerate(grids):
        grid.setBufferRow(y, buffers[i], update=False)
  
 
    for i in grids:
      i.writeDisplay()
    final = default_timer()-start
    if final <= wait_time:
      time.sleep(wait_time - final)
    scrolled += 1
    if scrolled >= len(printcon[0]) / 2 + 6:
      scrolled = 0
      if "--once" in sys.argv:
        exit(0)

if __name__ == "__main__":
  try:
    main()
  except BaseException:
    for i in grids:
      for y in range(8):
        i.setBufferRow(y, 0x00, update=False)
      i.writeDisplay()
