# CircuitPython
[this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Distance_Sensor](#Distance_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Motor_Control](#Motor_Control)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
This code makes the Neopixel on the Metro Board change colors

```python
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

```


### Evidence

![IMG_9229](https://user-images.githubusercontent.com/71406905/197607446-4faf477a-6805-4b23-a978-288fef8ab14e.jpg)



### Wiring
There is no wireing for this assignment.

### Reflection
This was my very first time working with Python, and it was a pretty big shift. One of my biggest problems I found was realizing that indentation matters a whole lot. This took a little while for me to understant because all my lines of code were red until I realized. 



## CircuitPython_Servo

### Description & Code
This assignment was to control a 180 degree servo with two buttons, controling which direction it turns.

```python
# Kathryn Lenert
# Servo Turn Python
# This code makes a servo spin to the left and reset itself back

import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D8)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN 

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D10, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.

my_servo = servo.Servo(pwm, min_pulse=600, max_pulse=2700)

angle = 90 

while True:
   if btn1.value and angle <180:
      print("btn1 pressed")
      angle = angle +5 
      my_servo.angle = angle 
      time.sleep(0.01)
   elif btn2.value and angle >0:
      print("btn2 pressed")
      angle = angle -5 
      my_servo.angle = angle 
      time.sleep(0.01)
   else: 
      print("servo off")
      time.sleep(1)

```

### Evidence

![2 button servo](https://user-images.githubusercontent.com/71406905/193344424-dd582054-5bf3-43e8-9169-ccd71b0e2fc1.gif)

### Wiring

![image](https://user-images.githubusercontent.com/71406905/193343939-f1b3b85d-398a-4ec5-af53-071f534a4e62.png)
Image credit goes to [Dylan Halbert](https://github.com/dhalber11/CircuitPython)

### Reflection

This was my frsit ever assignment with coding parts with Python. Innitially, I added resistors to the breadboard but those aren't needed with this type of board. This assignment was mostly challanging because of the code, but otherwise it went smoothly.


## Distance_Sensor

### Description & Code
For this assignment we were required to use the HC-SR04 ultrasonic sensor to measure the distance from an object, depending on the distance, 5-35 cm, the LED would change colors going through the colors from red to green to blue. 

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
This assignment was pretty difficult because it was a combination of both previous codes with a lot of new things I had to learn and download. The hard part was getting the first distance and color written, but after with was just the same thing, just ajustments on the colors.


## CircuitPython_LCD

### Description & Code
This code makes a LCD screen display numbers going up or down by pushing a button depending on whether the switch is up or not.

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


![ezgif com-gif-maker](https://user-images.githubusercontent.com/71406905/193125561-e706b7ef-b1ee-4d80-be82-5ffd5c3c839d.gif)

### Wiring

![image](https://user-images.githubusercontent.com/71406905/193124068-461c3046-cc5f-407f-9ed7-d9241c10ed8f.png)

### Reflection

This assignment was relativly simple because it was a combination of pervious assignments, just a few extra lines of code for the second button. Initally, the second button didn't change the numbers at all, but that was due to the wiring being incorrect, so be sure to follow the immage exactly.


## Motor Control 
For this assignment we had to make a DC motor rotate at a speed that can increase and decreased based on the position of a potentiometer.

### Description & Code

```python
import time
from time import sleep
import board
import simpleio
from analogio import AnalogIn 
import pwmio  

analog_in = AnalogIn(board.A1) #potentionmeter pin
pin_out = pwmio.PWMOut(board.D9,duty_cycle=65535,frequency=5000)

while True:

  sensor_value = analog_in.value
  # Map the sensor's range from 0<=sensor_value<=255 to 0<=sensor_value<=1023
  mapped_value = int(simpleio.map_range(sensor_value, 0, 65535, 0, 255))
  
  pin_out.duty_cycle = sensor_value
  print("mapped sensor value: ", sensor_value)
  time.sleep(0.1)
```

### Evidence

![ezgif com-gif-maker](https://user-images.githubusercontent.com/71406905/199819183-076ce0da-a1c4-4b80-8caf-3c1f82da6628.gif)

### Wiring

![Screenshot (17)](https://user-images.githubusercontent.com/71406905/199815893-909e71f3-98e2-4080-8c45-a9048be0dce9.png)


### Reflection
This was the first time I had done this assinment in Circuit Python, as I had done it last year in arduino.cc. The wireing was the same as the other assignement, however the code was in a new format. All I had to do was switch the code into python using resources online, other python assignment, and class mates. 


## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
