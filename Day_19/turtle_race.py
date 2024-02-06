"""
A turtle RACE! Aka have like 6 turtles randomly move forwards every x time, and whoever
makes it to the end first will be the winner. Good luck.
"""
from turtle import Turtle, Screen
from random import randint

def race_finished(contestents: list[Turtle], screen_width):
    for contestent in contestents:
        if contestent.position()[0] >= screen_width/2 - 10:
            print(f"{contestent.color()[0]} won!")
            return True
    return False

def define_contestants(contestents: list[Turtle]):
    colors = ["red", "green", "orange", "pink", "violet", "brown"]
    for i in range(6):
        turtle = Turtle("turtle")
        turtle.color(colors[i])
        turtle.penup()
        contestents.append(turtle)

def line_up_contestants(contestents: list[Turtle], screen_width):
    STARTING_X_POS = 90
    for contestant in contestents:
        contestant.setposition(int(-screen_width/2), STARTING_X_POS)
        STARTING_X_POS -= 30

def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 400
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    racers: list[Turtle] = []
    define_contestants(racers)
    line_up_contestants(racers, SCREEN_WIDTH)

    while not race_finished(racers, SCREEN_WIDTH):
        for racer in racers:
            racer.forward(randint(1,10))

    screen.exitonclick()

if __name__ == "__main__":
    main()
