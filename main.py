from turtle import Turtle, Screen
import random

painter = Turtle()
red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
purple = Turtle()

turtles = [red, orange, yellow, green, blue, purple]
turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()


def color():
    return random.random(), random.random(), random.random()


def setup():
    screen.bgcolor("black")
    painter.color("white")
    painter.pencolor("white")
    painter.penup()
    painter.right(180)
    painter.forward(200)
    painter.left(90)
    painter.pendown()
    painter.pensize(3)
    painter.forward(200)
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    painter.forward(200)
    painter.penup()
    painter.forward(250)
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    turtle_pos = 100
    color_picker = 0
    for turtle in turtles:
        turtle.penup()
        turtle.shape("turtle")
        turtle.color(turtle_color[color_picker])
        color_picker += 1
        turtle.left(180)
        turtle.forward(180)
        turtle.left(90)
        turtle.forward(turtle_pos)
        turtle.left(90)
        turtle_pos -= 50


def sprint():
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 180:
            return turtle.color()

    return "painter"


setup()

user_bet = screen.textinput(title="Make your bet", prompt="Which color of turtle will win?: ")

while True:
    winner = sprint()
    if winner != "painter":
        print(f"{winner[0]} just won the race!")
        break

if user_bet == winner[0]:
    print("You won!!")
else:
    print("You lost!")

screen.exitonclick()
