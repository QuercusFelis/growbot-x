from picamera import PiCamera
from time import localtime,strftime

def photo():
    camera = PiCamera()
    camera.resolution = [1200,900]
    path = strftime('images/growbot-%m-%d-%Y_%H.jpg')
    camera.capture(path)
    return path
