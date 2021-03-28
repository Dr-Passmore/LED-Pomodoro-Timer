import math
import utime
import picounicorn

picounicorn.init()

def pomocycle():

    # Set variables
    r = 255
    g = 69
    b = 0
    column = 15
    row = 6
    phase = "work"
    multiplier = 134

    # Start counting down
    while not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):

        # Illuminate every LED on the board
        for x in range(16):
            for y in range(7):
                picounicorn.set_pixel(x, y, r, g, b)
        
        # Extinguish LEDs one by one
        while row > -1:
            while column > -1:
                for x in range(multiplier):
                    if not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
                           utime.sleep(0.1)
                    else:
                        break
                picounicorn.set_pixel(column, row, 0, 0, 0)
                column -= 1
            column = 15
            row -= 1
        row = 6
        
        # No more LEDs? Switch from work to rest and vice versa
        if phase == "work":
            phase = "rest"
            multiplier = 27
            r = 0
            g = 255
            b = 0
        elif phase == "rest":
            phase = "work"
            multiplier = 134
            r = 255
            g = 69
            b = 0
        pass

    # Clear the display
    for x in range(16):
        for y in range(7):
            picounicorn.set_pixel(x, y, 0, 0, 0)

while True:
    while picounicorn.is_pressed(picounicorn.BUTTON_X):
        pomocycle()