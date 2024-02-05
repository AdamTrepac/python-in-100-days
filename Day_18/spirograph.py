"""
Have the turtle generate circles at a point that are X degrees apart in a circle
"""

from random import randint as random_int
from turtle import Screen, Turtle

STEPSIZE = 20
DEGREES = 100

joan = Turtle("turtle")
joan.pensize(12)
joan.speed(0)
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

for number_of_sides in range(100):
    joan.left(45)
    joan.pencolor(random_int(1, 255), random_int(1, 255), random_int(1, 255))
    for _ in range(number_of_sides):
        joan.forward(10)
        joan.right(DEGREES/number_of_sides)

screen.exitonclick()