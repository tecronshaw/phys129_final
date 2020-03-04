# Phys 129L Final Project

Herein lies the code for my Physics 129L final project.

## Web Server

The web server allows a user to capture an image and download it to a computer on the same network.

### Setup

See http://web.physics.ucsb.edu/~rpi/rpi_install.txt for setting up a Raspberry Pi properly.

Once that is done, login to your Pi and run the following commands in Terminal:

```text
$ cd ~
$ git clone https://github.com/tecronshaw/phys129_final.git
$ cd phys129_final
$ pip install -r requirements.txt
$ export FLASK_APP=web_app.py
$ python -m flask run
```

This will launch a web server on the Pi that allows you to make requests from a different machine.

## Client

The `client.py` script makes a GET request to the web server to capture and download an image. It then
performs an image analysis algorithm specified by the user as an argument and displays the result.

### Setup

On a different machine on the same network as the Pi (or just on the Pi for testing purposes),
open Terminal and run the following:

```text
$ cd ~
$ git clone https://github.com/tecronshaw/phys129_final.git   # skip if on same Pi
$ cd phys129_final
$ nano constants.py
```

Replace the hostname 'localhost' (underneath the comment that reads '# TODO - REPLACE THIS WITH THE PROPER HOSTNAME')
with the hostname of the Pi running the web application.
Press Ctl-X and y to exit and save.

Continue with the following commands:

```text
$ pip install -r requirements.txt
$ python client.py --help
```

This should display a help dialog that allows you to run the client.py script as desired.

As an example, in that same Terminal window run any of the following:

```text
$ python client.py sobel
$ python client.py blur
$ python client.py cluster
```

### Adding Algorithms

The `client.py` is written to allow easy addition of image analysis algorithms. To do so,
create a new file as `<name_of_algorithm>.py` (where `<name_of_alrgorithm>` is replaced with the
actual name) in the `analysis` directory. Create one
function called `run` that takes a 2D numpy array argument, `image_data`, and returns an
analyzed 2D numpy array to display. Save this file and run
`python client.py <name_of_algorithm>` (where `<name_of_algorithm>` is again replaced with
the same text you used in the filename). 
