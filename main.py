from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle()
r_paddle = Paddle()
ball = Ball()
score = Scoreboard()


l_paddle.goto(350,0)
r_paddle.goto(-350,0)
l_paddle.go_up()
l_paddle.go_down()

screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")

r_paddle.go_up()
r_paddle.go_down()

screen.listen()
screen.onkey(r_paddle.go_up,"w")
screen.onkey(r_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor()>388 : 
        ball.ball_reset()

    if ball.xcor() < -388:
        ball.ball_reset()




screen.exitonclick()