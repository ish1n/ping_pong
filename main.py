import time
from turtle import Screen

from ball import Ball
from create_wall import Wall
from paddle import Paddle

from scoreboard import Score

screen = Screen()
screen.title("The_pong_game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
wall = Wall()

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

play_ball = Ball()
scoreboard = Score()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:

    time.sleep(0.1)
    screen.update()
    play_ball.movement()

    # collision with wall
    if play_ball.ycor() > 270 or play_ball.ycor() < -270:
        play_ball.bounce_y()

    # collision with paddle
    if play_ball.distance(r_paddle) < 50 and play_ball.xcor() > 350 or play_ball.distance(
            l_paddle) < 50 and play_ball.xcor() < -350:
        play_ball.bounce_x()

    if play_ball.xcor() > 380:
        play_ball.reset()
        scoreboard.l_point()

    if play_ball.xcor() < -380:
        play_ball.reset()
        scoreboard.r_point()

screen.exitonclick()
