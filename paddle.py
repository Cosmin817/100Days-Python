from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.color("white")

    def move_up(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(x=current_x, y=current_y + 20)

    def move_down(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(x=current_x, y=current_y - 20)



