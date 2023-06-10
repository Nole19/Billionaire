from tkinter import *
from tkmacosx import Button #only for mac to chage bg in buttons
#import pygame



"""Creating main window"""
# pygame.init()
root = Tk()
root.geometry("1352x652+0+0")
# root.resizable(False, False)

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
top_frame = Frame(left_frame, bd=20, bg='black', width=900, height=200)
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


"""Label"""
center_image = PhotoImage(file="images/center.png")
logo = Label(middle_frame, image=center_image, background="black", bd=0, width=300, height=200)
logo.grid()

"""Buttons"""
image50_50 = PhotoImage(file="images/50-50.png")
lifeline_50_50_Button = Button(top_frame, image=image50_50, bg='black', bd=4, activebackground="black",
                               width=180, height=80, command=change_50_50())
lifeline_50_50_Button.grid(row=0, column=0)
image_audience = PhotoImage(file="images/audiencePole.png")
lifeline_image_audience_Button = Button(top_frame, image=image_audience, bg='black', bd=4, activebackground="black",
                                        width=180, height=80)
lifeline_image_audience_Button.grid(row=0, column=1)

image_phone = PhotoImage(file="images/phoneAFriend.png")
lifeline_image_phone_Button = Button(top_frame, image=image_phone, bg='black', bd=4, activebackground="black",
                                     width=180, height=80)
lifeline_image_phone_Button.grid(row=0, column=2)

"""Money"""
amount_image = PhotoImage(file='images/Picture0.png')
amount_label = Label(right_frame, image=amount_image, bg='black', bd=0)
amount_label.grid(row=0, column=0)

"""Question"""
question = Entry(bottom_frame, font=("arial", 18, "bold"), bg="blue", fg="white", bd=5, width=44, justify=CENTER)
question.grid(row=0, column=0, columnspan=4, pady=4)

"""Answers"""
"""a"""
answer_a = Label(bottom_frame, font=("arial", 14, "bold"),text="A:", bg="black", fg="white", bd=5, justify=CENTER)
answer_a.grid(row=1, column=0, pady=4, sticky=W) #<----west

button_a = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=150, height=27,
                  justify=CENTER)
button_a.grid(row=1, column=1, pady=4)

"""b"""
answer_b = Label(bottom_frame, font=("arial", 14, "bold"),text="B:", bg="black", fg="white", bd=5, justify=LEFT)
answer_b.grid(row=1, column=2, pady=4, sticky=W)

button_b = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=150, height=27,
                  justify=CENTER)
button_b.grid(row=1, column=3, pady=4)

"""c"""

answer_c = Label(bottom_frame, font=("arial", 14, "bold"),text="C: ", bg="black", fg="white", bd=5, justify=LEFT)
answer_c.grid(row=2, column=0, pady=4, sticky=W)

button_c = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=150, height=27,
                  justify=CENTER)
button_c.grid(row=2, column=1, pady=4)


"""d"""

answer_d = Label(bottom_frame, font=("arial", 14, "bold"),text="D: ", bg="black", fg="white", bd=5, justify=LEFT)
answer_d.grid(row=2, column=2, pady=4, sticky=W)

button_d = Button(bottom_frame, font=("arial", 14, "bold"), bg="blue", fg="white", bd=1, width=150, height=27,
                  justify=CENTER)
button_d.grid(row=2, column=3, pady=4)



root.mainloop()