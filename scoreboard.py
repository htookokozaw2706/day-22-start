from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.write(self.r_score, align="center", font=("Courier", 10,"normal"))