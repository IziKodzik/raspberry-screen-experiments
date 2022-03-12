from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.rectangle((10, 10, 30, 30), outline="white", fill="red")
    sleep(3)
    draw.rectangle((90, 10, 30, 30), outline="white", fill="red")

sleep(10)