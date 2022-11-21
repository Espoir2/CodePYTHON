from turtle import *
from paddle_class import Paddle
from ball_class import Ball
from score_board import Score
from time import *


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "s")
screen.onkeypress(l_paddle.go_down, "w")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    ball.move()
    r_distance = ball.distance(r_paddle)
    l_distance = ball.distance(l_paddle)



    # Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        
        
    # Detect collision with right paddle
    if r_distance < 50 and ball.xcor() > 320 or l_distance < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
        
    # Detect collision with left paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        
        
    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()
        
        
screen.exitonclick()