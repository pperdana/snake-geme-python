from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake():
    def __init__(self):
        self.segments = []
        self.create_segments()

    def create_segments(self):
        for segment in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(START_POSITION[segment])
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_pos = self.segments[seg_num - 1].xcor()
            y_pos = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=x_pos, y=y_pos)
        self.segments[0].forward(20)