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
from WaterCtrl.utils import get_analog_value, pump

def setup_mcp_interface():
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	print("Created the SPI bus {}".format(spi))

	cs = digitalio.DigitalInOut(board.D22)
	print("Created the chip select {}".format(cs))

	mcp = MCP.MCP3008(spi, cs)
	print("Created the MCP object {}",format(mcp))

	return {'mcp': mcp, 'cs':cs, 'spi':spi}

def setup_channel(mcp, input_pin):
	# TODO: Get these pin numbers from cli when starting program - needs to be variable
	ai = AI(mcp, input_pin)
	print("Created an analog input {} on MCP3008 Channel \#{}".format(ai, input_pin))

	return ai

def setup_pump(pin=PUMP_CTRL_PIN):
	# TODO: Get these pin numbers from cli when starting program - needs to be variable
	print("Setting up pump controller on pin {}".format(pin))
	g.setup(pin, g.OUT)
	g.output(pin, g.LOW)
	g.output(pin, g.HIGH)


def run_setup(num_inputs=NUM_INPUTS, pump_pin=PUMP_CTRL_PIN):
	input_channels = {}

	print("Running setup MCP/CS/SPI")
	interface = setup_mcp_interface()

	cs = interface['cs']
	mcp = interface['mcp']
	spi = interface['spi']

	for i in range(0, num_inputs):
		input_channels[str(i)] = setup_channel(mcp, i)

	setup_pump(pump_pin)

	return input_channels

