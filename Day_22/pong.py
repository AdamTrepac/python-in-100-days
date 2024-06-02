from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, screen_width, screen_height, paddle_width, paddle_height, start_x) -> None:
        super().__init__("paddle")
        self.penup()
        self.color("white")
        self.setheading(270)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.speed(10)
        self.goto(start_x, screen_height/2)

    def move_up(self):
        if self.ycor() > self.paddle_height:
            self.forward(20)

    def move_down(self):
        if self.ycor() < self.screen_height - self.paddle_height:
            self.back(20)

    def detect_collision(self):
        pass


def draw_background(screen_width, screen_height):
    cursor = Turtle("square")
    cursor.color("#bababa") # set color to a light grey 
    cursor.speed(9)
    cursor.hideturtle()
    cursor.pendown()
    cursor.pensize(5)
    
    cursor.goto(screen_width, 0)
    cursor.goto(screen_width, screen_height)
    cursor.goto(0, screen_height)
    cursor.goto(0, 0)

    cursor.goto(screen_width/2, 0)
    dash_size = 20
    cursor.setheading(90)
    cursor.penup()
    cursor.forward(screen_height/dash_size/2)
    for i in range(dash_size):
        if i % 2 == 1:
            cursor.penup()
        else:
            cursor.pendown()
        cursor.forward(screen_height/dash_size)


def main():
    screen_width = 1000
    screen_height = 600

    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)
    buffer = 5
    screen.setworldcoordinates(buffer, screen.window_height()+buffer, screen.window_width()+buffer, buffer)
    screen.bgcolor("black")
    paddle_width = 10
    paddle_height = screen_height/12

    screen.register_shape("paddle",
        ((paddle_width/2, paddle_height/2),
        (paddle_width/2, -paddle_height/2),
        (-paddle_width/2, -paddle_height/2),
        (-paddle_width/2, paddle_height/2)))

    draw_background(screen_width, screen_height)

    left_paddle = Paddle(screen_width, screen_height, paddle_width, paddle_height, 30)
    right_paddle = Paddle(screen_width, screen_height, paddle_width, paddle_height, screen_width-30)

    screen.listen()
    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")
    screen.onkeypress(right_paddle.move_up,"Up")
    screen.onkeypress(right_paddle.move_down,"Down")
    screen.exitonclick()

if __name__ == "__main__":
    main()
