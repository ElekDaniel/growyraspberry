import time
import board
import adafruit_sht4x
import subprocess

# Create I2C bus
i2c = board.I2C()

# Create sensor object
sensor = adafruit_sht4x.SHT4x(i2c)

# Set the sensor to no heater mode
sensor.heater = False  # Disables the heater

print("SHT40 Sensor Test")
print("-----------------")

# Initialize a flag to track if a picture has already been taken
picture_taken = False

# Loop to continuously read data
while True:
    temperature, humidity = sensor.measurements
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Humidity: {humidity:.2f} %")

    # If temperature is greater than or equal to 26°C and no picture has been taken yet
    if temperature >= 26 and not picture_taken:
        print("Temperature is above 26°C. Checking the cause")
        
        # Run the camera_test.py script
        subprocess.run(["python3", "video.py"])

        # Set the flag to indicate that a picture has been taken
        picture_taken = True

    # Reset the flag if the temperature drops below 26°C
    if temperature < 26:
        picture_taken = False

    time.sleep(0.1)
