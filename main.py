from pathlib import Path
from time import sleep

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

print("Whooot")
w = 100
step = 0
while step < 100:
    with canvas(device) as draw:
        draw.rectangle((0 + step, 0 + step/4, 20 + step, 20 + step/4), fill='blue', width=1)
    step += 20
    sleep(0.1)
sleep(5)
