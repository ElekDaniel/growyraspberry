import time
import board
import busio
from adafruit_mlx90614 import MLX90614

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an instance of the MLX90614 sensor
sensor = MLX90614(i2c)

while True:
    # Read the ambient temperature
    ambient_temp = sensor.ambient_temperature
    # Read the object temperature
    object_temp = sensor.object_temperature

    print(f"Object Temperature: {object_temp:.2f} °C")

    time.sleep(2)