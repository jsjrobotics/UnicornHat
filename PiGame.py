#!/usr/bin/env python
import time
from random import randint

import unicornhat as unicorn
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()
noColor = (0,0,0)


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
    display[7][2] = player
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
    display[7][2] = player
    return display

displayMatrix(standingStill())
time.sleep(2)
displayMatrix(kick3())
time.sleep(0.5)
displayMatrix(standingStill())
