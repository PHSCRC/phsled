#!/bin/bash

# Downloads code from https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/
# and sets it up to work with the PHSCRC LED Matrix Project code

# download
wget https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/archive/master.zip &&
# unzip
unzip master.zip &&
# move around
cp -RL Adafruit-Raspberry-Pi-Python-Code-master/Adafruit_LEDBackpack/ adafruitledbackpack &&
# create __init__.py
touch adafruitledbackpack/__init__.py &&
# clean up
rm -r Adafruit-Raspberry-Pi-Python-Code-master && rm master.zip
