# PHSCRC LED Matrix Project
Download and setup the code from the [Adafruit-Raspberry-Pi-Python-Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/) repository. Make sure wget and unzip are installed. Use the following commands or run setup.sh.
```bash
# download
wget https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/archive/master.zip
# unzip
unzip master.zip
# move around
cp -RL Adafruit-Raspberry-Pi-Python-Code-master/Adafruit_LEDBackpack/ adafruitledbackpack
# create __init__.py
touch adafruitledbackpack/__init__.py
# clean up
rm -r Adafruit-Raspberry-Pi-Python-Code-master
rm master.zip
```
I2C must also be enabled in raspi-config.
