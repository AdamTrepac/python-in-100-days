from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, screen_width, screen_height, start_x) -> None:
        super().__init__("paddle")
        self.penup()
        self.color("white")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.goto(start_x, screen_height/2)

    def move_up(self):
        self.heading(90)
        self.forward(10)

    def move_down(self):
        self.heading(270)
        self.forward(10)

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
    # screen.register_shape("paddle",
    #     ((paddle_width/2, paddle_height/2),
    #     (paddle_width/2, -paddle_height/2),
    #     (-paddle_width/2, -paddle_height/2),
    #     (-paddle_width/2, paddle_height/2)))

    screen.register_shape("paddle",
        ((paddle_height/2, paddle_width/2),
        (paddle_height/2, -paddle_width/2),
        (-paddle_height/2, -paddle_width/2),
        (-paddle_height/2, paddle_width/2)))


    draw_background(screen_width, screen_height)

    left_paddle = Paddle(screen_width, screen_height, 30)
    right_paddle = Paddle(screen_width, screen_height, screen_width-30)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
