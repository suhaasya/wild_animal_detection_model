from gpiozero import AngularServo
from picamera import PiCamera
from time import sleep
import os

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
camera = PiCamera()

while (True):
    print(servo.angle)
    servo.angle = 0
    sleep(2)
    servo.angle = 90
    camera.start_preview()
    sleep(5)
    camera.capture('/home/suhas/Documents/image1.jpg')
    camera.stop_preview()
    os.system("python3 TFLite_detection_image.py --modeldir=wad --image=/home/suhas/Documents/image1.jpg")
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = -90
    sleep(2)
    servo.angle = 0
    sleep(2)
    

