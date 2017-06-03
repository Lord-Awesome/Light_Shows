import Adafruit_WS2801
import Adafrit_GPIO.SPI as SPI
import time
import random
PIXEL_COUNT = 160
PIXEL_CLOCK = 11
PIXEL_DOUT  = 10
pixels = Adafruit.WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

pixels.clear()
wait = 0.1

# Light all of the lights to the same hue; scroll through spectrum
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(0, 255, i)
    for j in range(pixels.count()):
        pixels.set_pixel(j, color)
    pixels.show()
    if wait > 0:
        time.sleep(wait)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(0, 255-i, 255)
    for j in range(pixels.count()):
        pixels.set_pixel(j,color)
    pixels.show()
    if wait > 0:
        time.sleep(wait)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(i, 0, 255)
    for j in range(pixels.count()):
        pixels.set_pixel(j,color)
    pixels.show()
    if wait > 0:
        time.sleep(wait)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(255, 0, 255-i)
    for j in range(pixels.count()):
        pixels.set_pixel(j,color)
    pixels.show()
    if wait > 0:
        time.sleep(wait)

# Do the same thing, but every light is a different color
pixels.clear()
time.sleep(2)
color_list = []

# Generate the colors
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(0, 255, i)
    color_list.append(color)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(0, 255-i, 255)
    color_list.append(color)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(i, 0, 255)
    color_list.append(color)
for i in range(256):
    color = Adafruit_WS2801.RGB_to_color(255, 0, 255-i)
    color_list.append(color)

#Light the LEDs
for i in range(len(color_list)):
    for j in range(pixels.count()): 
        k = (i+j)%len(color_list) #if we exceed the list, wrap around
        pixels.set_pixel(j, color_list[k])
    pixels.show()
    if wait > 0:
        time.sleep(wait)

pixels.clear()
time.sleep(2)
pixels_list = list(range(pixels.count()))
random.shuffle(pixels_list)

# Same as above, but the LEDS don't display sequential colors. The same colors display over the lights, but the lights are shuffled.
for i in range(len(color_list)):
    for j in pixels_list:
        k = (i+j)%len(color_list) #if we exceed the list, wrap around
        pixels.set_pixel(j, color_list[k])
    pixels.show()
    if wait > 0:
        time.sleep(wait)

pixels.clear()
time.sleep(2)
pixels_list = list(range(pixels.count()))
random.shuffle(pixels_list)
random.shuffle(color_list)

# Same as above, but both the color list and the LED order are shuffled.
for i in range(len(color_list)):
    for j in pixels_list:
        k = (i+j)%len(color_list) #if we exceed the list, wrap around
        pixels.set_pixel(j, color_list[k])
    pixels.show()
    if wait > 0:
        time.sleep(wait)

    
