# CircuitPython
[this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Distance_Sensor](#Distance_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Motor_Control](#Motor_Control)
* [Temp sensor LCD screen](#Temp_sensor_LCD_screen)
* [Rotary Encoder](#Rotary_Encoder)
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



## Temp sensor LCD screen

### Description & Code
This assignment had us use a Tempature sensor, which senses the tempature around it, and show the tempature on the LCD screen in both celcius and fahrenheit.

```python
import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    lcd.clear()
    lcd.print("Temperature:\n{:.2f}C {:.2f}F".format(temp_C, temp_F)) # print to LCD with exactly 2 decimal points of precision
    time.sleep(1.0)
```

### Evidence

![temp](https://user-images.githubusercontent.com/71406905/225113744-10f176f0-819f-4b55-be77-3b80769f1354.jpg)

### Wiring

![Screenshot (18)](https://user-images.githubusercontent.com/71406905/225112516-c39c93a7-0966-4113-bf81-c19124852927.png)

### Reflection
This assignment was really hard because I haven't done code in quite some time. I also had to learn how to use the new tempature sensor and re-teach myself how to code an LCD screen. A big help for the code came from [River L's](https://github.com/rivques/CircuitPython/blob/master/tmp36.py) code. I did have to switch up which type of LCD screen I used and some of the wiring, but overall it works well.

## Rotary Encoder

### Description & Code

For this assignment I had to make a stop light that was controlled my a rotary encoder and display "go" "slow" and "stop" depending on the position of the rotary encoder. The LED lights were also indicating to "go" "slow" and "stop".

```python
import time
import rotaryio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull


encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)
last_position = 0
last_position = 0
btn = DigitalInOut(board.D4)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
state = 0
Buttonyep = 1


i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)


ledGreen = DigitalInOut(board.D8) #greenled is in pin 8
ledYellow = DigitalInOut(board.D9) #yellowled is in pin 9
ledRed = DigitalInOut(board.D10) #redled is in pin 10
ledGreen.direction = Direction.OUTPUT
ledYellow.direction = Direction.OUTPUT
ledRed.direction = Direction.OUTPUT


while True:
    position = encoder.position
    if position != last_position:
        if position > last_position:
            state = state + 1
        elif position < last_position:
            state = state - 1
        if state > 2: #the led will be red
            state = 2
        if state < 0: #the led will be green
            state = 0
        print(state)
        if state == 0: #if the led is green the lcd will print go
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Go")
            ledGreen.value = True
            ledRed.value = False
            ledYellow.value = False
        elif state == 1: #if the led is yellow the lcd will print caution
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Caution")
            ledYellow.value = True
            ledRed.value = False
            ledGreen.value = False
        elif state == 2:  #if the led is red the lcd will print stop
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Stop")
            ledRed.value = True
            ledGreen.value = False
            ledYellow.value = False
    if btn.value == 1:
        time.sleep(.1)
        Buttonyep = 1
    last_position = position

```

### Evidence

### Wiring

### Reflection
This assignment was pretty stright forward, with the main issue being that VS code was down. This was also my first time working with a rotary encoder but after a few google searches and help from [Nick](https://github.com/nbednar2929/CircuitPython) and [Joshua's](https://github.com/jbleakl36/CircuitPython) repositories, it wasn't too difficult.

## Photointerrupter

### Description & Code

For this assignment, we were assigned to count the amount of times a photointerrupted is interrupted during a four second window. The LCD will display the amount of times it was interrupted before resetting every 4 seconds.

```python

import board
import time
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

i2c = board.I2C()
btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.UP

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
buttonPress = -1
now = time.monotonic()  # Time in seconds since power on


while True: 
    if (now + 4) < time.monotonic():
        print ("times up " + str(now) + " " + str(buttonPress))
        now = time.monotonic()
        buttonPress = 0
    
    cur_state = btn.value
    if cur_state != prev_state:
        if not cur_state:
            buttonPress = buttonPress + 1
            lcd.clear()
            lcd.set_cursor_pos(0,0)
            lcd.print("The number of interrupts is: " + str(buttonPress))
    prev_state = cur_state
```

### Evidence

### Wiring

### Reflection

## Next Assignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
