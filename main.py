import math
import utime
import urandom
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
            
def lunch():
    # Set variables
    r = 0
    g = 0
    b = 0
    column = 15
    row = 6
    while not(picounicorn.is_pressed(picounicorn.BUTTON_Y)):
    #Sets all pixels to off
        for x in range(16):
            for y in range(7):
                picounicorn.set_pixel(x, y, r, g, b)
        
        #Randomises the pixels filling up the LEDs and switching individual colours
        while True: 
           x = urandom.randint(0,15)
           y = urandom.randint(0,6)
           r = urandom.randint(0,255)
           g = urandom.randint(0,255)
           b = urandom.randint(0,255)
           picounicorn.set_pixel(x, y, r, g, b)
           #Switch off lunch mode
           if (picounicorn.is_pressed(picounicorn.BUTTON_Y)):
               break 
           #Frequency of loop. This creates a nice sparkle effect 
           utime.sleep(0.01)
        
        # Clear the display
        for x in range(16):
                for y in range(7):
                    picounicorn.set_pixel(x, y, 0, 0, 0)
                    
def clear():
    #Clears display - Added as I noticed at power on some LEDs previously on may remain on. This enables you to clear down the display without activating pomocycle or lunch processes
    for x in range(16):
                for y in range(7):
                    picounicorn.set_pixel(x, y, 0, 0, 0)
        

while True:
    while picounicorn.is_pressed(picounicorn.BUTTON_X):
        pomocycle()
    while picounicorn.is_pressed(picounicorn.BUTTON_A): 
        lunch()
    while picounicorn.is_pressed(picounicorn.BUTTON_Y):
        clear()