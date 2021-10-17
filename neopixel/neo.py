## Reminder that this must be run as root and is incompatible with python2.X, so install packages accordingly.

import board
import neopixel

from decouple import config

from util import *

ctrl_pin = config('pin')
num_pixels = int(config('numpixels'))

pixels = neopixel.NeoPixel(board.D18, num_pixels)
s = Strip(pixels, **{'pin':board.D18,'n':num_pixels})
