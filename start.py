import cv2
import numpy
from PIL import ImageChops, ImageGrab  # $ pip install pillow


def setup():
    global notif_bbox
    notif_bbox = click() + click()


if __name__ == '__main__':
    setup()
    last = ImageGrab.grab().crop(notif_bbox)
    while True:
        im = ImageGrab.grab()
        new = im.crop(notif_bbox)
        diff = ImageChops.difference(new, last)
        bbox = diff.getbbox()
        if bbox is not None:  # exact comparison
            break

    print(f"bounding box of non-zero difference: {(bbox,)}")
    # superimpose the inverted image and the difference
    input("Press Enter to exit")
