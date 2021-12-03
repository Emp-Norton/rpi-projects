import logging
import RPi.GPIO as GPIO
import gpiozero as g

from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, filename="sensors.log", filemode="a", format="%(name)s-%(levelname)s-%(message)s")

sensors_array = [g.MCP3008(channel=i) for i in range(8)]

def sense(sensors=sensors_array):
    logging.info(f"\n--------------------------------New Sensor Reading---------------------------")
    for s in sensors:
        output=f"Value: {s.value} - Voltage: {s.voltage}"
        print(output)
        write_log(output)

def write_log(message):
    now = datetime.now()
    str_datetime = now.strftime('%Y-%m-%d - %I:%M:%s %p')
    logging.info(f"{str_datetime}: {message}")


