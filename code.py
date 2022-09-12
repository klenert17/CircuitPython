# Kathryn Lenert
# Hello Circuit Python
# This code makes the light turn colors

import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2

print("Make it aqua!")

while True:
    dot.fill((255, 0, 255)) 