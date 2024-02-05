"""Phase one is to draw a square"""

from turtle import Turtle
from turtle import Screen

rick = Turtle()
rick.shape("turtle")

for _ in range(4):
    rick.forward(100)
    rick.left(90)

screen = Screen()
screen.exitonclick()
