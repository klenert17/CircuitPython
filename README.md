# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Distance Sensor](#Distance_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection

## CircuitPython_DistanceSensor

### Description & Code
For this assignment we were required to use the HC-SR04 sensor to measure the distance from an object, depending on the distance the LED would change colors going through the colors from red to green to blue. 

```
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
    if distance < 5: #Makes neopixel red when it senses something within 5 cm
        r = 225
        g = 0
        b = 0
        r = int(r)
        g = int(g)
        b = int(b)
        print(">5")
    elif distance > 5 and distance < 20: #Makes neopixel purple to blue when it senses something within 5 and 20 cm
        r = int(simpleio.map_range(distance, 5, 20, 225, 0))
        g = int(0)
        b = int(simpleio.map_range(distance, 5, 20, 0, 225))
        print("5-20")
    elif distance > 20 and distance < 35: #Makes neopixel blue to green when it senses something within 20 and 35 cm
        r = int(0)
        g = int(simpleio.map_range(distance, 20, 35, 0, 225))
        b = int(simpleio.map_range(distance, 20, 35, 225, 0))
        print("<20")
    elif distance > 35: #Makes neopixel green
        r = 0
        g = 225
        b = 0
        print("<35")


    dot.fill((r, g, b))
    time.sleep (0.05)
```

## Evidence
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/71406905/193126632-d0500b6e-6a94-46f8-b8e3-bedee702d727.gif)


### Wiring
![Screenshot (3)](https://user-images.githubusercontent.com/71406903/192614570-c0fe8ff7-9f1b-4d20-8237-f645cfd45fa3.png)
### Reflection



## CircuitPython_LCD

### Description & Code

```python
# Kathryn Lenert
# LCD Button Python
# This code counts the time the button is pressed and shows whether its up or down

import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D2)
btn2 = DigitalInOut(board.D7)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0

while True:
    while btn2.value == False:
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
                time.sleep(0.005)
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state = cur_state
    else:
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
                time.sleep(0.005)

            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2

```

### Evidence

![image](https://user-images.githubusercontent.com/71406905/193124068-461c3046-cc5f-407f-9ed7-d9241c10ed8f.png)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/71406905/193125561-e706b7ef-b1ee-4d80-be82-5ffd5c3c839d.gif)

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
