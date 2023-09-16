import turtle
import pandas as pd

FONT = ('Arial', 8, 'normal')


class StateOnMap(turtle.Turtle):
    def __init__(self, text, x, y):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.goto(x, y)
        self.write(text, align='center', move=False, font=FONT)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
right_guesses = 0
correct_guesses = []

screen.addshape(image)
turtle.shape(image)

data_frame = pd.read_csv("50_states.csv")

all_states = data_frame.state.to_list()

while right_guesses < 50:
    answer_state = str(
                       screen.textinput(title=f"{right_guesses}/50 States Correct",
                                        prompt="What's another state's name?"
                                        ).title()
                       )

    if answer_state == "Exit":
        for state in correct_guesses:
            all_states.remove(state)
        remaining_state_df = pd.DataFrame(all_states, columns=['state'])
        remaining_state_df.to_csv('states_to_learn.csv', ',')
        break

    get_answer = data_frame.where(data_frame["state"] == answer_state).dropna()
    state_name = str(get_answer.state.item())
    x_coord = int(get_answer.x.item())
    y_coord = int(get_answer.y.item())

    if (not get_answer.empty) and (state_name not in correct_guesses) and state_name != "Exit":
        right_guesses += 1
        correct_guesses.append(state_name)
        # print(correct_guesses)
        # print(state_name)
        # print(x_coord)
        # print(y_coord)
        StateOnMap(state_name, x_coord, y_coord)
    else:
        pass
