from pathlib import Path

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep
from PIL import Image


serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
print("Whooot")
w = 100
# while w > 0:
#     w = w - 1
with canvas(device) as draw:
    background = Image.new(device.mode, device.size, 'black')
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'eyes.png'))
    logo = Image.open(img_path).convert("RGBA")
    background.paste(logo,(0,0))
    while True:
        device.display(background)

