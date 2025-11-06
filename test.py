from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
import routine_with_buttons as led
import json

ROWS = 16
COLS = 16
PIXEL_WIDTH = 30
PIXEL_HEIGHT = 30

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

total_width_grid = (COLS * PIXEL_WIDTH)
total_width = total_width_grid + 200
total_height = (ROWS * PIXEL_HEIGHT + 10 + 32)
root.geometry(f"{total_width}x{total_height}")

for x in range(ROWS):
    for y in range(COLS):
        button = Button(root,
                        relief="raised",
                        bd=1,
                        bg="#F0F0F0")
        button.place(x=x * PIXEL_WIDTH, y=(y * PIXEL_HEIGHT), width=PIXEL_WIDTH, height=PIXEL_HEIGHT)
        button.config(command=lambda x=x, y=y: change_bg(x, y))
        buttons[x][y] = button
        buttons_colors[x][y] = (0, 0, 0, 0)



submit_width = 200
submit_x = max((total_width_grid - submit_width) // 2, 0)
submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
submit_button = Button(root, bg="#F0F0F0", text="SUBMIT", command=submit)
submit_button.place(x=submit_x, y=submit_y, width=submit_width, height=32)



def file_load_from_list(data):

    for i, row in enumerate(data):
        if i >= ROWS:
            break
        if not isinstance(row, (list, tuple)):
            continue
        for j, cell in enumerate(row):
            if j >= COLS:
                break
            if isinstance(cell, (list, tuple)):
                if len(cell) == 3:
                    r, g, b = int(cell[0]), int(cell[1]), int(cell[2])
                    a = 0
                elif len(cell) >= 4:
                    r, g, b, a = int(cell[0]), int(cell[1]), int(cell[2]), int(cell[3])
                else:
                    r = g = b = a = 0
            else:
                r = g = b = a = 0
            buttons_colors[i][j] = (r, g, b, a)
            if (r, g, b, a) == (0, 0, 0, 0):
                btn_color = "#F0F0F0"
            else:
                r_clip = max(0, min(255, r))
                g_clip = max(0, min(255, g))
                b_clip = max(0, min(255, b))
                btn_color = f'#{r_clip:02x}{g_clip:02x}{b_clip:02x}'
            try:
                buttons[i][j].config(bg=btn_color)
            except Exception:
                pass

def open_file():
    file_path = askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as f:
            data = json.load(f)
            file_load_from_list(data)

def save_file():
    file_path = asksaveasfilename(defaultextension=".json",
                                   filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as f:
            json.dump(buttons_colors, f)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)





root.mainloop()