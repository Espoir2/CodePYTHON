from turtle import Turtle
ALIGNEMENT = "center"  
FONT = ("Arial", 20, "bold")   

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\snake_game_improved\data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, -200)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} \t High Score : {self.high_score}", align=ALIGNEMENT, font=FONT)

        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        
        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("D:\Mes FORMATIONS\CODING\PYTHON\CodePYTHON\gigacourse\day_24\snake_game_improved\data.txt", mode="w") as data:
                   data.write(f"{self.high_score}")     
            self.score = 0
            self.update_score()
            
    # def game_over(self):
    #     self.clear()
    #     self.write("💥GAME OVER💥", align=ALIGNEMENT, font=FONT)
    #     self.penup()
    #     self.goto(0, -100)
    #     self.write(f"Final score : {self.score} \n \n High Score : {self.high_score}", align=ALIGNEMENT, font=FONT)
        
    #     self.reset()

