import board
import busio
import datetime
import digitalio
import RPi.GPIO as g
import sys
import time

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn as AI

# Create the SPI bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# Create the chip select
cs = digitalio.DigitalInOut(board.D22)
# Create the MCP object
mcp = MCP.MCP3008(spi, cs)

def setup_channel(mcp, input_pin):
	# Create an analog input channel on MCP pin 0
	return AI(mcp, input_pin)

def setup_pump(pin):
	g.setup(pin, g.OUT)
	g.output(pin, g.LOW)
	g.output(pin, g.HIGH)


