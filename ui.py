from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        score_board = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 10, 'normal'))
        score_board.grid(row=0, column=1)

        question_screen = Canvas(height=250, width=300)
        question_screen_text = question_screen.create_text(
                                                           150, 125,
                                                           text='TEST TEXT BY CCH',
                                                           fill='black',
                                                           font=('Arial', 20, 'italic')
                                                           )
        question_screen.grid(row=1, column=0, columnspan=2, pady = 20)

        green_button_image = PhotoImage(file="images/true.png")
        green_button = Button(image=green_button_image)
        green_button.grid(row=2, column=0)

        red_button_image = PhotoImage(file="images/false.png")
        red_button = Button(image=red_button_image)
        red_button.grid(row=2, column=1)

        self.window.mainloop()
