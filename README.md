# -- LIGHT - BRITE ---
###  **Make sure to place the files in a position where it can access:**
- "Board" Class
- "Neopixel" Class
shouldnt need anything special to install like commands or anything but ya never know
# --- WARNINGS ---
The original file i used to base the board logic off of had ***"from adafruit_circuitplayground import cp"*** to use the boards natural input button(s), but since the program **I** have already **HAS** a button i removed it because mine is better!!! Hopefully this doesnt cause a problem,,, that would be a shame



From how i interpreted the code, it should work because it just replaces what was used for the mario LED board with a 2d list full of tuples which is like, pretty much what it orginally was

However, to do this you run the tkinter program and it just uses ***"Import"*** to pretty much run the entirety of the board logic



From personal testing, it stops immediately at the line ***"pixels[xy_to_index(x, y)] = color"*** with this being the error it sends back:
```
Exception in Tkinter callback
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.13_3.13.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 2074, in __call__
    return self.func(*args)
           ~~~~~~~~~^^^^^^^
  File "c:\Users\CMP_MaMazola\OneDrive - Erie County Technical School\Desktop\Python\Light Brite\test.py", line 32, in submit
    led.draw_grid()
    ~~~~~~~~~~~~~^^
  File "c:\Users\CMP_MaMazola\OneDrive - Erie County Technical School\Desktop\Python\Light Brite\routine_with_buttons.py", line 47, in draw_grid
    set_px(j, i, grid[i][j])
    ~~~~~~^^^^^^^^^^^^^^^^^^
  File "c:\Users\CMP_MaMazola\OneDrive - Erie County Technical School\Desktop\Python\Light Brite\routine_with_buttons.py", line 35, in set_px
    pixels[xy_to_index(x, y)] = color
    ~~~~~~^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object does not support item assignment
```

Im PRETTY sure this is just it not being able to set it to a pixel because, clearly, it doesnt exist because the placeholder file i have for board contains jack

Despite all of this im still only like 65% sure this will work at all so no promises!!!



I tried to save to a .txt file, but any solution i could find / come up with would be so comedically tedious and inefficient that i just asked ai... and it used json...
thats 2 for the count on my internal fight with AI use, my Mr. Hyde is showing GAH

Added conways flawlessly, im so cool im so awesome im so cool

Added animations, with a seperate saving schema for them. Using ai again however... BUT EVERYTHING that isnt JSON SAVING was made by MEE!!!