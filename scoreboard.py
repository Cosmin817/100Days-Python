from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(x=-280, y=250)

    def write_score_on_screen(self, my_score):
        self.clear()
        self.write(arg=f"Level: {my_score}", move=False, align='left', font=FONT)

    def write_gameover_on_screen(self):
        self.goto(x=-50, y=0)
        self.write(arg=f"GAME OVER", move=False, align='left', font=FONT)


