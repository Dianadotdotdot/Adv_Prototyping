## Assignment 1

### Introduction
This assignment is called "Friendship Circle," and the concept is a sock with magnet hands that will hold hand (attached to each other) at a distance, I want to amplify the hand holding by adding RGB light to it.


### Concept
![concept](https://github.com/user-attachments/assets/e2b95d2d-b283-410d-8b1d-2eb5dcb02f3f)


### State Diagram
[diagram.png](https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Assignment/diagram.png?raw=true)


### Hardware
* ATOM S3 
* BREADBRD
* DIGITAL RGB LED

### Firmware   
[micropython_code](Assignment_1.py)

``` Python  
  if input_pin.value():  # read digital input
    led_pin.off()        # turn off LED light
  else:
    led_pin.on()         # turn on LED light
```

### Physical Components   
I used a pair of socks with eye-shaped stitches and a pair of hands with a magnet tucked inside.

### Project outcome  
If the hands do not connect, everything is in a null state.
If the hands connect, the LED stripe placed in front will light up in white. 
After 5 seconds of connection, the LED stripe will flash light between pink, blue, and yellow.
If disconnected, the light will turn blue and pause, until it is reconnected.

[Video](https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Assignment/recording.mov)


