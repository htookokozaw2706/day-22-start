from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

tim = Turtle()

tim.shape("square")
tim.color("white")
tim.shapesize(stretch_wid=5,stretch_len=1)
tim.penup()
tim.speed(0.1)
tim.goto(x=350, y=0)

def go_up():
    new_y = tim.ycor() + 20
    tim.goto(tim.xcor(), new_y)

def go_down():
    new_y = tim.ycor() - 20
    tim.goto(tim.xcor(), new_y)


screen.listen()
screen.onkey(go_up(), "Up")
screen.onkey(go_down(), "Down")




screen.exitonclick