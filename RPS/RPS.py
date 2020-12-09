import random
#
from tkinter import Tk, Button, Label, PhotoImage, BOTTOM, Frame

# base gui initialization
root = Tk()
root.wm_title = "Rock Paper Scissors" #app title
root.geometry("600x600") #window size
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

startPage=Frame(root)
startPage.grid(row=0, column=0, sticky="nsew")

gamePage=Frame(root)
gamePage.grid(row=0, column=0, sticky="nsew")
startPage.tkraise() #function to stae which frame shows first

#grabbing images
rock = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/rock-100x120.png")
paper = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/paper-100x120.png")
scissors = PhotoImage(file="/Users/gervannastephens/Documents/GitHub/RockPaperScissors-with-Tkinter/RPS/scissors-100x120.png")

game_choices = [rock, paper, scissors]
style_button = ('Verdana', 14, 'bold')
status_font = ('Verdana', 13, 'bold')
label_font = ('Verdana', 13, 'underline')

welcome = Label(startPage, fg='blue', font='Verdana 24 bold', text= "Welcome to Rock Paper Scissors.")
welcome.pack(pady=30)

rules = '''The outcome of the game is determined by 3 simple rules:
\n1. Rock wins against scissors.
\n2. Scissors wins against paper.
\n3. Paper wins against rock.\n'''
info = Label(startPage, font='Verdana 14 bold', text=rules)
info.pack(pady=20)

winLimit = 0

def singleStart():
    global winLimit
    winLimit = 1
    gamePage.tkraise() #calls the game page when choice is made

def multigameStreak():
    global winLimit
    winLimit = 10
    gamePage.tkraise()

single=Button(startPage, font=style_button, fg= 'blue', text="SINGLE", command=singleStart)
single.pack(ipady=10, ipadx=10)
singleLabel=Label(startPage, font=label_font, text="Get to one point first and beat the robot!\n\n")
singleLabel.pack()

streak=Button(startPage, font=style_button, fg= 'blue', text="STREAK", command=multigameStreak)
streak.pack(ipady=10, ipadx=10)
streakLabel=Label(startPage, font=label_font, text="The first to ten points wins! Try to defeat the robot.")
streakLabel.pack()

#functions below are predefined ways to get rock, paper or scissors from the player
def pickedRock():
    player_choice= 0
    runGame(player_choice)

def pickedPaper():
    player_choice = 1
    runGame(player_choice)

def pickedScissors():
    player_choice = 2
    runGame(player_choice)

rps_label=Label(gamePage, font=style_button, text="Please choose:")
rps_label.pack()

rockButton = Button(gamePage, font=style_button, padx=2, pady=2, text="rock", command=pickedRock)
rockButton.pack(pady=1.2)

paperButton = Button(gamePage, font=style_button, padx=2, pady=2, text="paper", command=pickedPaper)
paperButton.pack(pady=1.2)

scissorsButton = Button(gamePage, font=style_button, padx=2, pady=2, text="scissors", command=pickedScissors)
scissorsButton.pack(pady=1.2)

player_choice_label = Label(gamePage) #shows what player chose
player_choice_label.pack()

computer_choice_label = Label(gamePage) #shows what computer chose
computer_choice_label.pack()

statusLabel = Label(gamePage) #shows who's currently winning/losing/draw
statusLabel.pack()

player_score_label = Label(gamePage) #players score 
player_score_label.pack()

computer_score_label = Label(gamePage) #computers score
computer_score_label.pack()

player_score = 0
computer_score = 0

#reset function with all the parts that need to be reset to start a new game
def resetGame():
    global player_score
    global computer_score

    startPage.tkraise()
    player_choice_label.configure(text="", image="")
    computer_choice_label.configure(text="", image="")
    statusLabel.configure(text="", image="", fg='black')
    player_score = 0
    computer_score = 0
    player_score_label.configure(text="")
    computer_score_label.configure(text="")
    rockButton.configure(state="normal")
    paperButton.configure(state="normal")
    scissorsButton.configure(state="normal")
    resetButton.configure(state="disabled")

#reset button disabled to start game, only clickable after single or streak ends
resetButton = Button(gamePage, font=style_button, text="Reset", command=resetGame, state="disabled")
resetButton.pack()

def exitGame():
    root.destroy()

exitButton = Button(root, font=style_button, text="Exit App", command=exitGame)
exitButton.grid(row=1, column=0)

#game logic
def runGame(player_choice):
    global player_score
    global computer_score

    player_choice_label.configure(font=status_font, text="You chose:\n", image=game_choices[player_choice], compound=BOTTOM)

    computer_choice = random.randint(0, 2)

    computer_choice_label.configure(font=status_font, text="The computer chose:\n", image=game_choices[computer_choice], compound=BOTTOM)

    if player_choice == computer_choice:
        statusLabel.configure(font=label_font, text="\nIt's a draw.")

    elif player_choice == 0 and computer_choice == 2:
        statusLabel.configure(font=label_font, text="\nYou win!")
        player_score +=1 #adds to score as rounds happen

    elif computer_choice == 0 and player_choice== 2:
        statusLabel.configure(font=label_font, text="\nYou lose...")
        computer_score +=1

    elif computer_choice > player_choice:
        statusLabel.configure(font=label_font, text="\nYou lose...")
        computer_score +=1

    elif player_choice > computer_choice:
        statusLabel.configure(font=label_font, text="\nYou win!")
        player_score +=1

    player_score_label.configure(font=status_font, text=f"\nYour score: {player_score}")
    computer_score_label.configure(font=status_font, text=f"\nComputer's score: {computer_score}")
    
    #conditionals that work with the single vs streak buttons
    if player_score == winLimit:
        statusLabel.configure(font=status_font, fg='blue', text="\nYou won the whole thing!")
        rockButton.configure(state="disabled")
        paperButton.configure(state="disabled")
        scissorsButton.configure(state="disabled")
        resetButton.configure(state="normal")
    
    elif computer_score == winLimit:
        statusLabel.configure(font=status_font, fg='red', text="\nYou lost to a robot...")
        rockButton.configure(state="disabled")
        paperButton.configure(state="disabled")
        scissorsButton.configure(state="disabled")
        resetButton.configure(state="normal")

root.mainloop() #runs the tkinter app loop