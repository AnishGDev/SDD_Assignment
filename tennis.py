'''
Points ---> Games ----> Sets

'''

# Tennis Version 2
# Player 1 Information. 
import tkinter as tk
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

height = 500
width = 500
MIN_PAD = height/4
root = tk.Tk()
root.title("Tennis Program")
root.geometry(str(height)+"x"+str(width))

scoreP1 = tk.StringVar()
scoreP2 = tk.StringVar()
def newGame():
   globals().update({
      'p1Points': 0,
      'p1Games': 0,
      'p1Sets': 0,
      'p2Points': 0,
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
      temp = p2Points
      tempGames = p2Games
      other = p1Points
      otherGames = p1Games
      print("Assign player. Temp is " + str(temp))

   if (temp == 0 or temp == 15):
      print("Value of temp before " + str(temp))
      temp+=15
      #print("Increased Player's point by 15. It is now " + str(temp)) 
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
      #print("Temp is " + str(temp))
      p1Points = temp
      p1Games = tempGames
      p2Points = other
      p2Games = otherGames
   elif (playerID == 2):
      #print("Gave a point to P2")
      #print("Temp is " + str(temp))
      p1Points = other
      p1Games = otherGames
      p2Points = temp
      p2Games =  tempGames
   #print("========addPoints========")
   #printStats()

def tiebreakAddPoints(playerID):
   global p1Points, p2Points
   global p1Games, p2Games
   # Current temp score and the opposing player's score
   if (playerID == 1):
      p1Points+=1
   elif (playerID == 2):
      p2Points+=1


# Update Sets and number crunch.
def updateGame():
   global p1Points, p2Points, p1Sets, p2Sets, p1Games, p2Games, maxSet, gameState
   #print("Inside update. Temp is " + str(p2Points))
   #print("Inside update. Games is " + str(p2Games))
   if (p1Games>=6 and ((p1Games-p2Games) >= 2) and p1Games > p2Games):
      print("Whoa 1")
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
      print("whoa 2")
      # Initiate Tie Breaker rules. 
      gameState = 1 # Set state to tiebreaker mode.
      if (p1Points>=7 and (p1Points - p2Points) >= 2):
         # Player one wins tiebreaker. Wins the game and +1 set. 
         p1Games = 0
         p1Points= 0
         p2Games = 0
         p2Points = 0
         p1Sets+=1
         gameState=0
      elif (p2Points>=7 and (p2Points-p1Points)>=2):
         p1Games = 0
         p1Points= 0
         p2Games = 0
         p2Points = 0
         p2Sets+=1
         gameState=0
   elif(p2Games>=6 and ((p2Games-p1Games) >= 2) and p2Games > p1Games):
      print("whoa 3")
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
   scoreP1.set(str(p1Sets) + ":" + str(p1Games) + ":" + str(p1Points))
   scoreP2.set(str(p2Sets) + ":" + str(p2Games) + ":" + str(p2Points))
   printStats()

def printStats():
   global p1Points, p2Points, p1Sets, p2Sets, p1Games, p2Games, p1Name, p2Name
   print(str(p1Sets) + ":" + str(p1Games) + ":" + str(p1Points) + ": " + p1Name)
   print(str(p2Sets) + ":" + str(p2Games) + ":" + str(p2Points) + ": " + p2Name)


'''
class App():
   newGameButton = None

   def startWindow(self):
      root = Tk()
      root.geometry("500x500")
      root.title("Tennis program")
      root.configure(bg='#F08130')
      titleLabel = Label(root, text="Tennis", width=6, font=("MS Sans Serif", 20, "bold"),bg='#F0A130', anchor='n')
      titleLabel.pack(pady=20)
      self.newGameButton = Button(root, text="New Game",width=8, highlightbackground='#699A33',font=("bold", 20), anchor = 'c', command=)
      self.newGameButton.bind("<Enter>", self.on_enter)
      self.newGameButton.bind("<Leave>", self.on_leave)
      self.newGameButton.pack(pady=60)
      #newGameButton.grid()
      root.mainloop()

   def on_enter(self, e):
    self.newGameButton.configure(bg='black')
    self.newGameButton.configure(fg='red')
    print("WHY AREN'T YOU WORKING ")

   def on_leave(self, e):
    self.newGameButton.configure(bg='#F0C130')
'''


def on_enter(e):
    newGameButton.configure(bg='black')
    newGameButton.configure(fg='red')
    print("WHY AREN'T YOU WORKING ")

def on_leave(e):
    newGameButton.configure(bg='#F0C130')

#root.configure(bg='#F08130')
class App():
   newGameButton = None
   # Frames that are going to be overlayed on top of the window
   startwindow = tk.Frame(root)
   startgame = tk.Frame(root)
   maingame = tk.Frame(root)
   # Temporary variables to hold names for GUI.
   name1 = tk.StringVar()
   name2 = tk.StringVar()
   #scoreP1 = tk.StringVar()
   #scoreP2 = tk.StringVar()
   def on_enter(self, e):
      self.newGameButton.configure(bg='black')
      self.newGameButton.configure(fg='red')
      print("WHY AREN'T YOU WORKING ")

   def on_leave(self, e):
      self.newGameButton.configure(bg='#F0C130')

   def start_window(self):
      # unpack other frames
      self.startgame.pack_forget()
      # pack start window
      self.startwindow.pack()
      # Label all widgets and grid them
      titleLabel = tk.Label(self.startwindow, text="Tennis", width=6, font=("MS Sans Serif", 20, "bold"),bg='#F0A130', anchor='n')
      titleLabel.grid(row=0, column=0)
      newGameButton = tk.Button(self.startwindow, text="New Game", width=8, font=("bold", 20), anchor = 'c', command=self.start_game)
      newGameButton.grid(row=2, column=0, pady=MIN_PAD)
      newGameButton.bind("<Enter>", self.on_enter)
      newGameButton.bind("<Leave>", self.on_leave)

   def start_game(self):
      # unpack any other frames
      self.startwindow.pack_forget()
      # pack start game window
      #self.startgame = tk.Frame(root)
      # Assign all widgets and grid them
      titleLabel = tk.Label(self.startgame, text="Setup the game", font=("MS Sans Serif", 20, "bold"),bg='#F0A130', anchor='n')
      titleLabel.grid(row=0, columnspan=1)
      name1Label = tk.Label(self.startgame, text= "Player 1: ", font=("MS Sans Serif", 20, "bold"))
      name2Label = tk.Label(self.startgame, text= "Player 2: ", font=("MS Sans Serif", 20, "bold"))
      name1Label.grid(row=1, column=0)
      name2Label.grid(row=2, column=0)
      nameEntry1 = tk.Entry(self.startgame, textvariable=self.name1)
      nameEntry2 = tk.Entry(self.startgame, textvariable=self.name2)
      nameEntry1.grid(row=1, column=1, pady = MIN_PAD/2)
      nameEntry2.grid(row=2, column=1, pady = MIN_PAD/2)
      startGameButton = tk.Button(self.startgame, text="Start", width=8, font=("bold", 20), anchor = 'c', command=self.background_setup)
      startGameButton.grid(row=3, columnspan=1)
      self.startgame.pack()

   def background_setup(self):
      p1Name=self.name1
      p2Name=self.name2
      newGame()
      self.main_game()

   def update_stats(self, playerID):
      print("game state is "+ str(gameState))
      if (gameState == 0):
         addPoints(playerID)
      elif(gameState == 1):
         tiebreakAddPoints(playerID)
      updateGame()
      print("Inside update stats")
      print("===============")
      #self.main_game()

   def main_game(self):
      self.startgame.pack_forget()
      titleLabel = tk.Label(self.maingame, text="Game", font=("MS Sans Serif", 20, "bold"),bg='#F0A130', anchor='n')

      titleLabel.grid(row=0, column=0)
      setsLabelP1 = tk.Label(self.maingame, textvariable=scoreP1, font=("MS Sans Serif", 20, "bold"))
      setsLabelP1.grid(row=1, column=0)
      setsLabelP2 = tk.Label(self.maingame, textvariable=scoreP2, font=("MS Sans Serif", 20, "bold"))
      setsLabelP2.grid(row=1, column=1)

      scoreLabelP1 = tk.Button(self.maingame, text="Player 1's point", width=10, font=("bold", 20), anchor = 'c', command=lambda : self.update_stats(1))
      scoreLabelP1.grid(row=2, column=0)
      scoreLabelP2 = tk.Button(self.maingame, text="Player 2's point", font=("bold", 20), anchor = 'c', command=lambda : self.update_stats(2))
      scoreLabelP2.grid(row=2, column=1, padx=10)
      self.maingame.pack()

app = App()
app.start_window()
root.mainloop()

'''
while(True):
   cmd = int(input("Enter a command:\n1. New Game\n2. Player 1's point.\n3. Player 2's point\n"))
   if (cmd == 1):
      name1 = input("Enter Player 1's name ")
      name2 = input("Enter Player 2's name ")
      newGame()
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

