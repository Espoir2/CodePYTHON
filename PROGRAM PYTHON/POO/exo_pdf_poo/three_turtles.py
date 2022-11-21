#!/usr/bin/python3
# -*- coding: utf-8 -*-
import turtle


# Move the turtle at the  position x,y
def move(the_turtle, x, y):
    the_turtle.up()
    the_turtle.goto(x, y)
    the_turtle.down()


# Draw une figure
def draw(the_turtle):
    the_turtle.right(90)
    the_turtle.forward(100)
    the_turtle.left(90)
    the_turtle.forward(50)


turtle.setup(800, 600)  # Canvas size
wn = turtle.Screen()  # The window screen of Turtle
wn.bgcolor("lightblue")  # background color of the window
wn.title("Python Turtle")  # Set a title

angelo = turtle.Turtle()  # Object "Turtle"
angelo.shape("turtle")  # A turtle instead of a triangle
angelo.color("green")  # Green turtle
move(angelo, 50, 50)
draw(angelo)

donatello = turtle.Turtle()  # Object "Turtle"
donatello.shape("turtle")  # A turtle instead of a triangle
donatello.color("red")  # Green turtle
move(donatello, 100, 100)
draw(donatello)

raphael = turtle.Turtle()  # Object "Turtle"
raphael.shape("turtle")  # A turtle instead of a triangle
raphael.color("blue")  # Green turtle
move(raphael, 150, 150)
draw(raphael)
wn.exitonclick()  # Wait the click to exit
