import turtle as t
import random as r

color = ["red", "orange", "yellow", "green", "blue", "purple"]


def start_position(the_turtle, x, y):
    the_turtle.penup()
    the_turtle.goto(x, y)
    
    
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win ?")
print(user_bet)




tim_01 = t.Turtle(shape="turtle")
tim_01.color("red")
tim_02 = t.Turtle(shape="turtle")
tim_02.color("orange")
tim_03 = t.Turtle(shape="turtle")
tim_03.color("yellow")
tim_04 = t.Turtle(shape="turtle")
tim_04.color("green")
tim_05 = t.Turtle(shape="turtle")
tim_05.color("blue")
tim_06 = t.Turtle(shape="turtle")
tim_06.color("purple")

turtle_list = [tim_01, tim_02, tim_03, tim_04, tim_05, tim_06]


set_y = 75

for tim in turtle_list:
    start_position(tim, -230, set_y)
    set_y -= 30 
    







     
    
    
    
    
    
    
    
    
screen.listen()
# screen.onkey() 
screen.exitonclick()



# Answer Craft
# It's  also possible to create the turtle with a for loop