"""
Practice with event listeners in turtle library
"""
from turtle import Turtle, Screen

def move_forward():
    shane.forward(10)

def turn_left():
    shane.left(90)

def turn_right():
    shane.right(90)



shane = Turtle("turtle")
screen = Screen()

screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.listen()


screen.exitonclick()
