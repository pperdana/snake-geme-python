from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

start_pos = [(0,0), (-20,0), (-40,0)]

segments = []
for segment in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(start_pos[segment])
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()

    for seg_num in range(len(segments)-1, 0, -1):
        x_pos = segments[seg_num - 1].xcor()
        y_pos = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=x_pos, y=y_pos)


screen.exitonclick()