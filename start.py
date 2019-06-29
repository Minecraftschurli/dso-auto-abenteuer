from time import sleep

import cv2
import numpy
from PIL import ImageChops, ImageGrab  # $ pip install pillow
from pynput.mouse import Listener as MouseListener


def click(_id=''):
    global pos
    pos = None

    def set_xy(x, y, button, pressed):
        global pos
        pos = (x, y)
        mouse_listener.stop()
    mouse_listener = MouseListener(on_click=set_xy)
    mouse_listener.start()
    while mouse_listener.running:
        pass
    print(f'Pos{ _id }: { pos }')
    return pos


def setup():
    global notif_bbox
    notif_bbox = click('1') + click('2')


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
        sleep(1)

    print(f"bounding box of non-zero difference: {(bbox,)}")
    # superimpose the inverted image and the difference
    input("Press Enter to exit")
