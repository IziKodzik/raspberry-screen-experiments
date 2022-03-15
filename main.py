from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
print("Whooot")
w = 100
while w > 0:
    w = w-1
    with canvas(device) as draw:
        draw.rectangle((30 + w, 30, 60 + w, 60), outline="white", fill="red")
    sleep(0.1)
sleep(10)