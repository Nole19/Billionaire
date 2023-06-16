from tkinter import *
from pygame import mixer
import pyttsx3


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
        """Adding 2 windows for the result"""
        self.root_2 = Toplevel()
        self.root_2.config(bg="black")
        self.root_2.geometry("500x400+140+30")
        self.root_2.title("You won 0 pounds")

        image_label = Label(self.root_2, image=self.center_image, bd=0)
        image_label.pack(pady=30)

        label = Label(self.root_2, text=self.bad_or_good, font=("arial", 30, "bold"), bg="black",
                      fg="white")
        label.pack()

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


class SoundPlayer:
    def __init__(self):
        mixer.init()

    @staticmethod
    def play_sound(file_path):
        mixer.music.load(file_path)
        mixer.music.play()


class VoicePlayer:
    def __init__(self):
        self.engine = pyttsx3.init(driverName='espeak')
        self.voices = self.engine.getProperty('voices')
        self.selected_voice = None

    def set_voice(self, voice_name):
        for voice in self.voices:
            if voice_name.lower() in voice.name.lower():
                self.selected_voice = voice.id
                self.engine.setProperty('voice', self.selected_voice)
                break

    def speak_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

