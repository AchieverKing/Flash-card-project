import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    start_data = pandas.read_csv("data/french_words.csv")
    to_learn = start_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
"""Picking a random word from the french list of words"""


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


"""flipping the card to the english translation after 3 seconds"""


def flip_card():
    canvas.itemconfig(card_bg, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


"""checking if the user already knows the word and creating a word to learn with the unknown words"""


def known_words():
    to_learn.remove(current_card)
    known_data = pandas .DataFrame(to_learn)
    known_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

"""Image pack"""
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"), text="")
canvas.grid(column=0, row=0, columnspan=2)

nun_image = PhotoImage(file="images/right.png")
known = Button(image=nun_image, command=known_words)
known.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
known.grid(row=1, column=0)

un_image = PhotoImage(file="images/wrong.png")
unknown = Button(image=un_image, command=next_card)
unknown.config(pady=50, padx=50, bg=BACKGROUND_COLOR, highlightthickness=0)
unknown.grid(row=1, column=1)

next_card()

window.mainloop()
