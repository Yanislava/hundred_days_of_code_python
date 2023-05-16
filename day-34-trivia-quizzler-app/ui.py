from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(350, 350)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text='Score: 0', fg='white', background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text='text',
            font=('Arial', 20, 'italic')
        )
        self.question_canvas.grid(column=0, columnspan=2, row=1, pady=50)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.question_canvas.configure(bg='green')
        else:
            self.question_canvas.configure(bg='red')

        self.window.after(1000, self.get_next_question)

