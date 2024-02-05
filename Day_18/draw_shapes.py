from random import randint as random_int
from turtle import Turtle
from turtle import Screen

DEGREES = 360

jim = Turtle("turtle")
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")

for number_of_sides in range(3, 10):
    jim.left(45)
    jim.pencolor(random_int(1, 255), random_int(1, 255), random_int(1, 255))
    for _ in range(number_of_sides):
        jim.forward(100)
        jim.right(DEGREES/number_of_sides)

screen.exitonclick()
