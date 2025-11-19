from tkinter import *
import routine_with_buttons as led

root = Tk()
root.title("Together We Are Stacker")
root.geometry("730x522")
ROWS = 16
COLS = 16
STAGE = 16

grid = [[(0, 0, 0, 0) for _ in range(COLS)] for _ in range(ROWS)]
grid_print = [[None for _ in range(COLS)] for _ in range(ROWS)]

def upload():
    led.grid = grid
    led.draw_grid()
    for i in led.grid:
        print(i)
            
    

def clear():
    for x in range(ROWS):
        for y in range(COLS):
            grid[x][y] = (0, 0, 0, 0)
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
    true_pos = 0  
    direction = 1

    def draw_row(draw_pos, length):
        for c in range(COLS):
            grid[position][c] = (0, 0, 0, 0)
        for i in range(length):
            if 0 <= draw_pos + i < COLS:
                grid[position][draw_pos + i] = (255, 0, 0, 0)

    def step():
        nonlocal true_pos, direction
        global moving, stop_request, lives
        if stop_request:
            lost = 0
            below = grid[position + 1] if position + 1 < ROWS else None
            for i in range(length):
                idx = true_pos + i
                if below is None:
                    if 0 <= idx < COLS:
                        grid[position][idx] = (255, 0, 0, 0)
                    continue
                if 0 <= idx < COLS and below[idx] == (255, 0, 0, 0):
                    grid[position][idx] = (255, 0, 0, 0)
                else:
                    if 0 <= idx < COLS:
                        grid[position][idx] = (0, 0, 0, 0)
                    lost += 1
            if lost:
                lives = max(0, lives - lost)
            upload()
            moving = False
            root.after(300, next_stage)
            return
        true_pos += direction
        draw_pos = min(max(true_pos, 0), COLS - length)

        draw_row(draw_pos, length)
        upload()
    
        if true_pos + length >= COLS:
            direction = -1
        if true_pos <= 0:
            direction = 1

        root.after(speed, step)

    step()
def wait():
    pass

def special_screens(num):
    if num == 1:
        sgrid = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [255, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    return sgrid
def next_stage():
    global STAGE, lives, grid
    if lives <= 0:
        print("Game Over")
        return
    STAGE -= 1
    if STAGE < 0:
        print("YOU WIN!")
        root.after(500, wait)
        grid = special_screens(1)
        upload()
        return
    speed = ((STAGE + 1) * 100) // 3 + 10
    start_stacker(length=lives, speed=speed, position=STAGE)


def stacker_stage(event):
    global stop_request
    if event and getattr(event, "keysym", "").lower() == "space":
        stop_request = True

def play():
    global STAGE
    STAGE -= 1
    start_stacker(length=lives, speed=(STAGE * 100) // 3 + 10, position=STAGE)

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
