from turtle import Turtle
ALIGNEMENT = "center"  
FONT = ("Arial", 50, "bold")   


class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font= FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font= FONT)
      
    def l_point(self):
        self.l_score += 1
        self.update_score()
        
    def r_point(self):
        self.r_score += 1
        self.update_score()
        
    def game_over(self):
        self.clear()
        self.write("💥GAME OVER💥", align=ALIGNEMENT, font=FONT)
        self.penup()
        self.goto(0, -100)
        self.write(f"Final score : {self.score}", align=ALIGNEMENT, font=FONT)

