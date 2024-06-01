from turtle import Turtle, Screen


def main():
    screen_width = 1000
    screen_height = 600

    screen = Screen()
    screen.setup(width = screen_width, height = screen_height)
    screen.bgcolor("black")
    screen.exitonclick()


if __name__ == "__main__":
    main()
