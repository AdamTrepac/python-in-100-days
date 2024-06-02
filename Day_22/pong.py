from turtle import Turtle, Screen


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
    screen.register_shape("my_square", ((0,0),(0,5),(5,5),(5,0)))

    draw_background(screen_width, screen_height)
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
