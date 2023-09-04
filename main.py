import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

game_is_on = True
counter = 0

while game_is_on:
    counter += 1
    for car in cars:
        car.move_car()
        if car.xcor() < -350:
            del car
    if counter == 6:
        counter = 0
        cars.append(CarManager())
    time.sleep(0.1)
    screen.update()


