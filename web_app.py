from flask import Flask, send_file
# from camera import capture_image_to_file
# import os
from constants import *
import socket
app = Flask(__name__)


@app.route('/')
@app.route('/help')
def get_help():
    base_url = 'http://{}:{}'.format(socket.gethostname(), PORT)
    message = 'Send a GET request to any of the following routes to perform the described action:\n\n'
    message += '{}/help - to view this response again\n'.format(base_url)
    message += '{}/image - to capture an image with the Pi camera and download that image\n'.format(base_url)
    return message


@app.route('/image')
def get_image():
    # TODO - replace this with proper server code
    # if os.path.exists(SERVER_IMAGE_PATH):
    #     os.remove(SERVER_IMAGE_PATH)
    # capture_image_to_file(SERVER_IMAGE_PATH)
    return send_file(SERVER_IMAGE_PATH)
