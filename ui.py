from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, padx=20)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="OK",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280,
        )
        check_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(
            file="images/false.png",
        )

        self.confirm_btn = Button(
            image=check_img, highlightthickness=0, command=self.validate
        )
        self.false_btn = Button(
            image=false_img, highlightthickness=0, command=self.reject
        )
        self.get_next_question()

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.confirm_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)
        self.score.grid(row=0, column=1)

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.confirm_btn.config(state="normal")
            self.false_btn.config(state="normal")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz finished with a score of {self.quiz.score}/10",
            )
            self.canvas.config(bg="white")
            self.confirm_btn.config(state="disabled")
            self.false_btn.config(state='disabled')
        self.score.config(text=f"Score: {self.quiz.score}")

    def validate(self):
        self.confirm_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right=is_right)

    def reject(self):
        self.confirm_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right=is_right)

    def change_color(self, color):
        self.canvas.config(bg=color)

    def give_feedback(self, is_right):
        if is_right:
            self.change_color("green")
        else:
            self.change_color("red")
        self.window.after(1000, self.get_next_question)
