import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tkinter.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"), width=200)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_img = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=self.true_img, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)
        self.false_img = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=self.false_img, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_clicked(self):
        main_answer = self.quiz.check_answer("True")
        self.feedback(main_answer)
        self.score_catch(main_answer)
    def false_clicked(self):
        main_answer = self.quiz.check_answer("False")
        self.feedback(main_answer)
        self.score_catch(main_answer)

    def feedback(self, main_answer):
        if main_answer:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.next_question)

    def score_catch(self, main_answer):
        if main_answer:
            self.score +=1
            self.score_label.config(text=f"Score: {self.score}")

