from tkinter import *


class QuizResultWindow:
    def __init__(self, root, bad_or_good):
        self.root = root
        self.bad_or_good = bad_or_good
        self.root_2 = None
        self.center_image = PhotoImage(file="images/center.png")

    def close_window(self):
        self.root_2.destroy()
        self.root.destroy()

    def show_result_window(self):

        self.root_2 = Toplevel()
        self.root_2.config(bg="black")
        self.root_2.geometry("500x400+140+30")
        self.root_2.title("You won 0 pounds")

        image_label = Label(self.root_2, image=self.center_image, bd=0)
        image_label.pack(pady=30)

        label = Label(self.root_2, text=self.bad_or_good, font=("arial", 30, "bold"), bg="black",
                      fg="white")
        label.pack()

        # try_again_button = Button(self.root_2, text="Try again", font=("arial", 20, "bold"),
        #                           bg="black", fg="white", bd=0, activebackground="black", cursor="hand2",
        #                           activeforeground="white")
        # try_again_button.pack()
        close_button = Button(self.root_2, text="Close", font=("arial", 20, "bold"),
                              bg="black", fg="white", bd=0, activebackground="black", cursor="hand2",
                              activeforeground="white", command=self.close_window)
        close_button.pack()
        if self.bad_or_good == "Victory! Cash waiting!!":
            happy_emoji_img = PhotoImage(file="images/happy.png")
            happy_emoji_label = Label(self.root_2, image=happy_emoji_img, bg="black")
            happy_emoji_label.place(x=30, y=280)

            happy_emoji_label_1 = Label(self.root_2, image=happy_emoji_img, bg="black")
            happy_emoji_label_1.place(x=400, y=280)
        else:
            sad_emoji_img = PhotoImage(file="images/sad.png")
            sad_emoji_label = Label(self.root_2, image=sad_emoji_img, bg="black")
            sad_emoji_label.place(x=30, y=280)

            sad_emoji_label_1 = Label(self.root_2, image=sad_emoji_img, bg="black")
            sad_emoji_label_1.place(x=400, y=280)

        self.root_2.mainloop()




# class Progress():
#     def __init__(self, main):
#         self.main = main
#         self.main.config(bg="black")
#         self.main.geometry("500x400+140+30")
#         self.main.title("You won 0 pounds")
#         self.central_image = tk.PhotoImage(file="images/center.png")
#         """Images in new window"""
#         self.image_label = tk.Label(self.main, image=self.central_image, bd=0)
#         self.image_label.pack(pady=30)
#
#         self.win_label = tk.Label(self.main, text="Victory! Cash waiting!!", font=("arial", 30, "bold"), bg="black",
#                           fg="white")
#         self.win_label.pack()
#
#         """Buttons"""
#         self.try_again_button = tk.Button(self, text="Try again", font=("arial", 20, "bold"),
#                                   bg="black", fg="white", bd=0, activebackground="black", cursor="hand2",
#                                   activeforeground="white", command=self.try_again)
#         self.try_again_button.pack()
        # close_button = tk.Button(self.main, text="Close", font=("arial", 20, "bold"),
        #                       bg="black", fg="white", bd=0, activebackground="black", cursor="hand2",
        #                       activeforeground="white", command=self.close_window)
        # close_button.pack()

        # """Images"""
        # happy_emoji_img = tk.PhotoImage(file="images/happy.png")
        # self.happy_emoji_label = tk.Label(self.main, image=happy_emoji_img, bg="black")
        # self.happy_emoji_label.place(x=30, y=280)
        #
        # self.happy_emoji_label_1 = tk.Label(self.main, image=happy_emoji_img, bg="black")
        # self.happy_emoji_label_1.place(x=400, y=280)
    #
    # def close_window(self):
    #     self.main.destroy()
#
#
