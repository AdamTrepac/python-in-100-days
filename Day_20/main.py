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

class Snake(Turtle):

    def __init__(self, step) -> None:
        super().__init__("mySquare")
        self.snake_array = []
        self.penup()
        self.color("green")
        self.snake_heading = 0
        self.step = step

    def create_snake(self):
        """Draw the initial snake of 3 pieces long
        """
        self.speed(0)
        for _ in range(5):
            self.forward(self.step)
            self.snake_array.append((self.stamp(), self.pos()))
        print(self.snake_array)

    def update_snake(self):
        """Move the snake forward, stamp at the new location, and 
        deletes the stamp at
        the oldest location in the array. 
        """
        self.snake_heading = self.heading()
        self.forward(self.step)
        self.snake_array.append((self.stamp(), self.pos()))
        self.clearstamp(self.snake_array[0][0])
        self.snake_array.pop(0)
        self.delay()

    def check_self_collision(self):
        snake_length = len(self.snake_array)
        for i in range(snake_length-1):
            if self.snake_array[i][1] == self.snake_array[snake_length-1][1]:
                return True
        return False

    def delay(self):
        for _ in range(10):     # delay the snake's speed
            self.forward(0)

    def move_up(self):
        if self.snake_heading != 270:
            self.setheading(90)

    def move_down(self):
        if self.snake_heading != 90:
            self.setheading(270)

    def move_left(self):
        if self.snake_heading != 0:
            self.setheading(180)

    def move_right(self):
        if self.snake_heading != 180:
            self.setheading(0)

    snake_up = move_up
    snake_down = move_down
    snake_left = move_left
    snake_right = move_right


def check_wall_collision(snake: Snake, screen_width, screen_height):
    # print(abs(snake.pos()))
    if abs(snake.pos()[0]) > screen_width/2 or abs(snake.pos()[1]) > screen_height/2:
        return True
    return False

def main():
    screen_width = 600
    screen_height = 600
    step = 20
    game_running = True

    screen = Screen()
    screen.setup(screen_width, screen_height)
    # screen.setworldcoordinates(0, SCREEN_HEIGHT, SCREEN_WIDTH, 0)
    screen.register_shape("mySquare",
        ((step/2, step/2),
        (-step/2, step/2),
        (-step/2, -step/2),
        (step/2, -step/2)))

    snake = Snake(step)
    snake.create_snake()

    # screen.exitonclick()
    screen.onkeypress(fun = snake.snake_up, key = "Up")
    screen.onkeypress(fun = snake.snake_down, key = "Down")
    screen.onkeypress(fun = snake.snake_left, key = "Left")
    screen.onkeypress(fun = snake.snake_right, key = "Right")

    # Moving the snake
    screen.listen()
    while game_running:
        snake.update_snake()
        if (snake.check_self_collision() is True
                or check_wall_collision(snake, screen_width, screen_height) is True):
            print("Collision!")
            game_running = False


if __name__ == "__main__":
    main()
