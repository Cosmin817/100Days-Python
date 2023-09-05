import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
score = 1
cars = []
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")

game_is_on = True
counter = 0

scoreboard.write_score_on_screen(score)

while game_is_on:
    counter += 1
    for car in cars:
        car.move_car()
        if car.check_safe_distance(player) is False:
            scoreboard.write_gameover_on_screen()
            game_is_on = False
        if car.xcor() < -350:
            del car
    if counter == 6:
        counter = 0
        cars.append(CarManager())
    # player.check_reached_endpoint()
    if player.check_reached_endpoint() is True:
        for car in cars:
            car.increase_car_speed()
            break
        score += 1
        scoreboard.write_score_on_screen(score)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()