from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Start the camera
picam2.start()

# Wait for the camera to warm up
time.sleep(2)

# Capture an image and save it to the Desktop
picam2.capture_file("/home/pi/test_image.jpg")

# Print success message
print("Image saved successfully!")

# Stop the camera
picam2.stop()

