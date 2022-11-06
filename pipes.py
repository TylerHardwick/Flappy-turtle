from turtle import Turtle
import random

SPEED_INCREASE = 0.2
SPAWN_CHANCE = 20


class PipeManager:

    def __init__(self):
        self.pipe_list_lower = []
        self.pipe_list_upper = []
        self.pipe_list_opening = []
        self.pipe_speed = 5
        self.pipe_height = 50
        self.assemble_pipe()

    def create_pipe_lower(self, pipe_height):
        l_pipe = Turtle("square")
        l_pipe.penup()
        l_pipe.color("green")
        l_pipe.goto(x=380, y=-300)
        l_pipe.shapesize(stretch_wid=pipe_height,stretch_len=2)
        self.pipe_list_lower.append(l_pipe)

    def create_pipe_upper(self, pipe_height):
        u_pipe = Turtle("square")
        u_pipe.penup()
        u_pipe.color("green")
        u_pipe.goto(x=380, y=300)
        u_pipe.shapesize(stretch_wid=pipe_height, stretch_len=2)
        self.pipe_list_upper.append(u_pipe)

    def create_pipe_opening(self, yloc):
        pipe_opening = Turtle()
        pipe_opening.penup()
        pipe_opening.hideturtle()
        self.pipe_list_opening.append(pipe_opening)
        pipe_opening.goto(x=380, y=yloc)


    def assemble_pipe(self):
        upper_pipe_height = random.randint(10,47)
        lower_pipe_height = self.pipe_height - upper_pipe_height
        opening_yloc = 300 - (upper_pipe_height * 10) -50
        self.create_pipe_opening(opening_yloc)
        self.create_pipe_lower(lower_pipe_height)
        self.create_pipe_upper(upper_pipe_height)

    def move(self):
        for l_pipe in self.pipe_list_lower:
            new_loc = l_pipe.xcor() - self.pipe_speed
            l_pipe.setx(new_loc)

        for u_pipe in self.pipe_list_upper:
            new_loc = u_pipe.xcor() - self.pipe_speed
            u_pipe.setx(new_loc)

        for opening in self.pipe_list_opening:
            new_loc = opening.xcor() - self.pipe_speed
            opening.setx(new_loc)


    def spawn_pipe(self):
        spawn_chance = random.randint(1, SPAWN_CHANCE)
        if self.pipe_list_upper[-1].xcor() < 260 and spawn_chance == 1:
            self.assemble_pipe()
            
    def increase_speed(self):
        self.pipe_speed += SPEED_INCREASE

    def pipes_reset(self):
        for pipe in self.pipe_list_upper:
            pipe.goto(1000, 1000)
        for pipe in self.pipe_list_lower:
            pipe.goto(1000, 1000)
        for pipe in self.pipe_list_opening:
            pipe.goto(1000, 1000)
        self.pipe_list_upper.clear()
        self.pipe_list_lower.clear()
        self.pipe_list_opening.clear()
        self.assemble_pipe()


