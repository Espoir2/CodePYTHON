from turtle import *
from random import *
import turtle

turtle.colormode(255)

my_turtle = Turtle()
my_turtle.penup()
my_turtle.goto(300, 300)
my_turtle.pendown()
my_turtle.shape("turtle")
my_turtle.color("blue")

for _ in range(10):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue



def square(color, size):
    turtle_square = Turtle()
    turtle_square.shape("turtle")
    turtle_square.penup()
    turtle_square.goto(-500, 300)
    turtle_square.pendown()
    turtle_square.color(color)
    for _ in range(4):
        turtle_square.forward(size)
        turtle_square.right(90)


def polygon(size):
    # color_list = ["cyan", "blue", "green", "red", "violet", "yellow", "black", "grey", "pink", "medium aquamarine", "CornflowerBlue", "DarkOrchid", "wheat"]
    turtle_polygon = Turtle()
    turtle_polygon.penup()
    turtle_polygon.goto(0, 300)
    turtle_polygon.pendown()
    for i in range(3, 20):
        angle = 360/i
        turtle_polygon.color(random_color())
        for _ in range(i):
            turtle_polygon.forward(size)
            turtle_polygon.right(angle)    

square("cyan", 200)

polygon(50)








screen = Screen()
screen.exitonclick()
