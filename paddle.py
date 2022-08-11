from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        self.pos = pos
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.setposition(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.pos[0], new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.pos[0], new_y)












