import argparse
from datetime import datetime
import RPi.GPIO as g
import time


def write_to_log(data):
	# TODO: Fix this to be more clear in output, better organized, better naming conventions, and dynamic file path
	now = datetime.now()
	accurate = now.strftime('%m/%d/%Y - %I:%M:%s %p')
	path='/home/pi/projects/rpi-projects/watering/WaterCtrl/logs/sensors/{}.txt'.format(now.strftime("%I:%M:%s %p"))
	with open(path, 'a') as file:
		file.write('written {}\n{}\n'.format(now, data))

def read_all_pins(inputs, write_logs=False):
	# TODO: add default paths and filename patterns for various components (pumps, sensors, etc)
	for channel in list(inputs.values()):
		name = channel['name']
		sensor = channel['sensor']
		readings = get_analog_value(sensor)
		message = "\nReading from {}:\n{}\n{}\n\n".format(name, sensor.value, sensor.voltage)
		print(message)

		if write_logs:
			print("writing readings to log")
			if name is not None:
				write_to_log(message)

def get_analog_value(chan):
	return {'raw': chan.value, 'voltage': chan.voltage}

def pump(pump_pin, seconds):
	# TODO: Log pump activity in terms of which relay pump, duration, etc
	print(pump_pin, seconds)
	g.output(pump_pin, g.LOW)
	time.sleep(seconds)
	g.output(pump_pin, g.HIGH)


def get_args():
	argp = argparse.ArgumentParser()
	argp.add_argument('--p0', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p1', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p2', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p3', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p4', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p5', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p6', help="This argument sets which pin will measure the plant or plant group provided")
	argp.add_argument('--p7', help="This argument sets which pin will measure the plant or plant group provided")

	return argp.parse_args()
