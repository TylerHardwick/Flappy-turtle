from turtle import Turtle
import random

FLYSPEED = 35
FALLSPEED = 10


class Bird(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("brown")
        self.goto(x=-100, y=0)

    def fly(self):
        new_y = self.ycor() + FLYSPEED
        self.sety(new_y)

    def fall(self):
        new_y = self.ycor() - FALLSPEED
        self.sety(new_y)


