# importing image object from PIL
import math


def main():
    from PIL import Image, ImageDraw

    w, h = 123, 63
    shape = [(0, 0), (w - 10, h - 10)]

    # creating new Image object
    img = Image.new("RGB", (w, h))

    # create rectangle image
    draw = ImageDraw.Draw(img)
    draw.rectangle((1, 1, 2, 2), 'white')
    # draw_rounded_rectangle(draw)
    img.show()


if __name__ == '__main__':
    main()
