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
from itertools import count
from turtle import Turtle, Screen, Vec2D
from random import randint

class Snake(Turtle):

    def __init__(self, step) -> None:
        super().__init__("mySquare")
        self.snake_array = []
        self.penup()
        self.color("green")
        self.snake_heading = 0
        self.speed(0)
        self.step = step

    def create_snake(self):
        """Draw the initial snake of 3 pieces long
        """
        for _ in range(9):
            self.forward(self.step)
            self.snake_array.append((self.stamp(), self.pos()))

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

    def eat_food(self):
        """Move the snake forward, stamp at the new location, and 
        deletes the stamp at
        the oldest location in the array. 
        """
        self.snake_heading = self.heading()
        self.forward(self.step)
        self.snake_array.append((self.stamp(), self.pos()))
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


class Food(Turtle):

    def __init__(self, step) -> None:
        super().__init__("mySquare")
        self.color("Red")
        self.penup()
        self.speed(0)
        self.stamp_ID = 0
        self.step = step

    def spawn_food(self, snake: Snake, width, height):
        self.clearstamp(self.stamp_ID)
        food_pos = Vec2D(randint(-width/2/self.step, width/2/self.step),
            randint(-height/2/self.step, height/2/self.step))
        food_pos *= self.step
        for snake_seg in snake.snake_array:
            if snake_seg[1] == food_pos:
                food_pos = self.spawn_food(snake, width, height)
        self.goto(food_pos)
        self.stamp_ID = self.stamp()
        return food_pos


class Score(Turtle):
    """Create a turtle object that displays and updates the users score
    """
    def __init__(self, screen_width, screen_height, step) -> None:
        super().__init__("square")
        self.penup()
        self.color("White")
        self.hideturtle()
        self.speed(0)
        self.goto(screen_width/2 - 10, screen_height/2 - step)
        self.score_count = -1

    def increment_score(self):
        self.clear()
        self.score_count += 1
        score_string = "Score: " + str(self.score_count)
        self.write(score_string, move = False, align="right", font=('Arial', 10, "bold"))

    def get_score(self):
        return self.score_count


def check_wall_collision(snake: Snake, screen_width, screen_height):
    if abs(snake.pos()[0]) > screen_width/2 or abs(snake.pos()[1]) > screen_height/2:
        return True
    return False

def check_food_collision(snake: Snake, food: Food, score: Score, screen_width, screen_height):
    if equal_vectors(snake.pos(), food.pos()):
        snake.eat_food()
        score.increment_score()
        food.spawn_food(snake, screen_width, screen_height)

def equal_vectors(vec1: Vec2D, vec2: Vec2D):
    if round(vec1[0]) == round(vec2[0]) and round(vec1[1]) == round(vec2[1]):
        return True
    return False


def main():
    screen_width = 600
    screen_height = 600
    step = 20
    game_running = True

    screen = Screen()
    screen.setup(screen_width, screen_height)
    screen.bgcolor("black")
    screen.register_shape("mySquare",
        ((step/2, step/2),
        (-step/2, step/2),
        (-step/2, -step/2),
        (step/2, -step/2)))

    snake = Snake(step)
    snake.create_snake()

    food = Food(step)
    food.color("Red")

    score = Score(screen_width, screen_height, step)
    score.increment_score()

    screen.onkeypress(fun = snake.snake_up, key = "Up")
    screen.onkeypress(fun = snake.snake_down, key = "Down")
    screen.onkeypress(fun = snake.snake_left, key = "Left")
    screen.onkeypress(fun = snake.snake_right, key = "Right")

    # Moving the snake
    screen.listen()
    food.spawn_food(snake, screen_width, screen_height)
    while game_running:
        snake.update_snake()
        print(snake.snake_array)
        check_food_collision(snake, food, score, screen_width, screen_height)
        if (snake.check_self_collision() is True
                or check_wall_collision(snake, screen_width, screen_height) is True):
            print("Game over! Your score was: ", score.get_score())
            game_running = False


if __name__ == "__main__":
    main()
