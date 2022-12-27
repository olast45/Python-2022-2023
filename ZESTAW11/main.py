from tkinter import *
import random

window = Tk()
window.title("Rock Paper Scissors")
window.resizable(0, 0)
window.configure(background="white")
window.geometry("500x300")


def play(move):
    computer_move = random.choice(["rock", "paper", "scissors"])

    if move == "rock":
        player_text.set("ROCK")
        if computer_move == "rock":
            result_text.set("It's a tie!")
            result_label.config(fg="gold")
            computer_text.set("ROCK")
        elif computer_move == "paper":
            result_text.set("You lose!")
            result_label.config(fg="red")
            computer_text.set("PAPER")
        else:
            result_text.set("You win!")
            result_label.config(fg="green")
            computer_text.set("SCISSORS")
    elif move == "paper":
        player_text.set("PAPER")
        if computer_move == "rock":
            result_text.set("You win!")
            result_label.config(fg="green")
            computer_text.set("ROCK")
        elif computer_move == "paper":
            result_text.set("It's a tie!")
            result_label.config(fg="gold")
            computer_text.set("PAPER")
        else:
            result_text.set("You lose!")
            result_label.config(fg="red")
            computer_text.set("SCISSORS")
    else:
        player_text.set("SCISSORS")
        if computer_move == "rock":
            result_text.set("You lose!")
            result_label.config(fg="red")
            computer_text.set("ROCK")
        elif computer_move == "paper":
            result_text.set("You win!")
            result_label.config(fg="green")
            computer_text.set("PAPER")
        else:
            result_text.set("It's a tie!")
            result_label.config(fg="gold")
            computer_text.set("SCISSORS")


def set_player_move(move):
    def game():
        play(move)
    return game


label = Label(window, text="ROCK PAPER SCISSORS", fg="lightblue", highlightbackground="white", bg="white", font=("Arial", 25))
label.pack()

player_var = StringVar()
rock_button = Button(text="Rock", command=set_player_move("rock"), highlightbackground="white", height=2, bg="white")
paper_button = Button(text="Paper", command=set_player_move("paper"), highlightbackground="white", height=2, bg="white")
scissors_button = Button(text="Scissors", command=set_player_move("scissors"), highlightbackground="white", height=2, bg="white")


computer_label = Label(window, text="Computer's move:")
player_label = Label(window, text="Player's move:")

computer_text = StringVar()
computer_label = Label(textvariable=computer_text, highlightbackground="white", bg="white")
player_text = StringVar()
player_label = Label(textvariable=player_text, highlightbackground="white", bg="white")


result_text = StringVar()
result_label = Label(textvariable=result_text, highlightbackground="white", bg="white", font=("Arial", 20))

label = Label(text="PLAYER         VS          COMPUTER", highlightbackground="white", bg="white", font=("Arial", 15), fg="blue")

rock_button.place(x=100, y=50)
paper_button.place(x=210, y=50)
scissors_button.place(x=320, y=50)
label.place(x=130, y=130)
result_label.place(x=205, y=210)
computer_label.place(x=290, y=160)
player_label.place(x=150, y=160)

window.mainloop()
