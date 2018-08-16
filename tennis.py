'''
Points ---> Games ----> Sets

'''

# Tennis Version 2
# Player 1 Information. 
from tkinter import *
from tkinter.ttk import *
p1Name = ""
p1Points = 0
p1Games = 0
p1Sets = 0
# Player 2 Information
p2Name = ""
p2Games = 0
p2Sets = 0
p2Points = 0
# Default amount of sets
maxSet = 3
# State of the game. 0 = Normal. 1 = Tie Breaker
gameState = 0
# Winner of the game. 1 = Player 1 and 2 = Player 2. -1 = Nobody
gameWinner = -1
def newGame(name1, name2):
   globals().update({
      'p1Name': name1,
      'p1Points': 0,
      'p1Games': 0,
      'p1Sets': 0,
      'p2Name': name2,
      'p2Games': 0,
      'p2Sets': 0
      })
# Add points based on playerID. 1 = Player 1 and 2 = Player 2
def addPoints(playerID):
   global p1Points, p2Points
   global p1Games, p2Games
   # Current temp score and the opposing player's score
   temp = 0
   tempGames = 0
   other = 0
   otherGames = 0
   if (playerID == 1):
      temp = p1Points
      tempGames = p1Games
      other = p2Points
      otherGames = p2Games
   elif (playerID == 2):
      temp == p2Points
      tempGames = p2Games
      other = p1Points
      otherGames = p1Games
   if (temp == 0 or temp == 15):
      temp+=15
   elif (temp == 30):
      temp+=10
   elif(temp == 40):
      if (other == 40):
         # Advantage Outcome
         temp = -1
      elif(other == -1):
         # Deuce Outcome
         temp = 40
         other = 40
      else:
         # Game Win Outcome
         temp = 0
         other = 0
         tempGames+=1
   elif(temp == -1):
      temp = 0
      other = 0
      tempGames+=1

   if (playerID == 1):
      print("Temp is " + str(temp))
      p1Points = temp
      p1Games = tempGames
      p2Points = other
      p2Games = otherGames
   elif (playerID == 2):
      p1Points = other
      p1Games = otherGames
      p2Points = temp
      p2Games = tempGames


# Update Sets and number crunch.
def updateGame():
   global p1Points, p2Points, p1Sets, p2Sets, p1Games, p2Games, maxSet
   if (p1Games>=6 and ((p1Games-p2Games) >= 2) and p1Games > p2Games):
      p1Sets+=1
      # Reset games
      p1Games = 0
      p2Games = 0
      # Reset points
      p1Points = 0
      p2Points = 0
      if (p1Sets == maxSet):
         #Game over. Player one wins.
         gameWinner = 1
   elif (p1Games == 6 and p2Games == 6):
      # Initiate Tie Breaker rules. 
      gameState = 1 # Set state to tiebreaker mode.
      if (p1Points>=7 and (p1Points - p2Points) >= 2):
         # Player one wins tiebreaker. Wins the game and +1 set. 
         p1Games = 0
         p1Points= 0
         p2Games = 0
         p2Points = 0
         p1Sets+=1
   elif(p2Games>=6 and ((p2Games-p1Games) >= 2) and p2Games > p1Games):
      p2Sets+=1
      #Reset Games
      p1Games = 0
      p2Games = 0
      # Reset points
      p1Points = 0
      p2Points = 0
      if (p2Sets == maxSet):
         # Game Over. Player Two wins.
         gameWinner = 2

def printStats():
   global p1Points, p2Points, p1Sets, p2Sets, p1Games, p2Games, p1Name, p2Name
   print(str(p1Sets) + ":" + str(p1Games) + ":" + str(p1Points) + ": " + p1Name)
   print(str(p2Sets) + ":" + str(p2Games) + ":" + str(p2Points) + ": " + p2Name)

def on_enter(e):
    newGameButton.configure(bg='green')
    print("WHY AREN'T YOU WORKING ")

def on_leave(e):
    newGameButton.configure(bg='SystemButtonFace')

root = Tk()
root.geometry("500x500")
root.title("Tennis program")
titleLabel = Label(root, text="Tennis", width=6, font=("bold", 20), anchor='n')
titleLabel.pack(pady=20)
newGameButton = Button(root, text="New Game", style="green/black.TLabel",width=8, bg='red', highlightbackground='white', activebackground='green',activeforeground='yellow',font=("bold", 20), anchor = 'c')
newGameButton.bind("<Enter>", on_enter)
newGameButton.bind("<Leave>", on_leave)
newGameButton.pack(pady=20)
#newGameButton.grid()
cmd = input(" DWQD")
if (int(cmd) == 1):
   newGameButton.configure(bg="red")
root.mainloop()

'''
while(True):
   cmd = int(input("Enter a command:\n1. New Game\n2. Player 1's point.\n3. Player 2's point\n"))
   if (cmd == 1):
      name1 = input("Enter Player 1's name ")
      name2 = input("Enter Player 2's name ")
      newGame(name1, name2)
   if (cmd == 2):
      if (gameState == 0):
         addPoints(1)
      #else: 
         # Tiebreaker. Increment points by one. 
   elif(cmd == 3):
      if (gameState == 0):
         addPoints(2)
      #else:
         # Tiebreaker. Increment points by one. 
   updateGame()
   printStats()
   print(p1Points)

'''
