"""
Simple demo of reading messages from the TURRIS:DONGLE.

Just run it from the command line and watch the messages printed
on the standard output.
"""

from __future__ import print_function
import sys
import datetime

from device import Device

device = Device(device="/dev/ttyUSB0")
reader = device.gen_lines()
    while True:
        line = reader.next()
        #date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(line)
