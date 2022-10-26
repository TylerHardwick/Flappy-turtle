from turtle import Screen
import time
from bird import Bird
from scoreboard import Scoreboard
from pipes import PipeManager



screen = Screen()
screen.title("Tyler's Flappy Turtle")
screen.setup(width=600, height=600)
screen.bgcolor("sky blue")
screen.tracer(0)
scoreboard = Scoreboard()
bird = Bird()
pipe_manager = PipeManager()

screen.listen()
screen.onkey(bird.fly, "space")



play_game = True
while play_game:
    screen.update()
    time.sleep(0.1)
    pipe_manager.spawn_pipe()
    pipe_manager.move()

    #Detect collision with lower wall:
    if not bird.ycor() < -270:
        bird.fall()


    # Detect collision with pipe.
    for opening in pipe_manager.pipe_list_opening:
        if opening.xcor() < -80 and opening.xcor() > -90 and bird.distance(opening) > 40:
            play_game = False
            scoreboard.game_over()
        # Detect passing pipe
        elif bird.distance(opening) < 40:
            pipe_manager.pipe_list_opening.remove(opening)
            scoreboard.increase_score()
            pipe_manager.increase_speed()



screen.exitonclick()