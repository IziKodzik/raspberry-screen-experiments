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
    w = w - 1
    with canvas(device) as draw:
        draw.rectangle((0, 0, 30, 30), fill='white', outline='white', width=1)
        # draw.ellipse((0, 0, 30, 30), fill='white', outline='white')
    sleep(0.1)
sleep(10)
