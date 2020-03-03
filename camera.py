from picamera import Picamera
from time import sleep


def capture_image_to_file(file_path):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera requires sleep during warm up time
    sleep(2)
    camera.capture(file_path)


def capture_image_to_stream(stream):
    camera = Picamera()
    camera.start_preview()
    # Camera requires sleep during warm up time
    sleep(2)
    camera.capture(stream, 'jpeg')
