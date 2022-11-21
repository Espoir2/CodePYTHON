from time import sleep
from turtle import Screen

from regex import F
import snake_class as sn
import food_class as fc
import score_board as scb

BG_COLOR = "blue"

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BG_COLOR)
screen.title("Snake_game")
screen.tracer(0)
  
snakee = sn.Snake()
foodee = fc.Food()
scoree = scb.Score()
# screen.update()

screen.listen()
screen.onkey(snakee.up, "Up")
screen.onkey(snakee.down, "Down")
screen.onkey(snakee.left, "Left")
screen.onkey(snakee.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.15)
    snakee.move()
    
    # Detect collision with food
    if snakee.head.distance(foodee) < 15:
        foodee.refresh()
        scoree.increase_score()
        snakee.extend()


    # Detect collision with wall
    if snakee.head.xcor() > 300 or snakee.head.xcor() < -300 or snakee.head.ycor() > 300 or snakee.head.ycor() < -300:
        game_is_on = False
        scoree.game_over()

    # Detect collision with tail
    for segment in snakee.segments[1:]:
        if snakee.head.distance(segment) < 10:
            game_is_on = False
            scoree.game_over()































screen.exitonclick()
# TODO : 
# 1️⃣ Make the snake body
# 2️⃣ Make snake move
# 3️⃣ Control the snake
# 4️⃣ Detect collision with food
# 5️⃣ Create a scoreboard
# 6️⃣ Detect collision with wall
# 7️⃣ Detect collision with tail
# 🔴 Help the user to win (Avoid tail and wall)