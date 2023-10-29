from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 10, 'normal'))
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_screen_text = self.canvas.create_text(
                                                           150, 125,
                                                           width=280,
                                                           text='TEST TEXT BY CCH',
                                                           fill=THEME_COLOR,
                                                           font=('Arial', 20, 'italic')
                                                           )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        green_button_image = PhotoImage(file="images/true.png")
        self.green_button = Button(image=green_button_image, highlightthickness=0, command=self.green_button_pressed)
        self.green_button.grid(row=2, column=0)

        red_button_image = PhotoImage(file="images/false.png")
        self.red_button = Button(image=red_button_image, highlightthickness=0, command=self.red_button_pressed)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_screen_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_screen_text, text="You have reached the end of the quiz.")
            self.red_button.config(state="disabled")
            self.green_button.config(state="disabled")

    def green_button_pressed(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def red_button_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right is True:
            self.canvas.config(bg='green')
        if is_right is False:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)