def random_light_display(wait):

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

    pixels.clear()
    time.sleep(2)
    pixels_list = list(range(pixels.count()))
    random.shuffle(color_list)

    for i in range(len(color_list)):
        random.shuffle(pixels_list)
        for j in pixels_list:
            k = random.randint(0, len(color_list) - 1)
            pixels.set_pixel(j, color_list[k])
        pixels.show()
        if wait > 0:
            time.sleep(wait)
