from turtle import Turtle
ALIGNEMENT = "center"  
FONT = ("Arial", 50, "bold")   


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.write(self.score, align=ALIGNEMENT, font=FONT)

        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.clear()
        self.write("💥GAME OVER💥", align=ALIGNEMENT, font=FONT)
        self.penup()
        self.goto(0, -100)
        self.write(f"Final score : {self.score}", align=ALIGNEMENT, font=FONT)

