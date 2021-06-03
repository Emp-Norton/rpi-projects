import argparse
from datetime import datetime
import os
import time
from decouple import config
import RPi.GPIO as g

workspace = config('workspace')
project_path = config('projectpath')

def get_time_parts(now):
	str_datetime = now.strftime('%Y-%m-%d - %I:%M:%s %p')
	time_parts = str_datetime.split(' ')
	date = time_parts[0]
	time = "-".join(time_parts[2:])

	return {'date': date, 'time': time}

def write(path, data, now):
	try:
		with open(path, 'a+') as file:
			file.write('Recorded: {}\n{}\n'.format(now, data))
	except Exception as e:
		print("Failed with {}".format(e))

def write_to_log(data):
	# TODO: Fix this to be more clear in output, better organized, better naming conventions, and dynamic file path (only if pulling to generic log_helper?)
	now = datetime.now()
	date = get_time_parts(now)['date']
	time = get_time_parts(now)['time']

	path="{}{}/logs/sensors/{}".format(workspace, project_path, date)
	file_path = "{}/{}.txt".format(path, time)

	# TODO write helper runction to create directory and then just do `if not os.path.... then create -- end block, drop into "write" like you normally would. 
	if os.path.exists(path):
		write(file_path, data, time)
	else:
		new_dir = "{}{}/logs/sensors/{}".format(workspace, project_path, date)
		os.makedirs(new_dir)
		file_name = "{}/{}.txt".format(new_dir, time)
		write(file_name, data, time)


def read_all_pins(inputs, write_logs=False):
	# TODO: add default paths and filename patterns for various components (pumps, sensors, etc)
	for channel in list(inputs.values()):
		name = channel['name']
		sensor = channel['sensor']
		readings = get_analog_value(sensor)
		message = "Reading from {}:\n{}\n{}\n\n".format(name, sensor.value, sensor.voltage)

		if write_logs:
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
