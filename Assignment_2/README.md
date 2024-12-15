## Introduction   

A halloween decoration. If someone holds the thombstone and start dancing, the thombstone will start glowing, and the dancing part of "Thriller" by Micheal Jackson will start playing.

## Implementation   

I taped the atom 3S onto a plastic thombstone. 
Conncet it to the comnputer through a usbc cable, and attach the LED strip
The motion data from the atom board, will decide play/pause of the video, and the brightness of the LED strip.

### Hardware

* atom S3
* LED Strip

### Firmware   

This snippet listens for "play" or "pause" commands received from the serial port and controls the playback of a video element on a web page. When the "play" command is received, it starts the video if it is paused, and when the "pause" command is received, it pauses the video if it is playing.

``` Python  
if command == "play" and video.paused:
    await video.play()
elif command == "pause" and not video.paused:
    video.pause()
```

### Software   

This project uses the Web Serial API to let a browser communicate with a serial device in real time, allowing it to control a video element with simple commands like "play" or "pause." The main parts of the code are read_serial(), which handles reading and processing data from the serial device, and toggle_connection(), which manages connecting and disconnecting the device.


### Project outcome  

https://github.com/user-attachments/assets/0f1f1ce3-ceed-49cb-97fd-77c9e495b33e


