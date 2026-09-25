from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle()
r_paddle = Paddle()

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
    screen.update()




screen.exitonclick