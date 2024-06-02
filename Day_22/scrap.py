from turtle import Turtle, Screen

screen = Screen()
buffer = 5
screen.setworldcoordinates(buffer, screen.window_height()+buffer, screen.window_width()+buffer, buffer)

turtle = Turtle('turtle')

turtle.goto(screen.window_width(), screen.window_height())
turtle.goto(0, screen.window_height())
turtle.goto(0, 0)
turtle.goto(screen.window_width(), 0)
turtle.goto(screen.window_width(), screen.window_height())
print(turtle.pos())


screen.exitonclick()