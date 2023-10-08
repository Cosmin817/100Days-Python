from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
flag = "you_can_YES_change"


def change_random_french_word(green_button_pressed):
    global flag
    if flag == "you_can_YES_change":
        random_number = random.randint(0, len(words_data_list)-1)
        random_french_word = list(words_data_list[random_number].keys())[0]
        card_canvas.itemconfig(canvas_image, image=card_front_image)
        card_canvas.itemconfig(card_title, text="French", fill="black", font=('Ariel 15 italic'))
        card_canvas.itemconfig(card_word, text=random_french_word, fill="black")
        flag = "you_can_NOT_change"
        main_window.after(3000, change_card, random_number, random_french_word, green_button_pressed)
    else:
        pass


def change_card(random_number, random_french_word, green_button_pressed):
    global flag
    card_canvas.itemconfig(canvas_image, image=card_back_image)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    english_words_translation = list(words_data_list[random_number].values())[0]
    card_canvas.itemconfig(card_word, text=english_words_translation, fill="white")
    flag = "you_can_YES_change"
    print(green_button_pressed)
    if green_button_pressed is True:
        print(f"{random_french_word},{english_words_translation}")
        with open("./data/french_words.csv", 'r') as french_words:
            initial_lines = french_words.readlines()

        with open("./data/french_words.csv", 'w') as french_words_updated:
            for lines in initial_lines:
                if lines.strip("\n") != f"{random_french_word},{english_words_translation}":
                    french_words_updated.write(lines)

        with open('./data/known_words.csv', 'a') as known_word:
            known_word.write(f"{random_french_word},{english_words_translation}\n")
        words_data_list.pop(random_number)
        green_button_pressed = False


def green_pressed():
    global green_button_pressed
    green_button_pressed = True
    change_random_french_word(green_button_pressed)


def red_pressed():
    global green_button_pressed
    green_button_pressed = False
    change_random_french_word(green_button_pressed)


words_data_df = read_csv("./data/french_words.csv")
words_data_dict = words_data_df.set_index('French')['English'].to_dict()
words_data_list = [{k: v} for (k, v) in words_data_dict.items()]

initial_random_number = random.randint(0, len(words_data_list)-1)
initial_random_french_word = list(words_data_list[initial_random_number].keys())[0]

main_window = Tk()
main_window.config(width=850, height=600, pady=50, padx=50, bg=BACKGROUND_COLOR)
main_window.eval('tk::PlaceWindow . center')


# Images

wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

# Canvas

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=card_front_image)
card_title = card_canvas.create_text(400, 150, text="French", fill="black", font=('Ariel 15 italic'))
card_word = card_canvas.create_text(400, 256, text=initial_random_french_word, fill="black", font=('Ariel 40 bold'))
card_canvas.grid(row=0, column=0, columnspan=2)


# Buttons

wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=red_pressed)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, bd=0, command=green_pressed)
right_button.grid(row=1, column=1)

main_window.after(0, change_random_french_word, False)

main_window.mainloop()