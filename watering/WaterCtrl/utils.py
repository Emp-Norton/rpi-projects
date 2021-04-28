import RPi.GPIO as g


def get_analog_value(chan):
	print("Raw ADC: ", chan.value)
	print("ADC Voltage: ", chan.voltage)
	return {'raw': chan.value, 'voltage': chan.voltage}
