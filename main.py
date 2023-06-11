from tkinter import *
import pygame
from questions import *
"""Variables with questions and answers"""
# all_questions = []
# first_option = []
# second_option = []
# third_option = []
# fourth_option = []
# correct_answer = []


# all_questions.append("When was created Python?")
# all_questions.append("Year of creating C#?")
# first_option.append("1988")
# first_option.append("1985")
# second_option.append("1990")
# second_option.append("1997")
# third_option.append("1992")
# third_option.append("1989")
# fourth_option.append("1991")
# fourth_option.append("1998")
# correct_answer.append("1991")
# correct_answer.append('1989')
#
#
def select(event):
    """Shows us which button clicked"""
    b = event.widget
    value = b['text']
    for k in range(15):
        if value == correct_answer[k]:
            question.config(text=all_questions[k+1])
            button_a.config(text=first_option[k+1])
            button_b.config(text=second_option[k+1])
            button_c.config(text=third_option[k+1])
            button_d.config(text=fourth_option[k+1])
            amount_label.config(image=images[k])


"""Creating main window"""
pygame.init()
root = Tk()
root.geometry("1352x652+0+0")
root.title("Who wants to be an it millionaire created by Pavel Zenchanka")
root.config(background='black')


"""Frames"""
frame = Frame(root, bg='black')
frame.grid()

left_frame = Frame(root, bd=20, bg='black', width=900, padx=110, height=600)
left_frame.grid(row=0, column=0)

right_frame = Frame(root, bd=20, bg='black', width=452, height=600)
right_frame.grid(row=0, column=1)

"""Dividing left frame into 3 parts"""
top_frame = Frame(left_frame, bd=20, bg='black', width=900, padx=25, height=200)
top_frame.grid(row=0, column=0)

middle_frame = Frame(left_frame, bd=20, bg='black', width=900, height=200)
middle_frame.grid(row=1, column=0)

bottom_frame = Frame(left_frame, bd=20, bg='black', width=900, height=200)
bottom_frame.grid(row=2, column=0)

"""Change buttons functions"""


def change_50_50():
    canvas = Canvas(top_frame, bg="black", width=180, height=80)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image_50_50_x = PhotoImage(file="images/50-50-X.png")
    canvas.create_image(90, 40, image=image_50_50_x)
    canvas.image = image_50_50_x


def change_audience():
    canvas = Canvas(top_frame, bg="black", width=180, height=80)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    image_audience_x = PhotoImage(file="images/audiencePoleX.png")
    canvas.create_image(90, 40, image=image_audience_x)
    canvas.image = image_audience_x


def change_phone():
    canvas = Canvas(top_frame, bg="black", width=180, height=80)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    image_phone_x = PhotoImage(file="images/phoneAFriendX.png")
    canvas.create_image(90, 40, image=image_phone_x)
    canvas.image = image_phone_x


def million_picture_1():
    canvas = Canvas(right_frame, bg="black", width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image_1 = PhotoImage(file="images/Picture1.png")
    canvas.create_image(215, 300, image=image_1)
    canvas.image = image_1


def million_picture_2():
    canvas = Canvas(right_frame, bg="black", width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    image_2 = PhotoImage(file="images/Picture2.png")
    canvas.create_image(215, 300, image=image_2)
    canvas.image = image_2


"""Label"""
center_image = PhotoImage(file="images/center.png")
logo = Label(middle_frame, image=center_image, background="black", width=300, height=200)
logo.grid()

"""Buttons"""
image50_50 = PhotoImage(file="images/50-50.png")
lifeline_50_50_Button = Button(top_frame, image=image50_50, bg='black', bd=0, activebackground="black",
                               command=change_50_50, width=180, height=80)
lifeline_50_50_Button.grid(row=0, column=0)
image_audience = PhotoImage(file="images/audiencePole.png")
lifeline_image_audience_Button = Button(top_frame, image=image_audience, bg='black', bd=0, activebackground="black",
                                        command=change_audience, width=180, height=80)
lifeline_image_audience_Button.grid(row=0, column=1)

image_phone = PhotoImage(file="images/phoneAFriend.png")
lifeline_image_phone_Button = Button(top_frame, image=image_phone, bg='black', bd=0, activebackground="black",
                                     command=change_phone, width=180, height=80)
lifeline_image_phone_Button.grid(row=0, column=2)

"""Money"""
amount_image = PhotoImage(file='images/Picture0.png')
amount_label = Label(right_frame, image=amount_image, bg='black', bd=0, width=430, height=600)
amount_label.grid(row=0, column=0)
image1 = PhotoImage(file='images/Picture1.png')
image2 = PhotoImage(file='images/Picture2.png')
image3 = PhotoImage(file='images/Picture3.png')
image4 = PhotoImage(file='images/Picture4.png')
image5 = PhotoImage(file='images/Picture5.png')
image6 = PhotoImage(file='images/Picture6.png')
image7 = PhotoImage(file='images/Picture7.png')
image8 = PhotoImage(file='images/Picture8.png')
image9 = PhotoImage(file='images/Picture9.png')
image10 = PhotoImage(file='images/Picture10.png')
image11 = PhotoImage(file='images/Picture11.png')
image12 = PhotoImage(file='images/Picture12.png')
image13 = PhotoImage(file='images/Picture13.png')
image14 = PhotoImage(file='images/Picture14.png')
image15 = PhotoImage(file='images/Picture15.png')
images = [image1, image2, image3, image4, image5,
          image6, image7, image8, image9, image10, image11, image12, image13, image14, image15]

"""Question"""
question = Label(bottom_frame, font=("arial", 18, "bold"), bg="blue", fg="white", bd=5, width=44, justify=CENTER,
                 text=all_questions[0])
question.grid(row=0, column=0, columnspan=4, pady=4)

"""Answers"""
"""a"""
answer_a = Label(bottom_frame, font=("arial", 14, "bold"),text="A:", bg="black", fg="white", bd=5, justify=CENTER)
answer_a.grid(row=1, column=0, pady=4, sticky=W) #<----west

button_a = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30, height=2,
                  justify=CENTER, text=first_option[0], activebackground="blue",
                  activeforeground='black')
button_a.grid(row=1, column=1, pady=4)

"""b"""
answer_b = Label(bottom_frame, font=("arial", 14, "bold"), text="B:", bg="black", fg="white", bd=5, justify=LEFT)
answer_b.grid(row=1, column=2, pady=4, sticky=W)

button_b = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30, height=2,
                  justify=CENTER, text=second_option[0], activebackground="blue",
                  activeforeground='black')
button_b.grid(row=1, column=3, pady=4)

"""c"""

answer_c = Label(bottom_frame, font=("arial", 14, "bold"), text="C: ", bg="black", fg="white", bd=5, justify=LEFT)
answer_c.grid(row=2, column=0, pady=4, sticky=W)

button_c = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30, height=2,
                  justify=CENTER, text=third_option[0], activebackground="blue",
                  activeforeground='black')
button_c.grid(row=2, column=1, pady=4)


"""d"""

answer_d = Label(bottom_frame, font=("arial", 14, "bold"), text="D: ", bg="black", fg="white", bd=5, justify=LEFT)
answer_d.grid(row=2, column=2, pady=4, sticky=W)

button_d = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=30, height=2,
                  justify=CENTER, text=fourth_option[0], activebackground="blue",
                  activeforeground='black')
button_d.grid(row=2, column=3, pady=4)

"""Creating initialization of clicking particular button with left button of mouth"""
button_a.bind('<Button-1>', select)
button_b.bind('<Button-1>', select)
button_c.bind('<Button-1>', select)
button_d.bind('<Button-1>', select)
root.mainloop()
