from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CCH_SPEED_VARIABLE = 0


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_speed = 5
        self.speed_increment = 0
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
        self.initial_speed = STARTING_MOVE_DISTANCE + CCH_SPEED_VARIABLE

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE + CCH_SPEED_VARIABLE)
        print(self.initial_speed)

    def check_safe_distance(self, user_turtle):
        distance_to_user = self.distance(user_turtle)
        if distance_to_user > 20:
            return True
        elif distance_to_user <= 20:
            return False

    def increase_car_speed(self):
        global CCH_SPEED_VARIABLE
        CCH_SPEED_VARIABLE += 10

