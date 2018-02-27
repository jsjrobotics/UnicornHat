#!/usr/bin/env python
import time
from random import randint

import unicornhat as unicorn
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()
noColor = (0,0,0)
animationDelay=0.05

def emptyMatrix():
    return [[noColor for x in range(width)] for y in range(height)]
    
def randomColor():
    return randint(0, 255)

def playerColor():
    return (0, 255, 0)

def displayMatrix(matrix):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            rgb = matrix[x][y]
            unicorn.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
    unicorn.show()

def standingStill():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    return display



def kick1():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    return display

def kick2():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][1] = player
    return display

def kick3():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][1] = player
    display[5][1] = player
    return display

def kick4():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][1] = player
    display[5][1] = player
    display[5][2] = player
    return display

def kick4():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][2] = player
    display[5][1] = player
    display[5][2] = player
    display[7][1] = player
    return display

def kick5():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][2] = player
    display[5][1] = player
    display[5][2] = player
    display[7][2] = player
    return display

def kick6():
    display = emptyMatrix()
    player = playerColor()
    display[0][0] = player
    display[0][1] = player
    display[1][1] = player
    display[1][0] = player
    display[2][0] = player
    display[3][0] = player
    display[4][0] = player
    display[5][0] = player
    display[6][0] = player
    display[7][0] = player
    display[6][2] = player
    display[5][1] = player
    display[5][2] = player
    display[7][3] = player
    return display

while True:
    displayMatrix(standingStill())
    time.sleep(2)
    displayMatrix(kick1())
    time.sleep(animationDelay)
    displayMatrix(kick2())
    time.sleep(animationDelay)
    displayMatrix(kick3())
    time.sleep(animationDelay)
    displayMatrix(kick4())
    time.sleep(animationDelay)
    displayMatrix(kick5())
    time.sleep(animationDelay)
    displayMatrix(kick6())
    time.sleep(animationDelay)
    displayMatrix(kick5())
    time.sleep(animationDelay)
    displayMatrix(kick4())
    time.sleep(animationDelay)
    displayMatrix(kick3())
    time.sleep(animationDelay)
    displayMatrix(kick2())
    time.sleep(animationDelay)
    displayMatrix(kick1())
    time.sleep(animationDelay)
    displayMatrix(standingStill())
