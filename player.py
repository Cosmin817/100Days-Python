from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def check_reached_endpoint(self):
        y_cor = self.ycor()
        if y_cor == FINISH_LINE_Y:
            self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
            return True


