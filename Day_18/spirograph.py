"""
Have the turtle generate circles at a point that are X degrees apart in a circle

Notes - radius is based on the turn angle and forward distance traveled
    they combine to produce some radius
"""

from random import randint as random_int
from turtle import Screen, Turtle

STEPSIZE = 5 # radius
DEGREES = 360
ANGLE = 4
SPIRO_ANGLE = 30

joan = Turtle("turtle")
joan.pensize(1)
joan.speed(0)
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

# The better way to do this is with the circle() function, but oh well
# joan.pencolor(random_int(1, 255), random_int(1, 255), random_int(1, 255))
# joan.circle(100)

for _ in range(int(DEGREES/SPIRO_ANGLE)):
    joan.left(SPIRO_ANGLE)
    joan.pencolor(random_int(1, 255), random_int(1, 255), random_int(1, 255))
    for _ in range(int(DEGREES/ANGLE)):
        joan.forward(STEPSIZE)
        joan.right(ANGLE)

screen.exitonclick()
