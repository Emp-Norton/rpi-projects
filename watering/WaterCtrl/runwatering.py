import setup as s

from vars import PUMP_CTRL_PIN, NUM_INPUTS
from utils import get_analog_value, pump, read_all_pins, write_to_log

inputs = {}

if __name__ == '__main__':
	inputs = s.run_setup()

print(inputs)
