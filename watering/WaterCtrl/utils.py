import argparse
from datetime import datetime
import os
import time

import RPi.GPIO as g


def write(path, data, now):
	# TODO Error handling and just choose one place to display write-time
	with open(path, 'a+') as file:
		file.write('Recorded: {}\n{}\n'.format(now, data))


def write_to_log(data):
	# TODO: Fix this to be more clear in output, better organized, better naming conventions, and dynamic file path
	now = datetime.now()
	str_datetime = now.strftime('%Y-%m-%d - %I:%M:%s %p')
	time_parts = str_datetime.split(' ')
	date = time_parts[0]
	time = "-".join(time_parts[2:])

	#project_path = os.environ['/watering/WaterCtrl']
	workspace = os.environ['workspace']
	path="{}/watering/WaterCtrl/logs/sensors/{}/".format(workspace, date)

	if os.path.exists(path):
		write(path+"{}.txt".format(time), data, time)
	else:
		new_dir = "{}/{}/logs/sensors/{}"
		os.makedirs(new_dir.format(workspace, '/watering/WaterCtrl', date))
		file_name = "{}/{}.txt".format(new_dir, time)
		write(file_name, data, time)



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
