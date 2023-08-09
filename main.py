from tkinter import *
 #it is pandas,
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except:
    original_data=pandas.read_csv("data/my_python_revision.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")
current_card={}

# def back_side():
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(image, image=back_image)
#     canvas.itemconfig(word_card, text=current_card["English"])
#     canvas.itemconfig(title_card, text="English")



def next_card():
    global current_card
    global flip_timer
    #now due to this after cancel time will stop moving
    windows.after_cancel(flip_timer)
    #here current_card which is a dict is replaced by new key value
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_word, text=current_card["Question"], fill="black")
    canvas.itemconfig(card_title, text="Question", fill="black")
    canvas.itemconfig(card_background, image=front_image)
    #even after putting windows.after(3000, func=flip_card) in a variable
    # we had to put value so that we could use windows.after_cancel(flip_timer)
    flip_timer=windows.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Answer", fill="White")
    canvas.itemconfig(card_word, text=current_card["Answer"], fill="White")
    canvas.itemconfig(card_background, image=back_image)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()




windows=Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer=windows.after(3000, func=flip_card)

# as long as we will provide coordinate of each object(image, text), each will
#overlap each other
canvas=Canvas(width=800, height=526)
back_image=PhotoImage(file="images/card_back.png")
front_image=PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400, 263, image=front_image)
#canvas.grid(row=0,column=0,columnspan=2)
#backgroung, text, heighlighttickness
card_title=canvas.create_text(400, 150, text="", font=("Ariel",40, "italic"))
card_word=canvas.create_text(400, 263, text="", font=("Ariel",60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image=PhotoImage(file="images/right.png")
check_button=Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()




windows.mainloop()


