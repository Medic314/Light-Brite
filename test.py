from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
import routine_with_buttons as led
import json
import time
import random

# ---------------------------------------------------------------------------------------------------

root = Tk()
root.title("Super Cool Program That Lets You Select LED Colors On a Grid 2025 Real Feat. John Conway")

ROWS = 16
COLS = 16
PIXEL_WIDTH = 30
PIXEL_HEIGHT = 30

colors = ["#000000", "#000000", "#000000", "#000000", "#000000", "#000000"]

buttons = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_colors = [[None for _ in range(COLS)] for _ in range(ROWS)]
buttons_other = [None for _ in range(30)]

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
        if check_var.get() == 1:
            submit()
            print("Auto")


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
    for _ in range(3):
        rotated = rotate90_ccw(rotated)


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


def base_colors(b):
    def color_set():
        buttons_other[3].config(bg=colors[0])
        for i in range(5):
            if not colors[i+1] == "#000000":
                buttons_other[i+4].config(bg=colors[i+1])
            else:
                buttons_other[i+4].config(bg="#F0F0F0")
        if len(colors) > 5:
            colors.pop()
    if b == 0:
        colors.insert(0, "#FF0000")
        color_set()
    if b == 1:
        colors.insert(0, "#FF5500")
        color_set()
    if b == 2:
        colors.insert(0, "#FFFF00")
        color_set()
    if b == 3:
        colors.insert(0, "#00FF55")
        color_set()
    if b == 4:
        colors.insert(0, "#005500")
        color_set()

    if b == 5:
        colors.insert(0, "#00FFFF")
        color_set()
    if b == 6:
        colors.insert(0, "#0000FF")
        color_set()
    if b == 7:
        colors.insert(0, "#AA00FF")
        color_set()
    if b == 8:
        colors.insert(0, "#FF00FF")
        color_set()
    if b == 9:
        colors.insert(0, "#FFFFFF")
        color_set()
    
        
        

# ---------------------------------------------------------------------------------------------------

total_width_grid = (COLS * PIXEL_WIDTH)
total_width = total_width_grid + 250
total_height = (ROWS * PIXEL_HEIGHT + 10 + 32)
root.geometry(f"{total_width}x{total_height}")
print(f"{total_width}x{total_height}")

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

check_var = IntVar()
buttons_other[19] = Checkbutton(root, text="Automatically Submit?", variable=check_var)
buttons_other[19].place(x=(total_width_grid + ((total_width - total_width_grid)/2.50)) - colorpick_width/2, y=colorpick_y+64+36)

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

offset = 0
for i in range(5):
    button = Button(root,
                        relief="raised",
                        bd=1,
                        bg="#F0F0F0")
    button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=((total_height / 7)*1.75)+80, width=32, height=32)
    button.config(command=lambda i=i: base_colors(i))
    buttons_other[i+9] = button
    offset += 48
offset = 0
for i in range(5):
    button = Button(root,
                        relief="raised",
                        bd=1,
                        bg="#F0F0F0")
    button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=((total_height / 7)*1.75)+80+48, width=32, height=32)
    button.config(command=lambda i=i: base_colors(i+5))
    buttons_other[i+14] = button
    offset += 48
buttons_other[9].config(bg="#FF0000")
buttons_other[10].config(bg="#FF5500")
buttons_other[11].config(bg="#FFFF00")
buttons_other[12].config(bg="#00FF55")
buttons_other[13].config(bg="#005500")
buttons_other[14].config(bg="#00FFFF")
buttons_other[15].config(bg="#0000FF")
buttons_other[16].config(bg="#AA00FF")
buttons_other[17].config(bg="#FF00FF")
buttons_other[18].config(bg="#FFFFFF")

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

# Animation load/save (open_file2 / save_file2)
def open_file2():
    file_path = askopenfilename(filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, 'r') as f:
        data = json.load(f)

    # support {"frames": [...]} or raw list of frames
    if isinstance(data, dict) and 'frames' in data:
        frames_data = data['frames']
    else:
        frames_data = data

    if not isinstance(frames_data, list):
        return

    new_frames = []
    for frame in frames_data:
        grid = empty_grid()
        if not isinstance(frame, (list, tuple)):
            new_frames.append(grid)
            continue
        for i, row in enumerate(frame):
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
                grid[i][j] = (r, g, b, a)
        new_frames.append(grid)

    if not new_frames:
        return

    global frame_grids, frames, current_frame
    frame_grids = new_frames
    frames = len(frame_grids)
    current_frame = 0

    # Switch UI into animation mode and load first frame
    try:
        load_animation()
    except Exception:
        pass
    try:
        load_grid_to_ui(frame_grids[current_frame])
    except Exception:
        pass

def save_file2():
    file_path = asksaveasfilename(defaultextension=".json",
                                   filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")])
    if not file_path:
        return

    global frame_grids, frames
    out_frames = []
    count = min(frames, len(frame_grids))
    for i in range(count):
        frame = frame_grids[i]
        frame_out = []
        for row in frame:
            row_out = []
            for cell in row:
                if isinstance(cell, (list, tuple)) and len(cell) >= 3:
                    r = int(cell[0]); g = int(cell[1]); b = int(cell[2])
                    a = int(cell[3]) if len(cell) >= 4 else 0
                    row_out.append([r, g, b, a])
                else:
                    row_out.append([0, 0, 0, 0])
            frame_out.append(row_out)
        out_frames.append(frame_out)

    with open(file_path, 'w') as f:
        json.dump(out_frames, f, indent=2)

# ---------------------------------------------------------------------------------------------------
buttons_polarity = [[False for _ in range(COLS)] for _ in range(ROWS)]
game_states = [None for _ in range(2)]

def flip_polarity(x,y):
    current = bool(buttons_polarity[x][y])
    if current:
        buttons[x][y].config(bg="#000000")
        color_rgb = hex_to_rgb("#000000")
        buttons_polarity[x][y] = False
    else:
        buttons[x][y].config(bg="#FFFFFF")
        color_rgb = hex_to_rgb("#FFFFFF")
        buttons_polarity[x][y] = True
    buttons_colors[x][y] = color_rgb

def conway_clear():
    try:
        led.clear()
    except Exception:
        pass
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].config(bg="#000000")
            buttons_colors[x][y] = (0, 0, 0, 0)
            buttons_polarity[x][y] = False


def update():
    next_state = [[False for _ in range(COLS)] for _ in range(ROWS)]
    for x in range(ROWS):
        for y in range(COLS):
            neighbors = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and buttons_polarity[nx][ny]:
                        neighbors += 1

            if buttons_polarity[x][y]:
                next_state[x][y] = (neighbors == 2 or neighbors == 3)
            else:
                next_state[x][y] = (neighbors == 3)

    for x in range(ROWS):
        for y in range(COLS):
            buttons_polarity[x][y] = bool(next_state[x][y])
            if buttons_polarity[x][y]:
                buttons[x][y].config(bg="#FFFFFF")
                buttons_colors[x][y] = hex_to_rgb("#FFFFFF")
            else:
                buttons[x][y].config(bg="#000000")
                buttons_colors[x][y] = hex_to_rgb("#000000")
    submit()

def play_conway():
    try:
        initial_delay_ms = int(buttons_other[4].get() * 100)
        if initial_delay_ms == 0:
            initial_delay_ms = 100
    except Exception:
        initial_delay_ms = 100
    game_states[0] = True

    def _step():
        if not game_states[0]:
            return
        update()
        try:
            next_delay = int(buttons_other[4].get() * 100)
            if next_delay == 0:
                next_delay = 100
        except Exception:
            next_delay = initial_delay_ms
        root.after(next_delay, _step)

    root.after(initial_delay_ms, _step)

def stop_conway():
    game_states[0] = False
    print(game_states[0])

def randomize():
    for x in range(ROWS):
        for y in range(COLS):
            alive = random.choice([True, False])
            buttons_polarity[x][y] = alive
            btn_color = "#FFFFFF" if alive else "#000000"
            try:
                buttons[x][y].config(bg=btn_color)
            except Exception:
                pass
            buttons_colors[x][y] = hex_to_rgb(btn_color)

def load_conway():
    buttons_polarity = [[False for _ in range(COLS)] for _ in range(ROWS)]
    game_states = [None for _ in range(2)]
    game_states[0] = False
    deload_light_brite()
    for x in range(ROWS):
        for y in range(COLS):
            button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#000000")
            button.place(x=x * PIXEL_WIDTH, y=(y * PIXEL_HEIGHT), width=PIXEL_WIDTH, height=PIXEL_HEIGHT)
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

    play_width = 200
    play_x = (total_width_grid + ((total_width - total_width_grid)/2)) - play_width/2
    play_y = total_height / 7
    buttons_other[2] = Button(root, bg="#F0F0F0", text="Start Simulation", command=play_conway)
    buttons_other[2].place(x=play_x, y=play_y, width=play_width, height=32)

    stop_width = 200
    stop_x = (total_width_grid + ((total_width - total_width_grid)/2)) - stop_width/2
    stop_y = (total_height / 7)+64
    buttons_other[3] = Button(root, bg="#F0F0F0", text="Stop Simulation", command=stop_conway)
    buttons_other[3].place(x=stop_x, y=stop_y, width=stop_width, height=32)

    random_width = 200
    random_x = (total_width_grid + ((total_width - total_width_grid)/2)) - random_width/2
    random_y = (total_height / 7)+64
    buttons_other[5] = Button(root, bg="#F0F0F0", text="Randomize", command=randomize)
    buttons_other[5].place(x=random_x, y=random_y+128, width=random_width, height=32)

    buttons_other[4] = Scale(root, from_=0, to=20, orient="horizontal",
                 label="Select a Value", tickinterval=5, length = (total_width - total_width_grid)-20)
    buttons_other[4].place(x=stop_x-20, y=stop_y+32)

# ---------------------------------------------------------------------------------------------------
frames = 3
current_frame = 0
animation_running = False

def empty_grid():
    return [[(0, 0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]

frame_grids = [empty_grid() for _ in range(frames)]

def ensure_frame_list():
    global frame_grids
    while len(frame_grids) < frames:
        frame_grids.append(empty_grid())

def copy_ui_to_grid():
    return [list(row)[:] for row in buttons_colors]

def load_grid_to_ui(grid):
    for x in range(ROWS):
        for y in range(COLS):
            try:
                cell = grid[x][y]
            except Exception:
                cell = (0, 0, 0, 0)
            if not isinstance(cell, (list, tuple)) or len(cell) < 3:
                r = g = b = a = 0
            else:
                r = int(cell[0]); g = int(cell[1]); b = int(cell[2])
                a = int(cell[3]) if len(cell) >= 4 else 0
            buttons_colors[x][y] = (r, g, b, a)
            if (r, g, b, a) == (0, 0, 0, 0):
                btn_color = "#F0F0F0"
            else:
                r_clip = max(0, min(255, r))
                g_clip = max(0, min(255, g))
                b_clip = max(0, min(255, b))
                btn_color = f'#{r_clip:02x}{g_clip:02x}{b_clip:02x}'
            try:
                buttons[x][y].config(bg=btn_color)
            except Exception:
                pass

def next_frame():
    global current_frame
    ensure_frame_list()
    frame_grids[current_frame] = copy_ui_to_grid()
    current_frame = (current_frame + 1) % frames
    ensure_frame_list()
    load_grid_to_ui(frame_grids[current_frame])
    try:
        buttons_other[25].config(text=f"Current Frame: {current_frame+1}")
    except Exception:
        pass

def previous_frame():
    global current_frame
    ensure_frame_list()
    frame_grids[current_frame] = copy_ui_to_grid()
    current_frame = (current_frame - 1) % frames
    ensure_frame_list()
    load_grid_to_ui(frame_grids[current_frame])
    try:
        buttons_other[25].config(text=f"Current Frame: {current_frame+1}")
    except Exception:
        pass

def raise_frames():
    global frames
    frames += 1
    frame_grids.append(empty_grid())
    try:
        buttons_other[24].config(text=f"{frames} Frames total")
    except Exception:
        pass

def lower_frames():
    global frames, current_frame, frame_grids
    if frames <= 1:
        return
    frames -= 1
    if len(frame_grids) > frames:
        frame_grids.pop()
    if current_frame >= frames:
        current_frame = frames - 1
        load_grid_to_ui(frame_grids[current_frame])
    try:
        buttons_other[24].config(text=f"{frames} Frames total")
        buttons_other[25].config(text=f"Current Frame: {current_frame+1}")
    except Exception:
        pass

def play_animation():
    global animation_running, current_frame
    ensure_frame_list()
    try:
        frame_grids[current_frame] = copy_ui_to_grid()
    except Exception:
        pass
    animation_running = True

    try:
        initial_delay_ms = int(buttons_other[27].get() * 100)
        if initial_delay_ms <= 0:
            initial_delay_ms = 100
    except Exception:
        initial_delay_ms = 100

    def _step():
        global current_frame, animation_running
        if not animation_running:
            return
        current_frame = (current_frame + 1) % frames
        ensure_frame_list()
        load_grid_to_ui(frame_grids[current_frame])
        try:
            buttons_other[25].config(text=f"Current Frame: {current_frame+1}")
        except Exception:
            pass
        submit()
        try:
            next_delay = int(buttons_other[27].get() * 100)
            if next_delay <= 0:
                next_delay = initial_delay_ms
        except Exception:
            next_delay = initial_delay_ms
        root.after(next_delay, _step)

    root.after(initial_delay_ms, _step)

def stop_animation():
    global animation_running
    animation_running = False

def load_animation():
    load_light_brite()
    try:
        buttons_other[19].destroy()
    except Exception:
        pass
    try:
        buttons_other[0].destroy()
    except Exception:
        pass
    ensure_frame_list()

    submit_width = 100
    submit_x = max((total_width_grid - submit_width) // 4, 0)-50
    submit_y = ROWS * PIXEL_HEIGHT + 10 // 2
    buttons_other[0] = Button(root, bg="#F0F0F0", text="Start Animation", command=play_animation)
    buttons_other[0].place(x=submit_x, y=submit_y, width=submit_width, height=32)

    buttons_other[26] = Button(root, bg="#F0F0F0", text="Stop Animation", command=stop_animation)
    buttons_other[26].place(x=submit_x+100, y=submit_y, width=submit_width, height=32)

    arrowL_width = 32
    arrowL_x = ((total_width_grid + ((total_width - total_width_grid)/2)) - arrowL_width)-32-32
    arrowL_y = total_height / 7
    buttons_other[20] = Button(root, bg="#F0F0F0", command=previous_frame, text="<")
    buttons_other[20].place(x=arrowL_x, y=arrowL_y+256, width=arrowL_width, height=32)

    arrowR_width = 32
    arrowR_x = ((total_width_grid + ((total_width - total_width_grid)/2)) - arrowR_width)+64+32
    arrowR_y = total_height / 7
    buttons_other[21] = Button(root, bg="#F0F0F0", command=next_frame, text=">")
    buttons_other[21].place(x=arrowR_x, y=arrowR_y+256, width=arrowR_width, height=32)

    arrowU_width = 32
    arrowU_x = ((total_width_grid + ((total_width - total_width_grid)/2)) - arrowL_width)-32-32
    arrowU_y = (total_height / 7)+256+64
    buttons_other[22] = Button(root, bg="#F0F0F0", command=raise_frames, text="+")
    buttons_other[22].place(x=arrowU_x, y=arrowU_y, width=arrowU_width, height=16)

    buttons_other[23] = Button(root, bg="#F0F0F0", command=lower_frames, text="-")
    buttons_other[23].place(x=arrowU_x, y=arrowU_y+16, width=arrowU_width, height=16)

    label_width = 100
    label_x = (total_width_grid + ((total_width - total_width_grid)/2)) - label_width/2
    buttons_other[24] = Label(root, text=f"{frames} Frames total")
    buttons_other[24].place(x=label_x, y=arrowU_y, width=label_width, height=32)

    buttons_other[25] = Label(root, text=f"Current Frame: {current_frame+1}")
    buttons_other[25].place(x=label_x, y=arrowU_y-64, width=label_width, height=32)

    buttons_other[27] = Scale(root, from_=0, to=20, orient="horizontal",
                 label="Frame Delay", tickinterval=5, length = (total_width - total_width_grid)-20)
    buttons_other[27].set(2)
    buttons_other[27].place(x=label_x-64, y=submit_y-42)


# ---------------------------------------------------------------------------------------------------

def deload_all_lights():
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].destroy()

def deload_light_brite():
    clear()
    deload_all_lights()
    for i in range(len(buttons_other)):
        try:
            buttons_other[i].destroy()
        except Exception:
            pass

def load_light_brite():
    deload_light_brite()
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

    check_var = IntVar()
    buttons_other[19] = Checkbutton(root, text="Automatically Submit?", variable=check_var)
    buttons_other[19].place(x=(total_width_grid + ((total_width - total_width_grid)/2.50)) - colorpick_width/2, y=colorpick_y+64+36)

    for i in range(5):
        button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#F0F0F0")
        button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=(total_height / 7)*1.75, width=32, height=32)
        button.config(command=lambda i=i: set_color_from_history(i))
        buttons_other[i+4] = button
        offset += 48

    offset = 0
    for i in range(5):
        button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#F0F0F0")
        button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=((total_height / 7)*1.75)+80, width=32, height=32)
        button.config(command=lambda i=i: base_colors(i))
        buttons_other[i+9] = button
        offset += 48
    offset = 0
    for i in range(5):
        button = Button(root,
                            relief="raised",
                            bd=1,
                            bg="#F0F0F0")
        button.place(x=(((total_width_grid + ((total_width - total_width_grid)/2)) - colorpick2_width)-64-16)+offset, y=((total_height / 7)*1.75)+80+48, width=32, height=32)
        button.config(command=lambda i=i: base_colors(i+5))
        buttons_other[i+14] = button
        offset += 48
    buttons_other[9].config(bg="#FF0000")
    buttons_other[10].config(bg="#FF5500")
    buttons_other[11].config(bg="#FFFF00")
    buttons_other[12].config(bg="#00FF55")
    buttons_other[13].config(bg="#005500")
    buttons_other[14].config(bg="#00FFFF")
    buttons_other[15].config(bg="#0000FF")
    buttons_other[16].config(bg="#AA00FF")
    buttons_other[17].config(bg="#FF00FF")
    buttons_other[18].config(bg="#FFFFFF")

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open Frame", command=open_file)
file_menu.add_command(label="Save Frame", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Open Animation", command=open_file2)
file_menu.add_command(label="Save Animation", command=save_file2)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu2 = Menu(menu_bar, tearoff=0)

file_menu2.add_command(label="Light Brite", command=load_light_brite)
file_menu2.add_command(label="Animation", command=load_animation)
file_menu2.add_command(label="Conway", command=load_conway)
menu_bar.add_cascade(label="Modes", menu=file_menu2)

root.config(menu=menu_bar)

# ---------------------------------------------------------------------------------------------------





root.mainloop()