from tkinter import *
from quiz_brain import QuizBrain
import time

FONT = ("Arial",20,"italic")
THEME_COLOR = "#375362"
class QuizeInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")
        self.score_label = Label(text=f"score: {self.score}", foreground="white", bg=THEME_COLOR, font=FONT)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Question", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_icon = PhotoImage(file="images/true.png", width=100,height=97)
        false_icon = PhotoImage(file="images/false.png", width=100,height=97)

        self.true_button = Button(image=true_icon, highlightthickness=0, command=self.user_chose_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_icon, highlightthickness=0, command=self.user_chose_false)
        self.false_button.grid(row=2, column=1)


        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've finished the quize")
            self.canvas.config(bg="orange")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def user_chose_true(self):
        if self.quiz.check_answer("true"):
            self.canvas.config(bg="green")
            self.score +=1
            self.score_label.config(text=f"score: {self.score}")
            self.canvas.config(bg="green")
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000,self.get_next_question)
    def user_chose_false(self):
        if self.quiz.check_answer("false"):

            self.score += 1
            self.score_label.config(text=f"score: {self.score}")
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)