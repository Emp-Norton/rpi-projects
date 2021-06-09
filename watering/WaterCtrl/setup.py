import board
import busio
import datetime
import digitalio
import RPi.GPIO as g
import sys
import time
import var

import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn as AI

from collections import defaultdict
from utils import get_analog_value, get_args, read_all_pins, run_all_pumps

        # TODO Create classes for hardware elements Pump, Sensor, and use methods. Way easier and cleaner.

def setup_mcp_interface():
        # TODO: investigate setting up multiple MCP3008 boards, and why P0 keeps getting fried (always no power or full power)
        # TODO Followup- just use chip select CE0,1,1.12, 2.1.12? Check docs.
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        print("Created the SPI bus {}".format(spi))

        cs = digitalio.DigitalInOut(board.CE0)
        print("Created the chip select {}".format(cs))

        mcp = MCP.MCP3008(spi, cs)
        print("Created the MCP object {}",format(mcp))

        return {'mcp': mcp, 'cs':cs, 'spi':spi}

def setup_channel(mcp, input_pin):
        return AI(mcp, input_pin)

def setup_pumps(pins):
        for pin in pins:
        	setup_pump(pin)

def setup_pump(pin):
        # TODO This is where the class would come in handy, and be able to return a set of pump objects instead of just referring by pin num and having no methods
        print("Setting up pump controller on pin {}".format(pin))
        g.setup(pin, g.OUT)
        g.output(pin, g.LOW)
        g.output(pin, g.HIGH)


def run_setup(num_inputs=vars.NUM_INPUTS, pump_pins=vars.PUMP_PINS):
        print("Running setup MCP/CS/SPI")
        interface = setup_mcp_interface()

        input_channels = {}
        args = get_args()
        args_dict = vars(args)
        print(args_dict)
        cs = interface['cs']
        mcp = interface['mcp']
        spi = interface['spi']

        for _, pin in args_dict:
            pin = int(pin)
            print(_, pin, args_dict)
            input_channels[pin] = {'name': args_dict["p{}".format(pin)], 'sensor': setup_channel(mcp, pin), 'pin': pin}

        setup_pumps(*pump_pins)

        return input_channels
