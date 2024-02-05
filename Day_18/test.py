"""Phase one is to draw a square"""

from turtle import Turtle
from turtle import Screen

rick = Turtle()
rick.shape("turtle")

for steps in range(10):
    for color in ('green', 'white'):
        rick.color(color)
        rick.forward(10)

rick.color('black')
for steps in range(5):
    rick.pendown()
    rick.forward(10)
    rick.penup()
    rick.forward(10)

screen = Screen()
screen.exitonclick()
