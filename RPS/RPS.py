import random
from tkinter import Tk, Button, Label, Text, PhotoImage, TOP, BOTTOM

root = Tk()
root.wm_title = "Rock Paper Scissors" #app title
root.geometry("600x600") #window size

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
    player = 0
    runGame(player)

def pickedPaper():
    player = 1
    runGame(player)

def pickedScissors():
    player = 2
    runGame(player)

rockButton = Button(root, font='Verdana 14 bold', text="rock", command=pickedRock)
rockButton.pack()

paperButton = Button(root, font='Verdana 14 bold', text="paper", command=pickedPaper)
paperButton.pack()

scissorsButton = Button(root, font='Verdana 14 bold', text="scissors", command=pickedScissors)
scissorsButton.pack()

#rock_img = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/rock.png")
player_choice_label = Label(root)
player_choice_label.pack()

computer_choice_label = Label(root)
computer_choice_label.pack()

statusLabel = Label(root)
statusLabel.pack()

def runGame(player):

    player_choice_label.configure(text="You chose: ", image=game_choices[player], compound=BOTTOM)

    #statusLabel.configure(text="") #clears after each play

    #statusLabel.configure("Player chose: ", (game_choices[player]))
    #statusLabel.configure(image=game_choices[player])

    computer = random.randint(0, 2)

    computer_choice_label.configure(text="The computer chose: ", image=game_choices[computer], compound=BOTTOM)

    #statusLabel.configure("Computer chose: " + (game_choices[computer]))

    if player == computer:
        statusLabel.configure(text="\nIt's a draw.")
    elif player == 0 and computer == 2:
        statusLabel.configure(text="\nYou win!")
    elif computer == 0 and player == 2:
        statusLabel.configure(text="\nYou lose...")
    elif computer > player:
        statusLabel.configure(text="\nYou lose")
    elif player > computer:
        statusLabel.configure(text="\nYou win")

root.mainloop()