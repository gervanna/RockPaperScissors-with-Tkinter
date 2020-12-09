import random
from tkinter import Tk, Button, Label, PhotoImage, TOP, BOTTOM, Frame

# base gui initialization
root = Tk()
root.wm_title = "Rock Paper Scissors" #app title
root.geometry("500x600") #window size
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

startPage=Frame(root)
startPage.grid(row=0, column=0, sticky="nsew")

gamePage=Frame(root)
gamePage.grid(row=0, column=0, sticky="nsew")
startPage.tkraise()

# grabbing our images
rock = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/rock-100x120.png")
paper = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/paper-100x120.png")
scissors = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/scissors-100x120.png")

game_choices = [rock, paper, scissors]
style_button = ('Verdana', 14, 'bold')

welcome = Label(startPage, padx=20, pady=20, fg='blue', font='Verdana 24 bold', text= "Welcome to Rock Paper Scissors.")
welcome.grid(row=0, column=0, columnspan=2, sticky='nsew')

rules = '''The outcome of the game is determined by 3 simple rules:
\n1. Rock wins against scissors.
\n2. Scissors win against paper.
\n3. Paper wins against rock.'''
info = Label(startPage, font='Verdana 14', bg='#B0C4DE', text=rules)
info.grid(row=1, column=0, columnspan=2, pady=10, sticky='nsew')

winLimit = 0

def singleStart():
    global winLimit
    winLimit = 1
    gamePage.tkraise()

def multigameStreak():
    global winLimit
    winLimit = 10
    gamePage.tkraise()

single=Button(startPage, font=style_button, text="Single", command=singleStart)
single.grid(row=2, column=0, pady=50)

streak=Button(startPage, font=style_button, text="Streak", command=multigameStreak)
streak.grid(row=2, column=1, pady=50)

def pickedRock():
    player_choice= 0
    runGame(player_choice)

def pickedPaper():
    player_choice = 1
    runGame(player_choice)

def pickedScissors():
    player_choice = 2
    runGame(player_choice)

rps_label=Label(gamePage, font=style_button, text="Please choose one of the following:\n")
rps_label.pack()

rockButton = Button(gamePage, font=style_button, padx=2, pady=2, text="rock", command=pickedRock)
rockButton.pack(pady=3)

paperButton = Button(gamePage, font=style_button, padx=2, pady=2, text="paper", command=pickedPaper)
paperButton.pack(pady=3)

scissorsButton = Button(gamePage, font=style_button, padx=2, pady=2, text="scissors", command=pickedScissors)
scissorsButton.pack(pady=3)

player_choice_label = Label(gamePage)
player_choice_label.pack()

computer_choice_label = Label(gamePage)
computer_choice_label.pack()

statusLabel = Label(gamePage)
statusLabel.pack()

player_score_label = Label(gamePage)
player_score_label.pack()

computer_score_label = Label(gamePage)
computer_score_label.pack()

player_score = 0
computer_score = 0

def resetGame():
    global player_score
    global computer_score

    player_choice_label.configure(text="", image="")
    computer_choice_label.configure(text="", image="")
    statusLabel.configure(text="", image="")
    player_score = 0
    computer_score = 0
    player_score_label.configure(text="")
    computer_score_label.configure(text="")
    rockButton.configure(state="normal")
    paperButton.configure(state="normal")
    scissorsButton.configure(state="normal")
    resetButton.configure(state="disabled")
    startPage.tkraise()


resetButton = Button(gamePage, font=style_button, text="Reset", command=resetGame, state="disabled")
resetButton.pack()

def exitGame():
    root.destroy()

exitButton = Button(root, font=style_button, text="Exit App", command=exitGame)
exitButton.grid(row=1, column=0)

def runGame(player_choice):
    global player_score
    global computer_score

    player_choice_label.configure(text="You chose:\n", image=game_choices[player_choice], compound=BOTTOM)

    computer_choice = random.randint(0, 2)

    computer_choice_label.configure(text="The computer chose:\n", image=game_choices[computer_choice], compound=BOTTOM)

    if player_choice == computer_choice:
        statusLabel.configure(text="\nIt's a draw.")

    elif player_choice == 0 and computer_choice == 2:
        statusLabel.configure(text="\nYou win this round!")
        player_score +=1

    elif computer_choice == 0 and player_choice== 2:
        statusLabel.configure(text="\nYou lose...")
        computer_score +=1

    elif computer_choice > player_choice:
        statusLabel.configure(text="\nYou lose")
        computer_score +=1

    elif player_choice > computer_choice:
        statusLabel.configure(text="\nYou win")
        player_score +=1

    player_score_label.configure(text=f"Your score: {player_score}")
    computer_score_label.configure(text=f"Computer's score: {computer_score}")

    if player_score == winLimit:
        statusLabel.configure(text="you won the whole thing!")
        rockButton.configure(state="disabled")
        paperButton.configure(state="disabled")
        scissorsButton.configure(state="disabled")
        resetButton.configure(state="normal")
    elif computer_score == winLimit:
        statusLabel.configure(text="you lost to a robot.")
        rockButton.configure(state="disabled")
        paperButton.configure(state="disabled")
        scissorsButton.configure(state="disabled")
        resetButton.configure(state="normal")

root.mainloop()