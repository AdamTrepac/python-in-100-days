from turtle import Turtle, Screen


def main():
    screen_width = 1000
    screen_height = 600

    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)
    buffer = 5
    screen.setworldcoordinates(buffer, screen.window_height()+buffer, screen.window_width()+buffer, buffer)
    screen.bgcolor("black")
    screen.register_shape("my_square", ((0,0),(0,5),(5,5),(5,0)))
    
    cursor = Turtle("square")
    cursor.color("white")
    cursor.speed(9)
    cursor.hideturtle()
    cursor.pendown()
    cursor.pensize(5)
    
    cursor.goto(screen_width, 0)
    cursor.goto(screen_width, screen_height)
    cursor.goto(0, screen_height)
    cursor.goto(0, 0)

    screen.exitonclick()

if __name__ == "__main__":
    main()
