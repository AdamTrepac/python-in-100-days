"""
Etch and sketch app that allows you to move forwards and backwards and rotate left or right.
You can also clear the screen
"""
from turtle import Turtle, Screen

STEP = 10

def move_forwards():
    linda.forward(STEP)

def move_backwards():
    linda.back(STEP)

def turn_left():
    linda.left(STEP)

def turn_right():
    linda.right(STEP)

def clear_screen():
    linda.reset()

linda = Turtle()
screen = Screen()

screen.onkeypress(fun = move_forwards, key = "w")
screen.onkeypress(fun = turn_left, key = "a")
screen.onkeypress(fun = move_backwards, key = "s")
screen.onkeypress(fun = turn_right, key = "d")
screen.onkeypress(fun = clear_screen, key = "c")
screen.listen()

screen.exitonclick()
