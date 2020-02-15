from picamera import PiCamera
from time import localtime,strftime

camera = PiCamera()

camera.resolution(1200,900)
camera.capture(strftime('images/growbot-%m-%d-%Y_%H.jpg'))
