## Introduction   

The concept is an educational interactive board, presenting people "morie effect"
There are 3 pieces of transparent paper with patterns, together, they created this illusion. 
I was facinated by this illution so I decide to create a prototype around this topic.

https://github.com/user-attachments/assets/ac9267fb-2883-4a6c-b6a2-13954dbba439



## Implementation   

Here is the initial sketch:

![Sketch.jpeg
](https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Final/Design.png)

The 2 180 servo will be connected to the 2 angle unit, controlling the rotating degree.
The 360 servo will be connected to adafruit through wifi, and the rotation speed can be adjusted on a phone slider.


### Hardware

* AtomS3 Development Kit 
* ATOMIC PortABC Extension Base   
* Mini Angle Unit *2
* Servo Kit 180° *2
  
![Final/Hardware.jpeg
](https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Final/Hardware.jpeg)

### Firmware   

Full Code Here:
[https://github.com/Dianadotdotdot/Adv_Prototyping/blob/main/Final/Thonny%20Code]


1. Angle Unit Reading and Mapping
This reads the ADC values from the angle sensors and maps them to the specified angle range, rounding the results to one decimal place for smoother control.

``` Python  
def read_angle_unit(adc, start_angle, end_angle):
    adc_val = adc.read()  # Read raw ADC value (0–4095)
    print(f"Raw ADC Value: {adc_val}")  # Debugging
    angle = m5utils.remap(adc_val, 0, 4095, start_angle, end_angle)  # Map to the specified angle range
    rounded_angle = round(angle, 1)  # Round to one decimal place
    print(f"Mapped and Rounded Angle: {rounded_angle}°")
    return rounded_angle
```

2. MQTT Slider Callback for 360° Servo Control
This callback function processes slider input from the MQTT feed to control the speed and direction of the 360° servo. It maps the slider value to an appropriate PWM duty cycle range.

``` Python  
def slider_callback(topic, msg):
    global slider_value
    try:
        slider_value = int(msg.decode())
        print(f"Slider value: {slider_value}")
        if slider_value == 0:
            servo_360.duty(75)  # Stop the 360° servo (neutral position)
        else:
            # Map slider value (0-255) to servo PWM duty cycle (78-100 for speed control)
            servo_duty = int(m5utils.remap(slider_value, 0, 255, 78, 100))
            servo_360.duty(servo_duty)
    except ValueError:
        print("Invalid slider value received!")
```

### Software   

Adafruit feed connection through wifi:
I created a dashboard on Adafruit, adjusting the slider on the dashboard will send data to atom S3, which is ,capped to the 360 servo speed.
![CleanShot 2024-12-13 at 16 42 17@2x](https://github.com/user-attachments/assets/54432969-99a3-4643-992f-e686e463c7b4)


### Enclosure / Mechanical Design   
![Slide 16_9 - 6](https://github.com/user-attachments/assets/918887c4-bfd5-4fb3-9227-f5cc25109640)

## Project outcome  

Summarize the results of your final project implementation and include some photos of the prototype and a video walkthrough showing it working.  

Note that GitHub has a small size limit for uploading files via browswer (25Mb max), so you may choose to use a link to YouTube, Google Drive, or another external site.

## Conclusion  

As you wrap up the project, reflect on your experience of creating it.  Use this as an opportunity to mention any discoveries or challenges you came across along the way.  If there is anything you would have done differently, or have a chance to continue the project development given more time or resources, it’s a good way to conclude this section.

## Project references  

https://medium.com/art-marketing/practical-magic-the-moir%C3%A9-effect-3faecc04cd07
