# import board
# import digitalio
import time
from adafruit_circuitplayground.express import cpx

# led = digitalio.DigitalInOut(board.D13)
# led.direction = digitalio.Direction.OUTPUT

while True:
    cpx.red_led = True
    # led.value = True
    time.sleep(0.5)
    cpx.red_led = False
    # led.value = False
    time.sleep(0.5)
    print(cpx.light)