from pathlib import Path
from time import sleep

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

print("Starting program...")
with canvas(device) as draw:
    draw.rectangle((1, 1, 2, 2), 'whie')
    # draw.rounded_rectangle((20, 10, 40, 40), 7, 'white')
    # draw.rounded_rectangle((100, 10, ))
device.show()
while True:
    pass
print('Ending program.')
