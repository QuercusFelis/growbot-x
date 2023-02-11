from picamera import PiCamera
from time import localtime,strftime
import os

def photo():
    with PiCamera() as camera:
        camera.rotation = -90
        camera.resolution = [2592,1944]
        camera.awb_mode = 'off'
        camera.awb_gains = (0.70,0.55)
        camera.contrast = -7 
        camera.iso = 100
        camera.shutter_speed = 1400
        camera.image_denoise = False
 #       camera.sharpness = 65
 #       camera.exposure_mode = 'sports'
        path = os.path.join(os.path.dirname(__file__), strftime('images/growbot-%m-%d-%Y_%H_%M.jpg'))
        camera.capture(path)
        pass
    return path
