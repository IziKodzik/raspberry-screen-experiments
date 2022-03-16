from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
print("Whooot")
w = 100
# while w > 0:
#     w = w - 1
with canvas(device) as draw:
    draw.ellipse((10, 10, 20, 20), fill='white', outline='white')
    draw.ellipse((10, 30, 20, 40), fill='white', outline='white')
    draw.ellipse((20, 10, 30, 20), fill='white', outline='white')
    draw.ellipse((20, 30, 30, 40), fill='white', outline='white')
    draw.rectangle((10, 15, 30, 35), fill='white', width=1)
    draw.rectangle((15, 10, 25, 13), fill='white', outline='white')
    draw.rectangle((15, 37, 25, 40), fill='white', outline='white')
    # draw.rectangle()
    # sleep(0.1)
while True:
    pass