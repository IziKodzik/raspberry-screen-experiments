from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
print("Whooot")
with canvas(device) as draw:
    draw.rectangle((30, 30, 60, 60), outline="white", fill="red")

sleep(10)