import time
import picamera
import Adafruit_BMP.BMP085 as BMP085

VIDEO_DAYS = 1
FRAMES_PER_HOUR = 60
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
    with picamera.PiCamera() as cam:
        time.sleep(2)
        cam.capture('/root/Desktop/frame%03d.jpg' % frame)

# Capture the images
for frame in range(FRAMES):
    # Note the time before the capture
    start = time.time()
    capture_frame(frame)
    # Wait for the next capture. Note that we take into
    # account the length of time it took to capture the
    # image when calculating the delay
    # Capture data from the BMP085
    sensor = BMP085.BMP085()
    print('Temp = {0:0.2f} *F'.format(sensor.read_temperature() * 1.8 + 32))
    print('Pressure = {0:0.2f} psi'.format(sensor.read_pressure() * .000145038))
    print('Altitude = {0:0.2f} ft'.format(sensor.read_altitude() * 3.2808399))
    time.sleep(
        int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
    )
