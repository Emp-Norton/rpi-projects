import board
import busio
import datetime
import digitalio
import RPi.GPIO as g
import sys
import time

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn as AI

from WaterCtrl.vars import PUMP_CTRL_PIN, NUM_INPUTS


def setup_mcp_interface():
	# Create the SPI bus
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

	# Create the chip select
	cs = digitalio.DigitalInOut(board.D22)

	# Create the MCP object
	mcp = MCP.MCP3008(spi, cs)

	return {'mcp': mcp, 'cs':cs, 'spi':spi}

def setup_channel(mcp, input_pin):
	# TODO: Get these pin numbers from cli when starting program - needs to be variable
	# Create an analog input channel on MCP pin 0
	return AI(mcp, input_pin)


def setup_pump(pin):
	# TODO: Get these pin numbers from cli when starting program - needs to be variable
	g.setup(pin, g.OUT)
	g.output(pin, g.LOW)
	g.output(pin, g.HIGH)


def run_setup(num_inputs=NUM_INPUTS, pump_pin=PUMP_CTRL_PIN):
	input_channels = {}
	interface = setup_mcp_interface()

	cs = interface['cs']
	mcp = interface['mcp']
	spi = interface['spi']

	for i in range(0, num_inputs):
		print(i)
		input_channels = {str(i): setup_channel(mcp, i)}
		print(input_channels)

	setup_pump(pump_pin)

	return input_channels
