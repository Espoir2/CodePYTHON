from turtle import *
from pprint import pprint

# pprint(dir())
# help(Turtle)
up()
goto(-500, 200)
down()


def turn_right():
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)


def game_01():
    forward(40)
    left(90)
    forward(50)
    turn_right()
    forward(30)
    turn_right()
    forward(40)  # Because when I turn_right() the last time I forward(10) in the same direction
    left(90)


for _ in range(0, 5):
    game_01()

exitonclick()
