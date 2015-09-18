#!/usr/bin/env python

import time, sys

from traceback import print_exc

from Adafruit_LEDBackpack import LEDBackpack
from LEDLetterValues import textTo2D

grids = [LEDBackpack(address=i) for i in range(0x70, 0x74)]

def main():
  while True:
    printcon = textTo2D(time.strftime(".%I:.%M:.%S %p "))
    for y, v in enumerate(printcon):
      buffers = [0x00, 0x00, 0x00, 0x00]
      for a, i in enumerate(v):
        if i:
          if a >= 0 and a < len(grids) * 16:
            buffers[a // 16] = buffers[a // 16] | 1 << (a % 16)
      for i, grid in enumerate(grids):
        grid.setBufferRow(y, buffers[i], update=False)
    for i in grids:
      i.writeDisplay()
    time.sleep(1)

if __name__ == "__main__":
  try:
    main()
  except BaseException as err:
    print_exc(err)
    for i in grids:
      for y in range(8):
        i.setBufferRow(y, 0x00, update=False)
      i.writeDisplay()
