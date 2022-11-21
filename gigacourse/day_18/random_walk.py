import turtle as t
import random as r

# color_list = ["cyan", "blue", "green", "red", "violet", "yellow", "black", "grey", "pink",
            #   "medium aquamarine", "CornflowerBlue", "DarkOrchid", "wheat", "IndianRed"]

t.colormode(255)

def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return red, green, blue

directions = [0, 270, 90, 180 ]
rw_turtle = t.Turtle()
rw_turtle.pensize(15)
rw_turtle.speed('fastest')
for _ in range(200):
    rw_turtle.color(random_color())
    rw_turtle.forward(30)
    rw_turtle.setheading(r.choice(directions))

