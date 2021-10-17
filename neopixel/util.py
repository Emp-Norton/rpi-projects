import time
import board

from decouple import config
from neopixel import NeoPixel

num_pixels = int(config('numpixels')) or 240
pin = config('pin')

class Strip(NeoPixel):
    def __init__(self, pixels, **kwargs):
        super().__init__(**kwargs)
        #self.data= dict(kwargs)
        self.pixels = pixels
        self.num_pixels = len(self.pixels)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.OFF = (0,0,0)

    def off(self):
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
            print(j)
            for i in range(self.num_pixels):
                pi = i + j
                pixel_index = (i * 256 // self.num_pixels) + j
                print(pixel_index,pi)
                self.pixels[i] = self.wheel(pixel_index & 255)
                self.pixels.show()
                time.sleep(wait)


    def xmas(self, wait, m=1):
        """ Run with ```while True: m = (m + 1) % 2; s.xmas(1, m)``` """
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
