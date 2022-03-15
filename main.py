from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# Box and text rendered in portrait mode
print("Whooot")
with canvas(device) as draw:
    for i in range(0, 60):
        draw.rectangle((30 + i, 30, 60 + i, 60), outline="white", fill="red")
        sleep(1)
        device.clear()
        device.cleanup()
sleep(10)