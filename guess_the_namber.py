import random
from tkinter import *


class General_Win(object):

    def __init__(self, tk):
        self.root_win = tk
        self.root_win.title("Guess the namber")
        self.root_win.geometry("300x150")

        self.app = Game_frame(self.root_win)

        self.root_win.mainloop()


class Game_frame(Frame):

    def __init__(self, frame_win):
        self.frame_win = frame_win
        super(Game_frame, self).__init__(frame_win)
        self.grid(row=0, column=0)
        self.radio_button()

    def radio_button(self):
        Label(self,
              text="the number of attempts and press start game"
              ).grid(row=0, column=0)

        self.radio_button_value = IntVar()

        Radiobutton(self,
                    text="None",
                    variable=self.radio_button_value,
                    value=0,
                    ).grid(row=1, column=0, sticky=W)

        Radiobutton(self,
                    variable=self.radio_button_value,
                    text="5",
                    value=5
                    ).grid(row=2, column=0, sticky=W)

        Radiobutton(self,
                    variable=self.radio_button_value,
                    text="10",
                    value=10
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    variable=self.radio_button_value,
                    text="15",
                    value=15
                    ).grid(row=4, column=0, sticky=W)

        self.button = Button(self,
               text="Start Game",
               command=self.start_game
               )
        self.button.grid(row=5, column=0)

    def start_game(self):
        self.game = Game_Window(self.frame_win)
        self.game.get_count(self.radio_button_value.get())
        self.game.change_attemps_label()


class Game_Window(Toplevel):

    def __init__(self, window):
        self.frame_win = window
        super(Game_Window, self).__init__(self.frame_win)
        self.title("Win or Die")
        self.geometry("200x90")
        self.rand_int = random.randint(0, 100)
        self.count = 0
        self.game_flag = True
        self.display_items()

    def display_items(self):

        self.attemps_label = Label(self, text="You attemps : Error")
        self.attemps_label.grid(row=0, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=1, column=0)

        self.label_game_messege = Label(self, text="Enter number and start game !!!")
        self.label_game_messege.grid(row=2, column=0)

        Button(self,
               text="I will try ...",
               command=self.game_logic
               ).grid(row=3, column=0)

    def get_count(self, count):
        self.count = count

    def destroy_win(self):
        self.destroy()

    def change_massege_label(self, massege):
        self.label_game_messege.configure(text = str(massege))

    def change_attemps_label(self):
        if self.count > 0:
            self.attemps_label.configure(text = "You attempps : " + str(self.count))
        else:
            self.attemps_label.configure(text = "You not have attemps !!!")

    def game_logic(self):
        if self.count > 0:
            self.count -= 1
            self.change_attemps_label()
            try:
                if self.rand_int == int(self.entry.get()):
                    winner_window = Winer_window(self.frame_win, self.rand_int, self.count)
                    self.destroy()
                if self.rand_int > int(self.entry.get()):
                    self.change_massege_label("Number more !")
                else:
                    self.change_massege_label("Number low !")
            except ValueError:
                self.change_massege_label("Idi naxyi !")
        else:
            self.destroy_win()


class Winer_window(Toplevel):
    def __init__(self, frame_win, randint, attemps):

        self.rand_ind = str(randint)
        self.attemps = str(attemps)
        super(Winer_window, self).__init__(frame_win)
        self.display_item()

    def display_item(self):
        self.label_gg = Label(self, text="You wins !!!!")
        self.label_gg.grid(row=0, column=0)

        self.label_randint = Label(self, text="Rand int : " + self.rand_ind)
        self.label_randint.grid(row=1, column=0)


if __name__ == '__main__':
    win = Tk()
    General_Win(win)
