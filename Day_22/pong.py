from ast import AsyncFunctionDef
from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, screen_height, paddle_width, paddle_height, start_x) -> None:
        super().__init__("paddle")
        self.screen_height = screen_height
        self.width = paddle_width
        self.height = paddle_height
        self.penup()
        self.color("white")
        self.setheading(270)
        self.speed(10)
        self.goto(start_x, screen_height/2)

    def move_up(self):
        if self.ycor() > self.height/2:
            self.forward(20)

    def move_down(self):
        if self.ycor() < self.screen_height - self.height/2:
            self.back(20)

    def detect_collision(self):
        pass


class Ball(Turtle):
    
    def __init__(self):
        super().__init__("ball")
        self.x_vel = 0
        self.y_vel = 0
        self.penup()
        self.color("white")
        self.speed(10)
    
    def set_position(self, x_pos, y_pos):
        """Sets the ball position"""
        self.hideturtle()
        self.goto(x_pos,y_pos)
        self.showturtle()

    def update_position(self):
        """Updates the position of the ball"""
        self.setx(self.xcor()+self.x_vel)
        self.sety(self.ycor()+self.y_vel)

    def set_velocity(self, x_vel, y_vel):
        """set the velocity of the ball"""
        self.x_vel = x_vel
        self.y_vel = y_vel

class Game:

    def __init__(self, screen_width, screen_height, ball_size, paddle_width) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball_size = ball_size
        self.paddle_width = paddle_width
        self.paddle_height = screen_height/12
        self.screen = Screen()
        self.setup_screen()

    def setup_screen(self):
        self.screen.setup(width=self.screen_width, height=self.screen_height)
        buffer = 5
        self.screen.setworldcoordinates(buffer, self.screen.window_height()+buffer, self.screen.window_width()+buffer, buffer)
        self.screen.bgcolor("black")

        self.screen.register_shape("paddle",
            ((self.paddle_width/2, self.paddle_height/2),
            (self.paddle_width/2, -self.paddle_height/2),
            (-self.paddle_width/2, -self.paddle_height/2),
            (-self.paddle_width/2, self.paddle_height/2)))

        self.screen.register_shape("ball",
            ((self.ball_size/2, self.ball_size/2),
            (self.ball_size/2, -self.ball_size/2),
            (-self.ball_size/2, -self.ball_size/2),
            (-self.ball_size/2, self.ball_size/2)))

        self.draw_background()

    def draw_background(self):
        cursor = Turtle("square")
        cursor.color("#bababa") # set color to a light grey 
        cursor.speed(9)
        cursor.hideturtle()
        cursor.pendown()
        cursor.pensize(5)
        
        cursor.goto(self.screen_width, 0)
        cursor.goto(self.screen_width, self.screen_height)
        cursor.goto(0, self.screen_height)
        cursor.goto(0, 0)

        cursor.goto(self.screen_width/2, 0)
        dash_size = 20
        cursor.setheading(90)
        cursor.penup()
        cursor.forward(self.screen_height/dash_size/2)
        for i in range(dash_size):
            if i % 2 == 1:
                cursor.penup()
            else:
                cursor.pendown()
            cursor.forward(self.screen_height/dash_size)

    def run_game(self):
        
        left_paddle = Paddle(self.screen_height, self.paddle_width, self.paddle_height, 30)
        right_paddle = Paddle(self.screen_height, self.paddle_width, self.paddle_height, self.screen_width-30)
        ball = Ball()

        ball.set_position(self.screen_width/2,self.screen_height/2)

        self.screen.listen()
        self.screen.onkeypress(left_paddle.move_up, "w")
        self.screen.onkeypress(left_paddle.move_down, "s")
        self.screen.onkeypress(right_paddle.move_up,"Up")
        self.screen.onkeypress(right_paddle.move_down,"Down")

        game_running = True
        ball.set_velocity(8, 3)

        while(game_running):
            ball.update_position()
            self.check_wall_collision(ball)
            self.check_paddle_collision(ball, left_paddle)
            self.check_paddle_collision(ball, right_paddle)

        self.screen.exitonclick()

    def check_wall_collision(self, ball: Ball):
        if ball.ycor() <= 0:
            ball.y_vel = -ball.y_vel
        if ball.ycor() >= self.screen_height:
            ball.y_vel = -ball.y_vel

    def check_paddle_collision(self, ball: Ball, paddle: Paddle):
        if (ball.ycor() < paddle.ycor() + paddle.height/2 
                and ball.ycor() > paddle.ycor() - paddle.height/2
                and ball.xcor() == paddle.xcor()):
            ball.x_vel = -ball.x_vel


def main():
    screen_width = 1000
    screen_height = 600
    paddle_width = 10
    ball_size = 10

    game = Game(screen_width, screen_height, ball_size, paddle_width)
    game.run_game()

if __name__ == "__main__":
    main()
