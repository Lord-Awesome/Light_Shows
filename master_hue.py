import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time
import random
import math
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)
from simultaneous_hue_shift import simultaneous_hue_shift
from serialized_hue_shift import serialized_hue_shift
from non_serialized_hue_shift import non_serialized_hue_shift
from random_light_display import random_light_display

pixels.clear()

# Function 1. All the LEDs light at the same time to the same color. Color iterates through spectrum.
wait1 = 0
speed1 = 1.75
simultaneous_hue_shift(wait1)

# Function 2. Sequential LEDs display sequential colors in the spectrum. Each LED iterates through the spectrum.
# Increasing speed makes the iteration coarser so the effect is more noticeable.
wait2 = 0
speed2 = 1.75
serialized_hue_shift(wait2, speed2)

#Function 3. LEDs are still lit sequentially so the colors appear to travel along the strand, but the colors are random.
wait3 = 0
speed3 = 1.75
non_serialized_hue_shift(wait3, speed3)

#The colors and placement are random, so it's just a crazy light show. Precursor to rave.py
wait4 = 0
random_light_display(wait4)
