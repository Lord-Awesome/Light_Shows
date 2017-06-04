def serialized_hue_shift(wait, speed):
    pixels.clear()
    pixels.show()
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
            k = (speed*(i+j))%len(color_list) #if we exceed the list, wrap around
            pixels.set_pixel(j, color_list[k])
        pixels.show()
        if wait > 0:
            time.sleep(wait)
