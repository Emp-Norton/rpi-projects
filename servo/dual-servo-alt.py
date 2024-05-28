from decouple import config
from gpiozero import Servo

class ServoWrapper(Servo):
    def init(self, pin):
        super().init(pin)

def stop(self):
    self.value = None
class PTZModule:
    def init(self, pan_pin, tilt_pin):
        self.pan_servo = ServoWrapper(pan_pin)
        self.tilt_servo = ServoWrapper(tilt_pin)

def setup(self):
    self.pan_servo.stop()
    self.tilt_servo.stop()
if name == "main":
    pan_pin = config('pan_pin')
    tilt_pin = config('tilt_pin')

ptz = PTZModule(pan_pin, tilt_pin)
ptz.setup()