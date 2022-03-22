from pathlib import Path
from time import sleep

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

print("Starting program...")
with canvas(device) as draw:
    draw.rounded_rectangle((0, 0, 20, 20), 15, 'black')
while True:
    pass
print('Ending program.')
