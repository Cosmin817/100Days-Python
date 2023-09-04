from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.init_car()

    def init_car(self):
        initial_x = 320
        initial_y = randint(-250, 250)
        self.color(COLORS[randint(0, len(COLORS) - 1)])
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.speed("fastest")
        self.setheading(180)
        self.goto(initial_x, initial_y)

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)
