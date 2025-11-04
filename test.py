from tkinter import *
from tkinter.colorchooser import askcolor
import routine_with_buttons as led

ROWS = 16
COLS = 16
PIXEL_WIDTH = 5
PIXEL_HEIGHT = 2

root = Tk()
root.title("Super Cool Program That Lets You Select LED Colors On a Grid 2025 Real")

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    return rgb + (0,)

buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_colors = [[None for _ in range(COLS)] for _ in range(ROWS)]

def change_bg(x, y):
    color = askcolor(title=f"Choose color for cell ({x},{y})")[1]
    if color:
        buttons[x][y].config(bg=color)
        color_rgb = hex_to_rgb(color)
        buttons_colors[x][y] = color_rgb

def submit():
    led.grid = buttons_colors
    for i in led.grid:
        print(i)
    led.draw_grid()


for x in range(ROWS):
    for y in range(COLS):
        button = Button(root,
                     width=PIXEL_WIDTH,
                     height=PIXEL_HEIGHT,
                     relief="raised",
                     bd=1,
                     bg="#F0F0F0")
        button.grid(column=y, row=x, padx=0, pady=0, sticky="nsew")
        button.config(command=lambda x=x, y=y: change_bg(x, y))
        buttons[x][y] = button
        buttons_colors[x][y] = (0, 0, 0, 0)

submit = Button(root, bg="#F0F0F0", text = "SUBMIT", command=submit)
submit.grid(column=COLS//2, row=ROWS+1)


for i in range(ROWS):
    root.grid_rowconfigure(i, weight=1)
for i in range(COLS):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()