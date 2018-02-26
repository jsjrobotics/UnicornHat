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
    return 255

def displayMatrix(matrix):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            rgb = matrix[x][y]
            unicorn.set_pixel(x, y, rgb[0], rgb[1], rgb[2])
    unicorn.show()

display = emptyMatrix()
display[5][3] = (0,255,0)
displayMatrix(display)
time.sleep(2)
display = emptyMatrix()
displayMatrix(display)
time.sleep(2)
display[2][4] = (97,14,0)
displayMatrix(display)
time.sleep(2)

def playerCharacter(xPosition, yPosition, matrix):
    playerColor = playerColor()
    matrix[yPosition][xPosition] = playerColor
    matrix[yPosition+1][xPosition] = playerColor
    matrix[yPosition][xPosition+1] = playerColor

