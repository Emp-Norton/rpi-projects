import argparse
import datetime
import RPi.GPIO as g
import time


def write_to_log(data, path='./'):
	with open(path, 'a') as file:
		file.write('written {}\n{}\n'.format(datetime.datetime.now(), data))

def read_all_pins(inputs, write_logs=False):
	for channel in inputs:
		sensor_info = inputs[channel]
		readings = get_analog_value(sensor_info['sensor'])

		message = "Reading from {}:\n\n{}\n\nRAW: {}\nVOLTAGE: {}\n\n".format(datetime.datetime.now, sensor_info['name'], reading['raw'], reading['voltage'])
		print("writing readings to log")
		print(message)
		write_to_log(message)

def get_analog_value(chan):
	print("Raw ADC: ", str(chan.value))
	print("ADC Voltage: ", chan.voltage)
	return {'raw': chan.value, 'voltage': chan.voltage}

def pump(pump_pin, seconds):
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
