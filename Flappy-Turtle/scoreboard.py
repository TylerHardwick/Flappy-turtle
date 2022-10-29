from turtle import Turtle

FONT = ("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("black")
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(x=-280, y=240)
        self.write(arg=f"Score:{self.score}    High Score:{self.high_score}",font=FONT ,align="left")

    def increase_score(self):
        self.score += 1
        self.display_score()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.display_score()


