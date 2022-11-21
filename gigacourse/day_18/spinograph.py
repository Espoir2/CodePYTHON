from turtle import *
import random as r


colormode(255)

def random_color():
    red = r.randint(0, 255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return red, green, blue


tim = Turtle()
def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)
        tim.circle(100)
tim.speed("fastest")

draw_spirograph(2)





screen = Screen()
screen.exitonclick()


# screen = t.Screen()
# screen.exitonclick()