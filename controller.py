# libraries for controlling lights
import board
import neopixel

class Controller:
    DOWN = 144

    def __init__(self, num_lights):
        # state of the lights
        self.num_lights = num_lights
        #self.color_on = color_on
        #self.color_off = color_off
        self.next_light = 0
        self.prev_light = 0

        # initialize the lights array, turn all lights off
        self.pixels = neopixel.NeoPixel(board.D18,
                                        self.num_lights,
                                        brightness=1,
                                        pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))