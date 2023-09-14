from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 20
        self.goto(x_cor, y_cor)

    def go_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 20
        self.goto(x_cor, y_cor)
