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
    img_path = str(Path(__file__).resolve().parent.joinpath('images', 'eyes.png'))
    logo = Image.open(img_path).convert("RGBA")
    fff = Image.new(logo.mode, logo.size, (255,) * 4)

    background = Image.new("RGBA", device.size, "white")
    posn = ((device.width - logo.width) // 2, 0)
    device.display(background.convert(device.mode))

while True:
    pass