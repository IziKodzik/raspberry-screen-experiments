from pathlib import Path
from time import sleep

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

print("Starting program...")
with canvas(device) as draw:
    # draw.rectangle((0, 0, 0, 0), 'white')
    draw.rounded_rectangle((19, 15, 39, 45), 7, 'white')
    draw.rounded_rectangle((84, 15, 104, 45), 7, 'white')
device.show()
while True:
    pass
print('Ending program.')
