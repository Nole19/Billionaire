import tkinter as tk
from tkinter.ttk import Progressbar
# from questions import *
from progress import *
import random


all_questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["India", "354",
                "Heron", "Euro",
                "Javascript", "36",
                "Windows 7", "Elephant", "11:23PM", "KKR",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["USA", "366",
                 "Parrot", "Peso ",
                 "Python", "34",
                 "Linux", "Lion", "11.11PM", "CSK",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["China", "365",
                "Crow", "Dollar",
                "Java", "30",
                "Mac", "Tiger", "7:23PM", "MI",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["Russia", "420",
                 "Pigeon", "Yen",
                 "C++", "37",
                 "Windows XP", "Cow", "9.11PM", "RCB",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answer = ["Russia", "366", "Heron", "Dollar", "Python", "36",
                   "Linux", "Lion", "7:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]


class MillionaireGame:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1352x652+0+0")
        self.root.title("Who wants to be an IT Millionaire created by Pavel Zenchanka")
        self.root.config(background='black')

        """Frames: Right and LEft -> top, middle, bottom"""
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.grid()

        self.left_frame = tk.Frame(self.root, bd=20, bg='black', width=900, padx=110, height=600)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = tk.Frame(self.root, bd=20, bg='black', width=452, height=600)
        self.right_frame.grid(row=0, column=1)

        self.top_frame = tk.Frame(self.left_frame, bd=20, bg='black', width=900, padx=25, height=200)
        self.top_frame.grid(row=0, column=0)

        self.middle_frame = tk.Frame(self.left_frame, bd=20, bg='black', width=900, height=200)
        self.middle_frame.grid(row=1, column=0)

        self.bottom_frame = tk.Frame(self.left_frame, bd=20, bg='black', width=900, height=200)
        self.bottom_frame.grid(row=2, column=0)

        """Center image"""
        self.center_image = tk.PhotoImage(file="images/center.png")
        self.logo = tk.Label(self.middle_frame, image=self.center_image, bg="black", width=300, height=200)
        self.logo.grid()
        """Amount table"""
        self.amount_image = tk.PhotoImage(file='images/Picture0.png')
        self.amount_label = tk.Label(self.right_frame, image=self.amount_image, bg='black', bd=0, width=430, height=600)
        self.amount_label.grid(row=0, column=0)

        """Creating 3 buttons"""
        self.image50_50 = tk.PhotoImage(file="images/50-50.png")
        self.lifeline_50_50_Button = tk.Button(self.top_frame, image=self.image50_50, bg='black', bd=0,
                                               activebackground="black", command=self.change_50_50, width=180,
                                               height=80)
        self.lifeline_50_50_Button.grid(row=0, column=0)

        self.image_audience = tk.PhotoImage(file="images/audiencePole.png")
        self.lifeline_image_audience_Button = tk.Button(self.top_frame, image=self.image_audience, bg='black', bd=0,
                                                        activebackground="black", command=self.change_audience,
                                                        width=180, height=80)
        self.lifeline_image_audience_Button.grid(row=0, column=1)

        self.image_phone = tk.PhotoImage(file="images/phoneAFriend.png")
        self.lifeline_image_phone_Button = tk.Button(self.top_frame, image=self.image_phone, bg='black', bd=0,
                                                     activebackground="black", command=self.change_phone, width=180,
                                                     height=80)
        self.lifeline_image_phone_Button.grid(row=0, column=2)

        """Question panel"""
        self.question_entry = tk.Entry(self.bottom_frame, font=("Arial", 18, "bold"), bg="blue", fg="white", bd=5,
                                       width=44, justify=tk.CENTER)
        self.question_entry.grid(row=0, column=0, columnspan=4, pady=4)

        self.question_label = tk.Label(self.bottom_frame, font=("arial", 18, "bold"), bg="blue", fg="white", bd=5,
                                       width=44, justify=tk.CENTER, text=all_questions[0])
        self.question_label.grid(row=0, column=0, columnspan=4, pady=4)
        """Answers"""
        """a"""
        self.answer_a = tk.Label(self.bottom_frame, font=("arial", 14, "bold"), text="A:", bg="black", fg="white", bd=5,
                                 justify=tk.CENTER)
        self.answer_a.grid(row=1, column=0, pady=4, sticky=tk.W)  # <----west

        self.button_a = tk.Button(self.bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30,
                                  height=2, justify=tk.CENTER, text=first_option[0], activebackground="blue",
                                  activeforeground='black', cursor="hand2")
        self.button_a.grid(row=1, column=1, pady=4)

        """b"""
        self.answer_b = tk.Label(self.bottom_frame, font=("arial", 14, "bold"), text="B:", bg="black", fg="white", bd=5,
                                 justify=tk.LEFT)
        self.answer_b.grid(row=1, column=2, pady=4, sticky=tk.W)

        self.button_b = tk.Button(self.bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30,
                                  height=2, justify=tk.CENTER, text=second_option[0], activebackground="blue",
                                  activeforeground='black', cursor="hand2")
        self.button_b.grid(row=1, column=3, pady=4)

        """c"""

        self.answer_c = tk.Label(self.bottom_frame, font=("arial", 14, "bold"), text="C:", bg="black", fg="white", bd=5,
                                 justify=tk.LEFT)
        self.answer_c.grid(row=2, column=0, pady=4, sticky=tk.W)

        self.button_c = tk.Button(self.bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30,
                                  height=2, justify=tk.CENTER, text=third_option[0], activebackground="blue",
                                  activeforeground='black', cursor="hand2")
        self.button_c.grid(row=2, column=1, pady=4)

        """d"""

        self.answer_d = tk.Label(self.bottom_frame, font=("arial", 14, "bold"), text="D:", bg="black", fg="white", bd=5,
                                 justify=tk.LEFT)
        self.answer_d.grid(row=2, column=2, pady=4, sticky=tk.W)

        self.button_d = tk.Button(self.bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30,
                                  height=2, justify=tk.CENTER, text=fourth_option[0], activebackground="blue",
                                  activeforeground='black', cursor="hand2")
        self.button_d.grid(row=2, column=3, pady=4)

        """Creating list for choices for the function of 50_50 button"""
        self.choices = [self.button_a, self.button_b, self.button_c, self.button_d]

        """Creating audience(That's why we need to import tkinter.tkk)"""
        self.audience_progressbar_a = Progressbar(root, orient=VERTICAL, length=100)
        self.audience_progressbar_b = Progressbar(root, orient=VERTICAL, length=100)
        self.audience_progressbar_c = Progressbar(root, orient=VERTICAL, length=100)
        self.audience_progressbar_d = Progressbar(root, orient=VERTICAL, length=100)

        self.audience_progressbar_a_label = Label(root, text="A", font=("arial", 23, "bold"), bg="black", fg="white")
        self.audience_progressbar_b_label = Label(root, text="B", font=("arial", 23, "bold"), bg="black", fg="white")
        self.audience_progressbar_c_label = Label(root, text="C", font=("arial", 23, "bold"), bg="black", fg="white")
        self.audience_progressbar_d_label = Label(root, text="D", font=("arial", 23, "bold"), bg="black", fg="white")

        """Creating winning images"""
        self.images = []
        self.images = []
        image1 = tk.PhotoImage(file='images/Picture1.png')
        image2 = tk.PhotoImage(file='images/Picture2.png')
        image3 = tk.PhotoImage(file='images/Picture3.png')
        image4 = tk.PhotoImage(file='images/Picture4.png')
        image5 = tk.PhotoImage(file='images/Picture5.png')
        image6 = tk.PhotoImage(file='images/Picture6.png')
        image7 = tk.PhotoImage(file='images/Picture7.png')
        image8 = tk.PhotoImage(file='images/Picture8.png')
        image9 = tk.PhotoImage(file='images/Picture9.png')
        image10 = tk.PhotoImage(file='images/Picture10.png')
        image11 = tk.PhotoImage(file='images/Picture11.png')
        image12 = tk.PhotoImage(file='images/Picture12.png')
        image13 = tk.PhotoImage(file='images/Picture13.png')
        image14 = tk.PhotoImage(file='images/Picture14.png')
        image15 = tk.PhotoImage(file='images/Picture15.png')
        self.images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11,
                       image12, image13, image14, image15]

        """Creating initialization of clicking particular button with left button of mouth"""
        self.button_a.bind('<Button-1>', self.select)
        self.button_b.bind('<Button-1>', self.select)
        self.button_c.bind('<Button-1>', self.select)
        self.button_d.bind('<Button-1>', self.select)

    def select(self, event):
        """Shows us which button clicked"""
        b = event.widget
        value = b['text']
        """Deleting audience """
        self.audience_progressbar_a.place_forget()
        self.audience_progressbar_b.place_forget()
        self.audience_progressbar_c.place_forget()
        self.audience_progressbar_d.place_forget()

        self.audience_progressbar_a_label.place_forget()
        self.audience_progressbar_b_label.place_forget()
        self.audience_progressbar_c_label.place_forget()
        self.audience_progressbar_d_label.place_forget()
        """Loop to run every time questions"""
        for k in range(15):
            if value == correct_answer[k]:
                if value == correct_answer[14]:
                    root_3 = QuizResultWindow(root, "Victory! Cash waiting!!")
                    root_3.show_result_window()
                    break
                self.question_label.config(text=all_questions[k + 1])
                self.button_a.config(text=first_option[k + 1])
                self.button_b.config(text=second_option[k + 1])
                self.button_c.config(text=third_option[k + 1])
                self.button_d.config(text=fourth_option[k + 1])
                self.amount_label.config(image=self.images[k])
            if value not in correct_answer:
                root_2 = QuizResultWindow(root, "You lose")
                root_2.show_result_window()
                break

    def change_50_50(self):
        """Changes 50_50 pictures """
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=0)
        canvas.delete("all")
        image_50_50_x = tk.PhotoImage(file="images/50-50-X.png")
        canvas.create_image(90, 40, image=image_50_50_x)
        canvas.image = image_50_50_x
        """Randomly deleting 2 numbers"""
        for d in range(2):
            random_choice = random.randint(0, 3)
            if self.choices[random_choice].cget("text") not in correct_answer:
                self.choices[random_choice].config(text='')
                self.choices.pop(random_choice)
            else:
                self.choices[random_choice - 1].config(text='')
                self.choices.pop(random_choice - 1)

    def change_audience(self):
        """Changes audience pictures"""
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=1)
        canvas.delete("all")
        image_audience_x = tk.PhotoImage(file="images/audiencePoleX.png")
        canvas.create_image(90, 40, image=image_audience_x)
        canvas.image = image_audience_x
        """Placing audience"""
        self.audience_progressbar_a.place(x=750, y=190)
        self.audience_progressbar_b.place(x=790, y=190)
        self.audience_progressbar_c.place(x=830, y=190)
        self.audience_progressbar_d.place(x=870, y=190)
        self.audience_progressbar_a_label.place(x=750, y=320)
        self.audience_progressbar_b_label.place(x=790, y=320)
        self.audience_progressbar_c_label.place(x=830, y=320)
        self.audience_progressbar_d_label.place(x=870, y=320)
        """Logic"""
        for answer in self.choices:
            if answer.cget("text") in correct_answer:
                if answer.cget("text") in first_option:
                    self.audience_progressbar_a.config(value=76)
                    self.audience_progressbar_b.config(value=27)
                    self.audience_progressbar_c.config(value=34)
                    self.audience_progressbar_d.config(value=19)
                elif answer.cget("text") in second_option:
                    self.audience_progressbar_b.config(value=76)
                    self.audience_progressbar_a.config(value=27)
                    self.audience_progressbar_c.config(value=34)
                    self.audience_progressbar_d.config(value=19)
                elif answer.cget("text") in third_option:
                    self.audience_progressbar_c.config(value=76)
                    self.audience_progressbar_b.config(value=27)
                    self.audience_progressbar_a.config(value=34)
                    self.audience_progressbar_d.config(value=19)
                elif answer.cget("text") in fourth_option:
                    self.audience_progressbar_d.config(value=76)
                    self.audience_progressbar_b.config(value=27)
                    self.audience_progressbar_c.config(value=34)
                    self.audience_progressbar_a.config(value=19)
                break

    def change_phone(self):
        """Changing hone call picture"""
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=2)
        canvas.delete("all")
        image_phone_x = tk.PhotoImage(file="images/phoneAFriendX.png")
        canvas.create_image(90, 40, image=image_phone_x)
        canvas.image = image_phone_x


if __name__ == "__main__":
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()
