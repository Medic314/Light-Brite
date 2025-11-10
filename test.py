from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
import routine_with_buttons as led
import json

# ---------------------------------------------------------------------------------------------------

root = Tk()
root.title("Super Cool Program That Lets You Select LED Colors On a Grid 2025 Real")

ROWS = 16
COLS = 16
PIXEL_WIDTH = 30
PIXEL_HEIGHT = 30

colors = ["#000000", "#000000", "#000000", "#000000", "#000000", "#000000"]

buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_colors = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_polarity = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_other = [None for _ in range(9)]

# ---------------------------------------------------------------------------------------------------

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    return rgb + (0,)

def pick_color():
    color = askcolor(title=f"Choose color to paint")[1]
    colors.insert(0, color)
    buttons_other[3].config(bg=colors[0])
    for i in range(5):
        if not colors[i+1] == "#000000":
            buttons_other[i+4].config(bg=colors[i+1])
        else:
            buttons_other[i+4].config(bg="#F0F0F0")
    if len(colors) > 5:
        colors.pop()
    print(colors)

def reset_color():
    colors.insert(0, "#000000")
    buttons_other[3].config(bg="#F0F0F0")
    for i in range(5):
        if not colors[i+1] == "#000000":
            buttons_other[i+4].config(bg=colors[i+1])
        else:
            buttons_other[i+4].config(bg="#F0F0F0")
    if len(colors) > 5:
        colors.pop()
    print(colors)

def change_bg(x, y):
    if colors[0]:
        if not colors[0] == "#000000":
            buttons[x][y].config(bg=colors[0])
        else:
            buttons[x][y].config(bg="#F0F0F0")
        color_rgb = hex_to_rgb(colors[0])
        buttons_colors[x][y] = color_rgb

def set_color_from_history(history_number):
    colors.insert(0, colors[history_number+1])
    if not colors[0] == "#000000":
        buttons_other[3].config(bg=colors[0])
    else:
        buttons_other[3].config(bg="#F0F0F0")
    for i in range(5):
        if not colors[i+1] == "#000000":
            buttons_other[i+4].config(bg=colors[i+1])
        else:
            buttons_other[i+4].config(bg="#F0F0F0")
    if len(colors) > 5:
        colors.pop()
    print(colors)

def rotate_and_mirror(grid):
    def rotate90_ccw(g):
        rows = len(g)
        cols = max((len(r) for r in g), default=0)
        rotated = []
        for y in range(cols):
            new_row = []
            for x in range(rows):
                if len(g[x]) > (cols - 1 - y):
                    new_row.append(g[x][cols - 1 - y])
                else:
                    new_row.append((0, 0, 0, 0))
            rotated.append(new_row)
        return rotated

    rotated = grid
    for _ in range(3):  # rotate three times (3 * 90° CCW = 270° CCW / 90° CW)
        rotated = rotate90_ccw(rotated)

    # Mirror horizontally (flip each row left-to-right)
    mirrored = [row[::-1] for row in rotated]
    return mirrored


def submit():
    led.grid = rotate_and_mirror(buttons_colors)
    print(rotate_and_mirror(buttons_colors))
    for i in led.grid:
        print(i)
    led.draw_grid()

def clear():
    led.clear
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].config(bg="#F0F0F0")
            buttons_colors[x][y] = (0, 0, 0, 0)

# ---------------------------------------------------------------------------------------------------

total_width_grid = (COLS * PIXEL_WIDTH)
total_width = total_width_grid + 250
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

submit_width = 100
submit_x = max((total_width_grid - submit_width) // 4, 0)
submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
buttons_other[0] = Button(root, bg="#F0F0F0", text="SUBMIT", command=submit)
buttons_other[0].place(x=submit_x, y=submit_y, width=submit_width, height=32)

submit_width = 100
submit_x = max(((total_width_grid - submit_width) // 4)*3, 0)
submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
buttons_other[1] = Button(root, bg="#F0F0F0", text="RESET", command=clear)
buttons_other[1].place(x=submit_x, y=submit_y, width=submit_width, height=32)

colorpick_width = 100
colorpick_x = (total_width_grid + ((total_width - total_width_grid)/2)) - colorpick_width/2
colorpick_y = total_height / 7
buttons_other[2] = Button(root, bg="#F0F0F0", text="Pick Color", command=pick_color)
buttons_other[2].place(x=colorpick_x, y=colorpick_y, width=colorpick_width, height=32)

colorpick2_width = 32
colorpick2_x = ((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-32-32
colorpick2_y = total_height / 7
buttons_other[3] = Button(root, bg="#F0F0F0", command=reset_color)
buttons_other[3].place(x=colorpick2_x, y=colorpick2_y, width=colorpick2_width, height=32)
offset = 0

for i in range(5):
    button = Button(root,
                        relief="raised",
                        bd=1,
                        bg="#F0F0F0")
    button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=(total_height / 7)*1.75, width=32, height=32)
    button.config(command=lambda i=i: set_color_from_history(i))
    buttons_other[i+4] = button
    offset += 48    

# ---------------------------------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------------------------------

def flip_polarity(x,y):
    if buttons_polarity[x][y]:
        buttons[x][y].config(bg="#000000")
        color_rgb = hex_to_rgb("#000000")
        buttons_polarity[x][y] = False
    else:
        buttons[x][y].config(bg="#F0F0F0")
        color_rgb = hex_to_rgb("#F0F0F0")
        buttons_polarity[x][y] = True
    buttons_colors[x][y] = color_rgb

def conway_clear():
    led.clear
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].config(bg="#000000")
            buttons_colors[x][y] = (0, 0, 0, 0)


def update():
    for x in range(ROWS):
        for y in range(COLS):
            if buttons_polarity[x][y]:
                for i in range(8):
                    pass
                     

def load_conway():
    deload_light_brite()
    for x in range(ROWS):
        for y in range(COLS):
            button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#000000")
            button.place(x=x * PIXEL_WIDTH, y=(y * PIXEL_HEIGHT), width=PIXEL_WIDTH, height=PIXEL_HEIGHT)
            p = False
            button.config(command=lambda x=x, y=y: flip_polarity(x, y))
            buttons[x][y] = button
            buttons_polarity[x][y] = False

    submit_width = 100
    submit_x = max((total_width_grid - submit_width) // 4, 0)
    submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
    buttons_other[0] = Button(root, bg="#F0F0F0", text="UPDATE", command=update)
    buttons_other[0].place(x=submit_x, y=submit_y, width=submit_width, height=32)

    submit_width = 100
    submit_x = max(((total_width_grid - submit_width) // 4)*3, 0)
    submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
    buttons_other[1] = Button(root, bg="#F0F0F0", text="RESET", command=conway_clear)
    buttons_other[1].place(x=submit_x, y=submit_y, width=submit_width, height=32)
    


# ---------------------------------------------------------------------------------------------------

def deload_all_lights():
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].destroy()

def deload_light_brite():
    clear()
    deload_all_lights()
    for i in range(len(buttons_other)):
        buttons_other[i].destroy()
    for i in range(len(buttons_other)-4):
        buttons_other[i+4].destroy()

def load_light_brite():
    deload_all_lights()
    total_width_grid = (COLS * PIXEL_WIDTH)
    total_width = total_width_grid + 250
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

    submit_width = 100
    submit_x = max((total_width_grid - submit_width) // 4, 0)
    submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
    buttons_other[0] = Button(root, bg="#F0F0F0", text="SUBMIT", command=submit)
    buttons_other[0].place(x=submit_x, y=submit_y, width=submit_width, height=32)

    submit_width = 100
    submit_x = max(((total_width_grid - submit_width) // 4)*3, 0)
    submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
    buttons_other[1] = Button(root, bg="#F0F0F0", text="RESET", command=clear)
    buttons_other[1].place(x=submit_x, y=submit_y, width=submit_width, height=32)

    colorpick_width = 100
    colorpick_x = (total_width_grid + ((total_width - total_width_grid)/2)) - colorpick_width/2
    colorpick_y = total_height / 7
    buttons_other[2] = Button(root, bg="#F0F0F0", text="Pick Color", command=pick_color)
    buttons_other[2].place(x=colorpick_x, y=colorpick_y, width=colorpick_width, height=32)

    colorpick2_width = 32
    colorpick2_x = ((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-32-32
    colorpick2_y = total_height / 7
    buttons_other[3] = Button(root, bg="#F0F0F0", command=reset_color)
    buttons_other[3].place(x=colorpick2_x, y=colorpick2_y, width=colorpick2_width, height=32)
    offset = 0

    for i in range(5):
        button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#F0F0F0")
        button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=(total_height / 7)*1.75, width=32, height=32)
        button.config(command=lambda i=i: set_color_from_history(i))
        buttons_other[i+4] = button
        offset += 48    

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu2 = Menu(menu_bar, tearoff=0)

file_menu2.add_command(label="Light Brite", command=load_light_brite)
file_menu2.add_command(label="Conway", command=load_conway)
menu_bar.add_cascade(label="Modes", menu=file_menu2)

root.config(menu=menu_bar)

# ---------------------------------------------------------------------------------------------------





root.mainloop()