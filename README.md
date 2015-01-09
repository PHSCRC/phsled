# PHS Computer & Robotics Club LED Matrix Project

I2C must be enabled in raspi-config, and the smbus module installed.

Usage: `sudo python scrollText.py "message" wait_time`

Piping stderr to `/dev/null` with `2>/dev/null` is reccomended if you do not have all four I2C devices connected.
