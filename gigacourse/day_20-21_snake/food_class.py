from turtle import Turtle, penup
import random
FOODSIZE = 1
FOODCOLOR = "red"


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=FOODSIZE, stretch_wid=FOODSIZE)
        self.color(FOODCOLOR)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)