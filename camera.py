# Enable the Camera Interface:
    # Open the Raspberry Pi configuration tool by running the following command:
        # sudo raspi-config
    # Navigate to Interfacing Options --> Camera and select Enable.
    # Exit the configuration tool and reboot your Raspberry Pi by running:
        # sudo reboot
    # Test the Camera:
        # Open a terminal window and run the following command to test the camera:
            # raspistill -o test.jpg

# To use the Raspberry Pi Camera within a Python program, you'll need the picamera library:
    # sudo apt install python3-picamera

import picamera
import time

# Taking a Picture
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('my_picture.jpg')
    print("done")
    

# Recording a 10 seconds video:
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    print("done1")

    