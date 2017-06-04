def simultaneous_hue_shift(wait) :
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
