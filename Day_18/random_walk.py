"""
Have the turtle walk in random directions (random walk), with a random color for each direction change.
Simulation should be faster and line thinkness should be thicker
Can have an increment for minimum distance to make it feel like its moving on a grid
"""

from random import randint as randomint
from turtle import Screen, Turtle

STEPSIZE = 20
karen = Turtle("turtle")
karen.pensize(12)
karen.speed(10)
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

turn_options = [0, 90, 270]

for _ in range(100):
    karen.pencolor(randomint(1, 255), randomint(1, 255), randomint(1, 255))
    karen.forward(STEPSIZE)
    karen.left(turn_options[randomint(0,2)])

screen.exitonclick()
