import time
import board

from decouple import config
from neopixel import NeoPixel

num_pixels = int(config('numpixels')) or 240
pin = config('pin')

class Strip(NeoPixel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.num_pixels = num_pixels
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.OFF = (0,0,0)

    def off(self):
    # TODO Switch this with below
        self.pixels.fill(self.OFF)

    def fill(self, color):
        return super().fill(color)


    def wheel(self, pos):
        """ Input a value 0 to 255 to get a color value. The colours are a transition r - g - b - back to r."""
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)


    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
                self.pixels.show()
                time.sleep(wait)


    def xmas(self, wait, m=1):
        def xmas_helper(wait, m):
            self.pixels = NeoPixel(board.D18, num_pixels) if not self.pixels else self.pixels
            for i in range(len(self.pixels)):
                if i % 2 == m:
                     self.pixels[i] = self.RED
                else:
                     self.pixels[i] = self.GREEN
            self.pixels.show()
            time.sleep(wait)
        while True:
            m = (m + 1) % 2
            xmas_helper(wait, m)


    def increment_colors(self, wait, offset=0):
        while True:
            for p in range(self.num_pixels+offset):
                q = (p + offset) % 255
                self[p % self.num_pixels] = self.wheel(q & 255)
                self.show()
                offset += 1
                time.sleep(wait)
