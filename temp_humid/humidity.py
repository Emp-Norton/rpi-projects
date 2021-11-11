import logging

import adafruit_dht
from adafruit_ahtx0 import AHTx0

import board
from decouple import config

pin1 = config('pin1') or 5
pin2 = config('pin2') or 4

# I2C device will only work if there are no other I2C devices on the bus, unless manually configure I2C0 or setup multiplexer
i2c = board.I2C()
aht = AHTx0(i2c)
dht = adafruit_dht.DHT11(pin1)
dht2 = adafruit_dht.DHT11(pin2)

def to_fahrenheit(d):
    return (d * (9/5)) + 32

def to_celcius(d):
    return (d - 32) * (5/9)

def get_temperature(scale='f'):
    if scale == 'f':
        score1 = to_fahrenheit(dht.temperature)
        score2 = to_fahrenheit(dht2.temperature)
        score3 = to_fahrenheit(aht.temperature)
        print(f"DHT1: {score1}\nDHT2: {score2}\n")
        print(f"\n-->AHT: {score3}\n")
        return (score1 + score2 + score3)/3

    return (dht.temperature + dht2.temperature + aht.temperature)/3

def get_humidity():
    score1 = dht.humidity
    score2 = dht2.humidity
    score3 = aht.relative_humidity
    print(f"DHT1: {score1}%\nDHT2: {score2}%")
    print(f"\n-->AHT: {score3}%")
    return (dht.humidity + dht2.humidity + score3)/3

def humidity():
    print(f"Humidity: {get_humidity()}%")
