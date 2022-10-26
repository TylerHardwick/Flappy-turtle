from turtle import Turtle

FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(x=-280,y=240)
        self.write(arg=f"Score:{self.score}",font=FONT ,align="left")

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over... GG", font=FONT, align="center")


