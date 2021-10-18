from decouple import config
from gpiozero import Servo

pin = config('servo_pin')

servo = Servo(pin)

class ServoWrapper(Servo):
    def __init__(self, pin):
