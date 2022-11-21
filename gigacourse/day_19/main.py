import turtle as t
import random as r

tim = t.Turtle()

def move_foward():
    # global tim
    tim.forward(10)
    
    
screen = t.Screen()

screen.listen()
screen.onkey(key="space", fun=move_foward)
screen.exitonclick()
