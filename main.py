from turtle import Screen, mode
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("CCH Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

speed = 0.1 # [0.1, 0.09, 0.08 .... 0.03]


def increase_speed(fspeed=speed):
    if fspeed <= 0.03:
        pass
    else:
        fspeed -= 0.01
    return fspeed

ball = Ball()

continue_game = True

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key="Up")
screen.onkeypress(fun=right_paddle.move_down, key="Down")
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")

while continue_game:
    sleep(speed)
    ball.move()
    screen.update()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        speed = increase_speed(speed)

    # Left paddle scores
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.r_point()
        speed = 0.1

    # Right paddle scores
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.l_point()
        speed = 0.1

screen.exitonclick()


