import tkinter as tk


class MillionaireGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1352x652+0+0")
        self.root.title("Who wants to be an IT Millionaire created by Pavel Zenchanka")
        self.root.config(background='black')

        self.create_frames()
        self.create_labels()
        self.create_buttons()
        self.create_entries()

    def create_frames(self):
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

    def create_labels(self):
        """Center image"""
        self.center_image = tk.PhotoImage(file="images/center.png")
        self.logo = tk.Label(self.middle_frame, image=self.center_image, bg="black", width=300, height=200)
        self.logo.grid()
        """Amount table"""
        self.amount_image = tk.PhotoImage(file='images/Picture0.png')
        self.amount_label = tk.Label(self.right_frame, image=self.amount_image, bg='black', bd=0, width=430, height=600)
        self.amount_label.grid(row=0, column=0)

    def create_buttons(self):
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

    def create_entries(self):
        """Question pannel"""
        self.question = tk.Entry(self.bottom_frame, font=("Arial", 18, "bold"), bg="blue", fg="white", bd=5,
                                 width=44, justify=tk.CENTER)
        self.question.grid(row=0, column=0, columnspan=4, pady=4)
        """4 options to answer"""
        self.create_answer("A", 1, 0)
        self.create_answer("B", 1, 2)
        self.create_answer("C", 2, 0)
        self.create_answer("D", 2, 2)

    def create_answer(self, label_text, row, column):
        """Creating option of answer"""
        answer_label = tk.Label(self.bottom_frame, font=("Arial", 14, "bold"), text=f"{label_text}:", bg="black",
                                fg="white", bd=5, justify="left")
        answer_label.grid(row=row, column=column, pady=4, sticky=tk.W)

        button = tk.Button(self.bottom_frame, font=("Arial", 14, "bold"), bg="blue", fg="white", bd=1, width=17,
                           height=2, justify=tk.CENTER)
        button.grid(row=row, column=column + 1, pady=4)

    def change_50_50(self):
        """Changes 50_50 pictures """
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=0)
        canvas.delete("all")
        image_50_50_x = tk.PhotoImage(file="images/50-50-X.png")
        canvas.create_image(90, 40, image=image_50_50_x)
        canvas.image = image_50_50_x

    def change_audience(self):
        """Changes audience pictures"""
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=1)
        canvas.delete("all")
        image_audience_x = tk.PhotoImage(file="images/audiencePoleX.png")
        canvas.create_image(90, 40, image=image_audience_x)
        canvas.image = image_audience_x

    def change_phone(self):
        """Changing hone call picture"""
        canvas = tk.Canvas(self.top_frame, bg="black", width=180, height=80)
        canvas.grid(row=0, column=2)
        canvas.delete("all")
        image_phone_x = tk.PhotoImage(file="images/phoneAFriendX.png")
        canvas.create_image(90, 40, image=image_phone_x)
        canvas.image = image_phone_x

    def change_million_picture(self):
        canvas = tk.Canvas(self.right_frame, bg="black", width=430, height=600)
        canvas.grid(row=0, column=0)
        canvas.delete("all")
        image_1 = tk.PhotoImage(file=f"images/Picture1.png")
        canvas.create_image(215, 300, image=image_1)
        canvas.image = image_1


if __name__ == "__main__":
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()
