"""Trippy-looking rainbow Mandelbrot set by Adam Watney"""

from PIL import Image, ImageDraw, ImageColor
from math import log

width = 875
height = 500
img = Image.new(mode='RGB', size=(width, height))       # ratio is 7:4
draw = ImageDraw.Draw(img)
pc_size = (560, 320)


iter = 100


def translate(number, oldmin, oldmax, newmin, newmax):
    number /= (oldmax - oldmin)
    number = number * (newmax - newmin) + newmin
    return number


def mandelbrot(c):
    z = 0
    n = 0

    while n < iter and abs(z) <= 2:
        z = z**2 + c
        n += 1

    if n == iter:
        global val
        val = 0
        return 0

    return n + 1 - log(log(abs(z))) / log(2)


for x in range(width):
    for y in range(height):
        a = translate(x, 0, width, -2.5, 1)
        b = translate(y, 0, height, -1, 1)
        val = 100
        c = complex(a, b)

        hue = int(mandelbrot(c) * 255)
        draw.point([x, y], ImageColor.getrgb("hsv({}, 100%, {}%)".format(hue, val)))

img.show()
