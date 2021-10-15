## Reminder that this must be run as root and is incompatible with python2.X, so install packages accordingly.

import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 300)

