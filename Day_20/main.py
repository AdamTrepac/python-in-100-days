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

snake_heading = 0

def move_up(snake: Turtle):
    if snake_heading != 270:
        snake.setheading(90)

def move_down(snake: Turtle):
    if snake_heading != 90:
        snake.setheading(270)

def move_left(snake: Turtle):
    if snake_heading != 0:
        snake.setheading(180)

def move_right(snake: Turtle):
    if snake_heading != 180:
        snake.setheading(0)

STEP = 20

def main():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    # screen.setworldcoordinates(0, SCREEN_HEIGHT, SCREEN_WIDTH, 0)
    screen.register_shape("mySquare", ((STEP/2, STEP/2), (-STEP/2, STEP/2), (-STEP/2, -STEP/2), (STEP/2, -STEP/2)))
    
    # Draw the initial snake
    snake = Turtle("mySquare")
    snake_array = []
    snake.penup()
    snake.color("green")
    for _ in range(3):
        snake_array.append(snake.stamp())
        snake.forward(STEP)
    print(snake_array)
    # generate food
    food = Turtle("mySquare")
    food.penup()
    food.color("red")

    snake.speed(0)
    # screen.exitonclick()
    screen.onkeypress(fun = partial(move_up, snake), key = "Up")
    screen.onkeypress(fun = partial(move_down, snake), key = "Down")
    screen.onkeypress(fun = partial(move_left, snake), key = "Left")
    screen.onkeypress(fun = partial(move_right, snake), key = "Right")

    # Moving the snake
    screen.listen()
    while True:
        global snake_heading
        snake_heading = snake.heading()
        snake_array.append(snake.stamp())
        print(snake_array[0])
        snake.clearstamp(snake_array[0])
        snake_array.pop(0)
        snake.forward(STEP)
        for _ in range(10):     # delay the snake's speed
            snake.forward(0)
        # print(snake.position())

if __name__ == "__main__":
    main()
