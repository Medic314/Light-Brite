import board
import neopixel
import time

# ------- CONFIG -------
PIN = board.A1
WIDTH = 16
HEIGHT = 16
NUM_PIXELS = WIDTH * HEIGHT
BRIGHTNESS = 0.08
PIXEL_ORDER = neopixel.GRBW   # change to GRB for RGB strips
BK = (0, 0, 0, 0)
BL = (0, 0, 255, 0)
RD = (189, 8, 8, 0)
SK = (217, 167, 57, 0)
HR = (126, 153, 83, 0)
PR = (52, 21, 57, 0)

grid = ()
pixels = neopixel.NeoPixel(
    PIN, NUM_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=PIXEL_ORDER
)


def xy_to_index(x, y):
    """Map (x,y) -> index for a zigzag-wired matrix, origin at top-left."""
    return y * WIDTH + (x if y % 2 == 1 else (WIDTH - 1 - x))


def set_px(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        pixels[xy_to_index(x, y)] = color


def clear(bg=BL):
    pixels.fill(bg)


def draw_grid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(i)
            print(j)
            set_px(j, i, grid[i][j])

    pixels.show()