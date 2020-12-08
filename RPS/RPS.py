import random
from tkinter import Tk, Button, Label, Text, PhotoImage, TOP, BOTTOM

# base gui initialization
root = Tk()
root.wm_title = "Rock Paper Scissors" #app title
root.geometry("600x600") #window size

# grabbing our images
rock = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/rock-100x120.png")

paper = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/paper-100x120.png")

scissors = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/scissors-100x120.png")


game_choices = [rock, paper, scissors]


welcome = Label(root, padx=10, pady=10, fg='blue', font='Verdana 24 bold', text= "Welcome to Rock Paper Scissors.")
welcome.pack()
rules = '''
The outcome of the game is determined by 3 simple rules:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
'''

def pickedRock():
    player_choice= 0
    runGame(player_choice)

def pickedPaper():
    player_choice = 1
    runGame(player_choice)

def pickedScissors():
    player_choice = 2
    runGame(player_choice)

rockButton = Button(root, font='Verdana 14 bold', text="rock", command=pickedRock)
rockButton.pack()

paperButton = Button(root, font='Verdana 14 bold', text="paper", command=pickedPaper)
paperButton.pack()

scissorsButton = Button(root, font='Verdana 14 bold', text="scissors", command=pickedScissors)
scissorsButton.pack()

player_choice_label = Label(root)
player_choice_label.pack()

computer_choice_label = Label(root)
computer_choice_label.pack()

statusLabel = Label(root)
statusLabel.pack()

player_score_label = Label(root)
player_score_label.pack()

computer_score_label = Label(root)
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

resetButton = Button(root, text="Reset", command=resetGame)
resetButton.pack()

def exitGame():
    root.destroy()

exitButton = Button(root, text="exit app", command=exitGame)
exitButton.pack()


def runGame(player_choice):

    global player_score
    global computer_score

    player_choice_label.configure(text="You chose: ", image=game_choices[player_choice], compound=BOTTOM)

    computer_choice = random.randint(0, 2)

    computer_choice_label.configure(text="The computer chose: ", image=game_choices[computer_choice], compound=BOTTOM)

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

    if player_score == 10:
        statusLabel.configure(text="you won the whole thing!")
        resetGame()
    elif computer_score == 10:
        statusLabel.configure(text="you lost to a robot.")
        resetGame()

    


root.mainloop()