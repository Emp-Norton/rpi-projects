from decouple import config
from gpiozero import Servo

pins = config('pins', [13, 18])

class ServoWrapper(Servo):
    def __init__(self, pins=pins):
        for pin in pins:
            self.servoes.append(super().__init__(int(pin)))

    def stop(self):
        self.value = None

    def setup_servo(selfpin):
        servo = ServoWrapper(pin)
        servo.stop()
        return servo

    def setup(self, pins=pins):
        [self.servos.append(self.setup_servo(pin)) for pin in pins]

