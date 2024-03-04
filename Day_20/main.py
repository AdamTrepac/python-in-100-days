"""
Snake game! There are 7 steps to the game:
1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect a collision with a wall
7. Detect a collision with the tail

"""
from turtle import Turtle, Screen
from functools import partial

def move_up(snake: Turtle):
    if snake.heading() != 270:
        snake.setheading(90)

def move_down(snake: Turtle):
    if snake.heading() != 90:
        snake.setheading(270)

def move_left(snake: Turtle):
    if snake.heading() != 0:
        snake.setheading(180)

def move_right(snake: Turtle):
    if snake.heading() != 180:
        snake.setheading(0)

STEP = 20

def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.register_shape("mySquare", ((0, 0), (0, STEP-1), (STEP-1, STEP-1), (STEP-1, 0)))

    # Draw the initial snake
    snake = Turtle("mySquare")
    snake_array = []
    snake.penup()
    snake.color("green")
    for _ in range(3):
        snake_array.append(snake.stamp())
        snake.forward(STEP)

    snake.speed(1)
    # screen.exitonclick()
    screen.onkeypress(fun = partial(move_up, snake), key = "Up")
    screen.onkeypress(fun = partial(move_down, snake), key = "Down")
    screen.onkeypress(fun = partial(move_left, snake), key = "Left")
    screen.onkeypress(fun = partial(move_right, snake), key = "Right")

    # Moving the snake
    while True:
        snake_array.append(snake.stamp())
        snake.forward(STEP)
        snake.clearstamp(snake_array[0])
        snake_array.pop(0)
        screen.listen()

if __name__ == "__main__":
    main()
