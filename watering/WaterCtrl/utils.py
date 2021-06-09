import argparse
from datetime import datetime
import os
import time
from decouple import config
import RPi.GPIO as g
import modules
# TODO Organize imports

workspace = config('workspace')
project_path = config('projectpath')

def get_time_parts(now):
	str_datetime = now.strftime('%Y-%m-%d - %I:%M:%s %p')
	time_parts = str_datetime.split(' ')
	date = time_parts[0]
	time = "-".join(time_parts[2:])

	return {'date': date, 'time': time}

# TODO Rename this function to avoid confusion / shadowing
def write(path, data, now):
	try:
		with open(path, 'a+') as file:
			file.write('Recorded: {}\n{}\n'.format(now, data))
	except Exception as e:
		print("Failed with {}".format(e))

def write_to_log(data, module, *prefix):
	# TODO: Fix this to be more clear in output, better organized, better naming conventions, and dynamic file path (only if pulling to generic log_helper?)
	now = datetime.now()
	date = get_time_parts(now)['date']
	time = get_time_parts(now)['time']

	path="{}{}/logs/{}/{}".format(workspace, project_path, module, date)
	file_path = "{}/{}.txt".format(path, time)

	# TODO write helper runction to create directory and then just do `if not os.path.... then create -- end block, drop into "write" like you normally would. 
	if os.path.exists(path):
		write(file_path, data, time)
	else:
		new_dir = "{}{}/logs/{}/{}".format(workspace, project_path, module, date)
		os.makedirs(new_dir)
		file_name = "{}/{}.txt".format(new_dir, time)
		write(file_name, data, time)


def read_all_pins(inputs, write_logs=False, *is_test):
        log_module = modules.SENSOR
        prefix = "TEST" if is_test else None
        # TODO: add default paths and filename patterns for various components (pumps, sensors, etc)
        for channel in list(inputs.values()):
                name = channel['name']
                sensor = channel['sensor']
                readings = get_analog_value(sensor)
                message = "Reading from {}:\n{}\n{}\n\n".format(name, sensor.value, sensor.voltage)
                print(prefix, message)
                if write_logs:
                        if name is not None:
                                write_to_log(message, log_module, prefix)

def get_analog_value(chan):
        # TODO Error handling and logging
        return {'raw': chan.value, 'voltage': chan.voltage}

# todo fix this issienwitj seconds not being loggrd
def pump(pump_pin, seconds, *is_test):
        prefix = "TEST" if is_test else None
        log_module = module.PUMP
        log_message = "{} pump \#{} - {} seconds at {}\n".format(actions.START, pump_pin, seconds, datetime.now())
        write_to_log(log_message, log_module, prefix)
        print(prefix, log_message)
        if not is_test:
                g.output(pump_pin, g.LOW)
                time.sleep(seconds)
                g.output(pump_pin, g.HIGH)
        else:
                time.sleep(seconds)

        log_message = "{} pump \#{} - {} seconds at {}\n".format(actions.STOP, pump_pin, seconds, datetime.now())
        print(prefix, log_message)
        write_to_log(log_message, log_module, prefix)

def run_all_pumps(pump_pins, seconds, *is_test, **custom_times):
        """
        Pumps don't run concurrently, they run in sequence of provided pins.
        This is partially due to ease of development, but also because in a small reservoir they can interfere with each other's operation.
        """
        prefix = "TEST" if is_test else None
        log_module = modules.PUMP
        pump_pin_times = {str(pin): seconds for pin in pump_pins}

        if custom_times:
                log_message ="Using custom times: {}\n".format(custom_times)
                write_to_log(log_message, log_module, prefix)
                print(prefix, log_message)
                for pin in custom_times:
                        pump_pin_times[pin] = custom_times[pin]

        for pin in pump_pin_times:
                time = pump_pin_times[pin]
                log_message = "Running pump \#{} for {} seconds at {}\n".format(pin, time, datetime.now())
                write_to_log(log_message, log_module, prefix)
                print(prefix, log_message)

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
