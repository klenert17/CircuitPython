# Kathryn Lenert
# Ultrasonic Sensor color changer
# This code makes the light turn colors

import board
import neopixel 
import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


while True:
    try: 
     print((sonar.distance,))
     distance = sonar.distance
    except RuntimeError:
        print("Retrying!")
    if distance < 5:
        r = 225
        g = 0
        b = 0
        r = int(r)
        g = int(g)
        b = int(b)
        print(">5")
    elif distance > 5 and distance < 20:
        r = 0
        g = 225
        b = 0
        r = int(r)
        g = int(g)
        b = int(b)
        print("5-20")
    elif distance > 20:
        r = 0
        g = 0
        b = 225
        r = int(r)
        g = int(g)
        b = int(b)
        print("<20")

    dot.fill((r, g, b))