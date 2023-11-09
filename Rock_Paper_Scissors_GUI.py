import tkinter as tk
from random import choice
from PIL import ImageTk, Image

#Configuring window
window = tk.Tk()
window.title("Rock, Paper, Scissors")
window.geometry('1200x900')
window.configure(bg = 'white')

#Configuration of first window asking for amount of games to play
spin = tk.Spinbox(window, from_=1, to=100, width = 5, wrap=True)
spin.grid(column=1,row=0) 
lbl = tk.Label(window, text = 'How many games do you want to play:', font = ('Arial Bold', 11))
lbl.grid(column=0, row=0)
lbl.configure(bg = 'white')

#Image Configuration
Rock_picture = Image.open('Rock.jpg')
Scissors_picture = Image.open('Scissors.jpg')
Paper_picture = Image.open('paper.png')

size = (90, 90)
size2 = (125, 125)
Rock_adjust = Rock_picture.resize(size)
Scissors_adjust = Scissors_picture.resize(size)
Paper_adjust = Paper_picture.resize(size)

Rock_adjust2 = Rock_picture.resize(size2)
Scissors_adjust2 = Scissors_picture.resize(size2)
Paper_adjust2 = Paper_picture.resize(size2)

Rock_pic = ImageTk.PhotoImage(Rock_adjust)
Scissors_pic = ImageTk.PhotoImage(Scissors_adjust)
Paper_pic = ImageTk.PhotoImage(Paper_adjust)

Rock_pic2 = ImageTk.PhotoImage(Rock_adjust2)
Scissors_pic2 = ImageTk.PhotoImage(Scissors_adjust2)
Paper_pic2 = ImageTk.PhotoImage(Paper_adjust2)


#Games variables
score ={'computer': 0, 'player': 0, 'tie': 0}    #States score between computer and player
games_played=0                     #Keep track of amount of games played
game_count = None             #Value of how many games user wants to play


player_icon = tk.Label(window, text = "Player", bg = 'light blue', font = ('Arial Bold', 50))
computer_icon = tk.Label(window, text = 'Computer', bg = 'light blue', font = ('Arial Bold', 50))
win = tk.Label(window, bg = 'light blue')
pl = tk.Label(window)
com = tk.Label(window)
computer_score = tk.Label(window)
player_score = tk.Label(window)
tie_score = tk.Label(window)
transition = tk.Button(window, text = 'Next', bg = 'white', font = ('Times New Roman', 12))


#Function transforming the number of games input window to the games 
def clicked():
    global game_count
    lbl.destroy()
    game_count = int(spin.get())
    spin.destroy()
    btn.destroy()
    Rock.place(relx = 0.45, rely = 0.5, anchor = 'e')
    Paper.place(relx = 0.5, rely = 0.5, anchor = 'center')
    Scissors.place(relx = 0.55, rely = 0.5, anchor = 'w')
    player_icon.place(relx = 0, rely = 0.1, anchor = 'w')
    computer_icon.place(relx = 1, rely = 0.1, anchor = 'e')
    window.configure(bg = 'light blue')

#Configues the window based during for all games played
def player(choose, game_count):
    global games_played              #Keeps record of number of games played
    computer_choose = choice(['rock', 'paper', 'scissors'])
    winner = play(choose, computer_choose)            #Runs the game and determines the winner of the game
    setup(choose, computer_choose)
    score[winner]+=1
    if winner == 'tie':
        win.place(relx = 0.5, rely = 0.35, anchor = 'center')
        win.config(text = 'Tie', font= ('Times New Roman', 40))
    else:
        win.place(relx = 0.5, rely = 0.35, anchor = 'center')
        win.config(text = ' '.join([winner.capitalize(),'wins']), font = ('Times New Roman', 40))
    
    computer_score.place(relx = 0.5, rely = 0.65, anchor = 'center')
    player_score.place(relx = 0.5, rely = 0.75, anchor = 'center')
    tie_score.place(relx = 0.5, rely = 0.85, anchor = 'center')
    computer_score.config(text = ' '.join(['Computer:', str(score['computer'])]), bg = 'light blue', font = ('Times New Roman', 28))
    player_score.config(text = ' '.join(['Player:', str(score['player'])]), bg= 'light blue', font = ('Times New Roman', 28))
    tie_score.config(text = ' '.join(['Tie:', str(score['tie'])]), bg = 'light blue', font = ('Times New Roman', 28))
    games_played += 1
    quit_button.place(relx = 0.975, rely = 0.975, anchor = 'se')
    
    if games_played == game_count:
        Rock['state']=tk.DISABLED
        Paper['state']=tk.DISABLED
        Scissors['state']=tk.DISABLED
        transition.place(relx = 0.025, rely = 0.975, anchor = 'sw')
        transition.config(command = end)
        quit_button.destroy()
        

# Produces the result of the winner of player vs computer
def play(player_choice, computer_choice):
    winner = None

    if (computer_choice == 'rock' and player_choice == 'paper') or (computer_choice == 'paper' and player_choice == 'scissors') or (computer_choice == 'scissors' and player_choice == 'rock'):  #Win conditions for a player
        winner = 'player'
    elif (computer_choice == 'paper' and player_choice == 'rock') or (computer_choice == 'scissors' and player_choice == 'paper') or (computer_choice == 'rock' and player_choice == 'scissors'):  #Win conditions for the computer
        winner = 'computer' 
    elif computer_choice == player_choice:    #Conditions for a tie
        winner = 'tie'
    return winner

#Configues window based computer and player choices after every game
def setup(choose, compt):
    if choose == 'rock':
        pl.place(relx = 0.075, rely = 0.25, anchor = 'center')
        pl.config(image = Rock_pic2)
    elif choose == 'paper':
        pl.place(relx = 0.075, rely = 0.25, anchor = 'center')
        pl.config(image = Paper_pic2)
    elif choose == 'scissors':
       pl.place(relx = 0.075, rely = 0.25, anchor = 'center')
       pl.config(image = Scissors_pic2)
    if compt == 'rock':
        com.place(relx = 0.925, rely = 0.25, anchor = 'center')
        com.config(image = Rock_pic2)
    elif compt == 'paper':
        com.place(relx = 0.925, rely = 0.25, anchor = 'center')
        com.config(image = Paper_pic2)
    elif compt == 'scissors':
        com.place(relx = 0.925, rely = 0.25, anchor = 'center')
        com.config(image = Scissors_pic2)

#Displays the final screen displaying the winner of the tournament
def end():
    quit_button.destroy()
    transition.destroy()
    Rock.destroy()
    Paper.destroy()
    Scissors.destroy()
    player_icon.destroy()
    computer_icon.destroy()
    com.destroy()
    pl.destroy()
    win.destroy()
    window['bg']='light green'
    if score['computer']>score['player']:
        tk.Label(window, text = 'Winner: Computer', font = ('Arial Bold', 50), bg = 'light green').place(relx = 0.5, rely = 0.45, anchor = 'center')
    elif score['player']>score['computer']:
        tk.Label(window, text = 'Winner: Player', font = ('Arial Bold', 50), bg = 'light green').place(relx = 0.5, rely = 0.45, anchor = 'center')
    else:
        tk.Label(window, text = 'Draw', font = ('Arial Bold', 50), bg = 'light green').place(relx = 0.5, rely = 0.45, anchor = 'center')
    computer_score.config(bg = 'light green')
    player_score.config(bg= 'light green')
    tie_score.config(bg = 'light green')    
    leave.place(relx = 0.975, rely = 0.975, anchor = 'se')

#Button allowing user to submit their input amount of games to be played
btn = tk.Button(window, text='Enter', command = clicked)
btn.grid(column=2, row=0)
btn['bg']='white'

# Buttons allowing user to choose their input
Rock = tk.Button(window, image = Rock_pic, activebackground = 'grey',  command = lambda: player('rock', game_count))
Paper = tk.Button(window, image = Paper_pic, activebackground = 'white', command = lambda: player('paper', game_count))
Scissors = tk.Button(window, image = Scissors_pic, activebackground = 'red', command = lambda: player('scissors', game_count)) 

#Transitions user to go to final screen if they decided to play less games than initially decided 
quit_button = tk.Button(window, text = 'Quit', font = ('Times New Roman', 12), bg = 'white', command = end)

#Button allowing user to close the window
leave = tk.Button(window, text = 'Exit', bg = 'white', font = ('Times New Roman', 12), command = window.destroy)

window.mainloop()