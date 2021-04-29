import board
import busio
import datetime
import digitalio

import RPi.GPIO as g
import sys
import time

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

from WaterCtrl import vars

#g.setmode(g.BOARD)


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)

def setup_chan(mcp, input_pin):
    print("Setting up analog channel on pin {}".format(input_pin))
   # create an analog input channel on pin 0
    return AnalogIn(mcp, input_pin)

def get_analog_value(chan):
	print('Raw ADC Value: ', chan.value)
	print('ADC Voltage: ' + str(chan.voltage) + 'V')
	return {'raw': chan.value, 'voltage': chan.voltage}

# TODO Use keyword args here? Need to abstract away from 1-1 mapping for sensor and pump pins
sensor_pin = 3
sensor_pin2 = 12
pump_relay_control_pin = vars.PUMP_CTRL_PIN

NEEDS_WATER = False

all_pins = [sensor_pin, sensor_pin2, pump_relay_control_pin]

def shoutout_pins():
    for pin in all_pins:
        print("Setting {} as sensor pin".format(pin))

def setup_pump(pin):
    print("setting up pump on pin {}".format(pin))
    g.setup(pin, g.OUT)
    g.output(pin, g.LOW)
    g.output(pin, g.HIGH)

def pull_sensor_data(pin):
    g.setup(pin, g.IN)
    moisture_data = g.input(pin)
   # print("Moisture: {}".format(moisture_data))
    return moisture_data

def pump(pump_pin=10, seconds=3):
    print("Switching pump \# /#{} on for {} seconds".format(pump_pin, seconds))
    g.output(pump_pin, g.LOW)
    time.sleep(seconds)
    g.output(pump_pin, g.HIGH)


#while True:
#    time.sleep(3)
#    NEEDS_WATER = pull_sensor_data(3)
#    print(NEEDS_WATER)
#    if NEEDS_WATER:
#        print('Needs water')

#spi, cs, mcp = setup_spi(board.D22)
setup_pump(pump_relay_control_pin)
