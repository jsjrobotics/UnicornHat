import turtle as t
import time
wm = t.Screen()
wm.colormode(255)
turtle = t.Turtle()
turtle.home()
turtle.penup()
turtle.speed('fastest')
turtle.tracer(0,0)
turtle.hideturtle()
width = 8
height = 8
noColor = (-1,-1,-1)
animationDelay = 0.1

def playerColor():
    return (0, 255, 0)

def emptyMatrix():
    return [[noColor for x in range(width)] for y in range(height)]

def displayMatrix(matrix):
    turtle.clear()
    for xIndex in range(0, len(matrix)):
        turtle.home()
        turtle.right(90)
        turtle.forward(10 * xIndex)
        turtle.left(90)
        for y in range(0, len(matrix[xIndex])):
            rgb = matrix[xIndex][y]
            if (rgb == noColor):
                turtle.pendown()
                turtle.circle(5)
                turtle.penup()
            else:
                turtle.color(rgb[0], rgb[1], rgb[2])
                turtle.begin_fill()
                turtle.circle(5)
                turtle.end_fill()
                turtle.color(0, 0, 0)
                

            turtle.forward(10)
    t.update()


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
