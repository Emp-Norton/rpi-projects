import setup as s

from utils import get_analog_value, pump, read_all_pins, run_all_pumps, write_to_log

inputs = {}

if __name__ == '__main__':
	inputs = s.run_setup()
	# TODO CLI argument to modify is_test

read_all_pins(inputs, write_logs=True)
