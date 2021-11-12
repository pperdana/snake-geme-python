from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

start_pos = [(0,0), (-20,0), (-40,0)]
for segment in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(start_pos[segment])
    # x_pos += -20


screen.exitonclick()