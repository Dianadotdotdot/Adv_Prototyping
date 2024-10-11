## Assignment 1

### Introduction
This assignment is called "Friendship Circle," and the concept is a sock with magnet hands that will hold hand (attached to each other) at a distance, I want to amplify the hand holding by adding RGB light to it.


### Concept
![concept](https://github.com/user-attachments/assets/e2b95d2d-b283-410d-8b1d-2eb5dcb02f3f)


### State Diagram
![diagram](https://github.com/user-attachments/assets/3014d940-7c47-4be6-839c-2c2ab18056d1)


### Hardware
* ATOM S3 
* DIGITAL RGB LED

### Firmware   
[micropython_code](Assignment_1.py)

``` Python  
    if button.value() == 0 and not button_pressed:
        button_pressed = True  # Button press detected

    if button_pressed and program_state == STATE_STOPPED:
        # State 1: White color, hold for 5 seconds
        set_rgb_color(255, 255, 255)
        time.sleep(5)
        program_state = STATE_CYCLE_COLORS  # Switch to State 2

    elif program_state == STATE_CYCLE_COLORS:
        # State 2: Cycle through three colors
        cycle_colors()

    elif button.value() == 1 and program_state != STATE_STOPPED:
        # State 3: When the button is released, stop the RGB strip
        set_rgb_color(0, 0, 0)
        program_state = STATE_STOPPED
        button_pressed = False 
```

### Physical Components   
I used a pair of socks with eye-shaped stitches and a pair of hands with a magnet tucked inside.

### Project outcome  
![Final_Output](https://github.com/user-attachments/assets/f64791bb-8e3e-4c2f-b928-202c2a96e8be)

If the hands do not connect, everything is in a null state.
If the hands connect, the LED stripe placed in front will light up in white. 
After 5 seconds of connection, the LED stripe will flash light between pink, blue, and yellow.
If disconnected, the light will turn blue and pause, until it is reconnected.

[Video](https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Assignment/recording.mov)


