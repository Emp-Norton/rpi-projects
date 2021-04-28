import RPi.GPIO as g
import time

def get_analog_value(chan):
	print("Raw ADC: ", chan.value)
	print("ADC Voltage: ", chan.voltage)
	return {'raw': chan.value, 'voltage': chan.voltage}

def pump(pump_pin, seconds):
	print(pump_pin, seconds)
	g.output(pump_pin, g.LOW)
	time.sleep(seconds)
	g.output(pump_pin, g.HIGH)
