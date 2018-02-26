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
display = [[noColor for x in range(width)] for y in range(height)] 

def displayMatrix(matrix):
    turtle.clear()
    for xIndex in range(0, len(matrix)):
        turtle.home()
        turtle.right(90)
        turtle.forward(10 * xIndex)
        turtle.left(90)
        for y in range(0, len(matrix[xIndex])):
            colorTuple = matrix[xIndex][y]
            if (colorTuple == noColor):
                turtle.pendown()
                turtle.circle(5)
                turtle.penup()
            else:
                turtle.color(colorTuple[0], colorTuple[1], colorTuple[2])
                turtle.begin_fill()
                turtle.circle(5)
                turtle.end_fill()
                turtle.color(0, 0, 0)
                

            turtle.forward(10)
    t.update()
    time.sleep(0.2)

display[5][3] = (0,255,0)
displayMatrix(display)
display[5][3] = noColor
displayMatrix(display)
