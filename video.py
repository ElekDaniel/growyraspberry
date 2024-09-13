from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera for video recording and set resolution
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)})  # Change this to your desired resolution
picam2.configure(video_config)

# Set up the encoder with a bit rate
encoder = H264Encoder(10000000)

# Specify the output file with Ffmpeg
video_output = FfmpegOutput("/home/pi/test_video.mp4")

# Start the camera
picam2.start()

# Start recording to the specified file
picam2.start_recording(encoder, output=video_output)

print("Recording video...")

# Record for 10 seconds
time.sleep(10)

# Stop recording and stop the camera
picam2.stop_recording()
picam2.stop()

print("Video saved successfully!")
