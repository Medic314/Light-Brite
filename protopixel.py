from tkinter import *

root = Tk()
root.title("ProtoPixel")
root.geometry("480x480")

def NeoPixel(PIN, NUM_PIXELS, brightness, auto_write, pixel_order):
    grid = []
    for x in range(16):
        grid.append([])
        for y in range(16):
            grid[x].append((0, 0, 0, 0))
    return grid

buttons = [[None for _ in range(16)] for _ in range(16)]
buttons_colors = [[None for _ in range(16)] for _ in range(16)]

for x in range(16):
    for y in range(16):
        button = Button(root,
                        relief="raised",
                        bd=1,
                        bg="#F0F0F0")
        button.place(x=x * 30, y=(y * 30), width=30, height=30)
        buttons[x][y] = button
        buttons_colors[x][y] = (0, 0, 0, 0)

root.mainloop()