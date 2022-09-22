# Kathryn Lenert
# Ultrasonic Sensor color changer
# This code makes the light turn colors based on distance

import board
import neopixel 
import time
import board
import adafruit_hcsr04
import simpleio

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
        r = int(simpleio.map_range(distance, 5, 20, 225, 0))
        g = int(0)
        b = int(simpleio.map_range(distance, 5, 20, 0, 225))
        print("5-20")
    elif distance > 20 and distance < 35:
        r = int(0)
        g = int(simpleio.map_range(distance, 20, 35, 0, 225))
        b = int(simpleio.map_range(distance, 20, 35, 225, 0))
        print("<20")
    elif distance > 35:
        r = 0
        g = 225
        b = 0
        print("<35")


    dot.fill((r, g, b))
    time.sleep (0.05)