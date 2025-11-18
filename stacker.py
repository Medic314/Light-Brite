from tkinter import *
import routine_with_buttons as led

root = Tk()
root.title("Together We Are Stacker")
root.geometry("730x522")
ROWS = 16
COLS = 16
STAGE = 16

grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

def rotate_and_mirror(grid):
    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] == None:
                grid [x][y] = (0, 0, 0, 0)
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

def upload():
    led.grid = rotate_and_mirror(grid)
    led.draw_grid()

def clear():
    for x in range(ROWS):
        for y in range(COLS):
            grid[x][y] = None
    upload()

moving = False
stop_request = False
lives = 5

def start_stacker(length=lives, speed=200, position=ROWS-1):
    global moving, stop_request, lives
    if moving:
        return
    moving = True
    stop_request = False
    pos = 0
    direction = 1

    def step():
        nonlocal pos, direction
        global moving, stop_request, lives
        if stop_request:
            lost = 0
            try:
                below_row = grid[position + 1]
            except Exception:
                below_row = None
            for i in range(length):
                idx = pos + i
                if 0 <= idx < COLS:
                    if below_row is None:
                        pass
                    else:
                        if below_row[idx] == (255, 0, 0, 0):
                            grid[position][idx] = (255, 0, 0, 0)
                        else:
                            if grid[position][idx] ==  (255, 0, 0, 0):
                                grid[position][idx] = None
                                lost += 1
            if lost:
                lives = max(0, lives - lost)

            upload()
            moving = False
            return
        for c in range(COLS):
            grid[position][c] = None
        for i in range(length):
            idx = pos + i
            if 0 <= idx < COLS:
                grid[position][idx] = (255, 0, 0, 0)
        upload()
        pos += direction
        if pos + length > COLS:
            pos = COLS - length
            direction = -1
        if pos < 0:
            pos = 0
            direction = 1
        root.after(speed, step)

    step()

def stacker_stage(event):
    global stop_request
    if event and getattr(event, "keysym", "").lower() == "space":
        stop_request = True

def play():
    global STAGE
    STAGE -= 1
    start_stacker(length=lives, speed=(STAGE*100)//3+10, position=STAGE)

start_width = 100
start_x = 730/2 - 50
start_y = 522/2 - 16 - 64
start_button = Button(root, bg="#F0F0F0", text="Start", command=play)
start_button.place(x=start_x, y=start_y, width=start_width, height=32)

stack_width = 100
stack_x = 730/2 - 50
stack_y = 522/2 - 16 
stack_button = Button(root, bg="#F0F0F0", text="Stack", command=play)
stack_button.place(x=stack_x, y=stack_y, width=stack_width, height=32)


root.bind("<Key>", stacker_stage)
root.mainloop()