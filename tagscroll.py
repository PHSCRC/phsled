#!/usr/bin/env python

from nfc import ContactlessFrontend
import os, time, sys

from traceback import print_exc

from Adafruit_LEDBackpack import LEDBackpack
from LEDLetterValues import textTo2D

from timeit import default_timer
from threading import Thread

grids = [LEDBackpack(address=i) for i in range(0x70, 0x74)]
wait_time = .08 # float(sys.argv[2] if len(sys.argv) > 2 else raw_input("Wait time: "))
original_text = sys.argv[1] if len(sys.argv) > 1 else "Ready..."
printcon = textTo2D(original_text)

def main():
  global printcon
  scrolled = 0
  while printcon != False:
    start = default_timer()
    original_con = printcon
    for y, v in enumerate(original_con):
      if printcon != original_con:
        break
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
    if scrolled >= len(original_con[0]) / 2 + 6:
      scrolled = 0
    if original_con != printcon:
      scrolled = 0
  printcon = True

def set_message(tag):
  global printcon
  try:
    message = tag.ndef.message[0].data[3:]
  except Exception as err:
    print_exc(err)
    print(tag.pretty())
  else:
    print(message)
    if message == "sys.exit":
      for i in grids:
        for y in range(8):
          i.setBufferRow(y, 0x00, update=False)
        i.writeDisplay()
      exit(0)
    message = message.replace("$ORIGINAL", original_text)
    printcon = textTo2D(message)
  return True

if __name__ == "__main__":
  try:
    #os.system("nfc-list")
    main_thread = Thread(target=main)
    main_thread.daemon = True
    main_thread.start()
    print("Started main thread")
    clf = ContactlessFrontend("tty:AMA0:pn532")
    print(clf)
    while True:
      clf.connect(rdwr={"on-connect":set_message})
  except BaseException as err:
    print_exc()
    for i in grids:
      for y in range(8):
        i.setBufferRow(y, 0x00, update=False)
      i.writeDisplay()
