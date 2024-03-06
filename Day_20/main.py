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

class Snake():

    def __init__(self, step) -> None:
        self.snake = Turtle("mySquare")
        self.snake_array = []
        self.snake.penup()
        self.snake.color("green")
        self.snake_heading = 0
        self.step = step

    def create_snake(self):
        """Draw the initial snake of 3 pieces long
        """
        self.snake.speed(0)
        for _ in range(3):
            self.snake_array.append(self.snake.stamp())
            self.snake.forward(self.step)
        print(self.snake_array)

    def update_snake(self):
        """Move the snake forward, stamp at the new location, and 
        deletes the stamp at
        the oldest location in the array. 
        """
        self.snake_heading = self.snake.heading()
        self.snake.forward(self.step)
        self.snake_array.append(self.snake.stamp())
        self.snake.clearstamp(self.snake_array[0])
        self.snake_array.pop(0)
        for _ in range(10):     # delay the snake's speed
            self.snake.forward(0)

    def move_up(self):
        if self.snake_heading != 270:
            self.snake.setheading(90)

    def move_down(self):
        if self.snake_heading != 90:
            self.snake.setheading(270)

    def move_left(self):
        if self.snake_heading != 0:
            self.snake.setheading(180)

    def move_right(self):
        if self.snake_heading != 180:
            self.snake.setheading(0)

    snake_up = move_up
    snake_down = move_down
    snake_left = move_left
    snake_right = move_right


def main():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    STEP = 20

    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    # screen.setworldcoordinates(0, SCREEN_HEIGHT, SCREEN_WIDTH, 0)
    screen.register_shape("mySquare",
        ((STEP/2, STEP/2),
        (-STEP/2, STEP/2),
        (-STEP/2, -STEP/2),
        (STEP/2, -STEP/2)))

    snake = Snake(STEP)
    snake.create_snake()

    # screen.exitonclick()
    screen.onkeypress(fun = snake.snake_up, key = "Up")
    screen.onkeypress(fun = snake.snake_down, key = "Down")
    screen.onkeypress(fun = snake.snake_left, key = "Left")
    screen.onkeypress(fun = snake.snake_right, key = "Right")

    # Moving the snake
    screen.listen()
    while True:
        snake.update_snake()


if __name__ == "__main__":
    main()
