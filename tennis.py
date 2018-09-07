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
#Current Server. 0 = Player 1, 1 = Player 2
currServer = 0
# State of the game. 0 = Normal. 1 = Tie Breaker
gameState = 0
# Winner of the game. 1 = Player 1 and 2 = Player 2. -1 = Nobody
gameWinner = -1
# Amount of faults committed. Resets and awards points every two faults committed by the same player.
faultAmount = 0
# Height and width of the GUI window respectively. 
height = 500
width = 915
# Minimum Padding which is a quarter of the window height.
MIN_PAD = height/4
last_five = ['0', '0', '0', '0', '0']
index = 0
root = tk.Tk()
root.title("Tennis Program")
root.geometry(str(width)+"x"+str(height))
scoreP1 = tk.StringVar()
scoreP2 = tk.StringVar()
currentServerString = tk.StringVar()
firstIndexRel = tk.StringVar()
secondIndexRel = tk.StringVar()
thirdIndexRel = tk.StringVar()
fourthIndexRel = tk.StringVar()
fifthIndexRel = tk.StringVar()
blueButton = tk.PhotoImage(file="Blue-Button.gif")
blueButtonDown = tk.PhotoImage(file="BlueButtonDown.gif")
greyButton = tk.PhotoImage(file="Grey-Button.gif")
greyButtonDown= tk.PhotoImage(file="greyButtonDown.gif")
redButton = tk.PhotoImage(file="Red-Button.gif")
redButtonDown = tk.PhotoImage(file="redButtonDown.gif")
homeButton = tk.PhotoImage(file="homeButton.gif")
ending1 = tk.StringVar()
ending2 = tk.StringVar()
p1PointsStringVar = tk.StringVar()
p1GamesStringVar = tk.StringVar()
p1SetsStringVar = tk.StringVar()

p2PointsStringVar = tk.StringVar()
p2GamesStringVar = tk.StringVar()
p2SetsStringVar = tk.StringVar()
currServerStringVar = tk.StringVar()
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

def swap_service():
   global currServer
   if (currServer == 0):
      currServer = 1
   elif (currServer == 1):
      currServer = 0

def addPoints(playerID):
   global p1Points, p2Points
   global p1Games, p2Games
   global index, last_five
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
         swap_service()
   elif(temp == -1):
      temp = 0
      other = 0
      tempGames+=1
      swap_service()

   if (playerID == 1):
      #print("Temp is " + str(temp))
      p1Points = temp
      p1Games = tempGames
      p2Points = other
      p2Games = otherGames
      last_five.insert(index, "P1")
   elif (playerID == 2):
      #print("Gave a point to P2")
      #print("Temp is " + str(temp))
      p1Points = other
      p1Games = otherGames
      p2Points = temp
      p2Games =  tempGames
      last_five.insert(index, "P2")
   #print("========addPoints========")
   #printStats()

def tiebreakAddPoints(playerID):
   global p1Points, p2Points
   global p1Games, p2Games
   global index, last_five
   # Current temp score and the opposing player's score
   if (playerID == 1):
      p1Points+=1
      #swap_service()
      last_five.insert(index, "P1")
   elif (playerID == 2):
      p2Points+=1
      #swap_service()
      last_five.insert(index, "P2")

   if ((p1Points + p2Points) % 2 == 0):
      swap_service()


# Update Sets and number crunch.
def updateGame():
   global p1Points, p2Points, p1Sets, p2Sets, p1Games, p2Games, maxSet, gameState, currServer, p1Name, p2Name, gameWinner
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
      print("EARNED A SET")
      if (p2Sets == maxSet):
         print("Won the game")
         # Game Over. Player Two wins.
         gameWinner = 2
   var1 = str(p1Points)
   var2 = str(p2Points)
   if (var1 == '-1'):
      var1='ADV'
   elif(var2 == '-1'):
      var2 = 'ADV'
   scoreP1.set(str(p1Sets) + ":" + str(p1Games) + ":" + str(var1))
   scoreP2.set(str(p2Sets) + ":" + str(p2Games) + ":" + str(var2))
   firstIndexRel.set(last_five[0])
   secondIndexRel.set(last_five[1])
   thirdIndexRel.set(last_five[2])
   fourthIndexRel.set(last_five[3])
   fifthIndexRel.set(last_five[4])

   p1PointsStringVar.set(str(var1))
   p1GamesStringVar.set(str(p1Games))
   p1SetsStringVar.set(str(p1Sets))

   p2PointsStringVar.set(str(var2))
   p2GamesStringVar.set(str(p2Games))
   p2SetsStringVar.set(str(p2Sets))
   
   #print("Temp serve is " + tempServe)
   print("p1Name is " + p1Name)
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



#root.configure(bg='#F08130')
root.configure(background="#ececec")
class App():
   newGameButton = tk.Button()
   # Frames that are going to be overlayed on top of the window
   startwindow = tk.Frame(root)
   startgame = tk.Frame(root)
   maingame = tk.Frame(root)
   winnerscreen = tk.Frame(root)
   # Temporary variables to hold names for GUI.
   name1 = tk.StringVar()
   name2 = tk.StringVar()
   winner = tk.StringVar()
   var = tk.IntVar()
   setsVar = tk.IntVar()
   var.set(1)
   setsVar.set(1)
   #scoreP1 = tk.StringVar()
   #scoreP2 = tk.StringVar()
   def on_enter(self, e):
      self.newGameButton.configure(image=blueButtonDown)
      self.newGameButton.image=blueButtonDown
      print("WHY AREN'T YOU WORKING ")

   def on_leave(self, e):
      self.newGameButton.configure(image=blueButton)

   def start_window(self):
      global blueButton
      # unpack other frames
      self.startgame.pack_forget()
      self.maingame.pack_forget()
      # pack start window
      self.startwindow.configure(background="#ececec")
      self.startwindow.pack()
      # Label all widgets and grid them
      titleLabel = tk.Label(self.startwindow, text="Tennis", width=6, font=("Verdana Regular", 36, "bold"), bg='#ececec', fg='#76838e', anchor='n')
      titleLabel.grid(row=0, column=0)
      newGameButton = tk.Button(self.startwindow, fg="red",text="New Game",font=("bold", 20 ), anchor = 'c', image=blueButton, compound=tk.CENTER,relief="flat", highlightthickness = 0, borderwidth = 0,command=self.start_game)
      #newGameButton.config(image=blueButton)
      newGameButton.grid(row=2, column=0, pady=50)

      helpButton = tk.Button(self.startwindow, text="Help", font=("Verdana", 20), anchor = 'c', image=greyButton, compound=tk.CENTER, relief="flat", highlightthickness = 0, borderwidth = 0)
      helpButton.grid(row=3, column=0, pady=0)

      quitButton = tk.Button(self.startwindow, text="Quit", font=("Verdana", 20), anchor = 'c', image=redButton, compound=tk.CENTER, relief="flat", highlightthickness = 0, borderwidth = 0, command=root.destroy)
      quitButton.grid(row=4, column=0, pady=50)
      newGameButton.bind("<Enter>", lambda e: newGameButton.configure(image=blueButtonDown))
      newGameButton.bind("<Leave>", lambda e: newGameButton.configure(image=blueButton))
      helpButton.bind("<Enter>", lambda e: helpButton.configure(image=greyButtonDown))
      helpButton.bind("<Leave>", lambda e: helpButton.configure(image=greyButton))
      quitButton.bind("<Enter>", lambda e: quitButton.configure(image=redButtonDown))
      quitButton.bind("<Leave>", lambda e: quitButton.configure(image=redButton))

   def start_game(self):
      # unpack any other frames
      self.startwindow.pack_forget()
      self.maingame.pack_forget()
      self.startgame.configure(background="#ececec")
      titleLabel = tk.Label(self.startgame, text="Setup", font=("Verdana", 30), bg='#ececec', fg='#76838e', anchor='n')
      titleLabel.grid(row=0, columnspan=3, pady=20)
      name1Label = tk.Label(self.startgame, text="Player1", font=("Verdana", 30), bg='#ececec', fg='#76838e', anchor='c')
      name2Label = tk.Label(self.startgame, text="Player2", font=("Verdana", 30), bg='#ececec', fg='#76838e', anchor='c')
      nameEntry1 = tk.Entry(self.startgame, textvariable=self.name1)
      nameEntry2 = tk.Entry(self.startgame, textvariable=self.name2)

      name1Label.grid(row=1, column=0)
      name2Label.grid(row=2, column=0, pady=20)
      nameEntry1.grid(row=1, column=1)
      nameEntry2.grid(row=2, column=1)
      serving1= tk.Radiobutton(self.startgame, text="Serving?", font=("Verdana", 15), bg='#ececec', variable=self.var, value=1)
      serving2 = tk.Radiobutton(self.startgame, text="Serving?", font=("Verdana", 15), bg='#ececec', variable=self.var, value=2)
      serving1.grid(row=1, column=2, padx=10)
      serving2.grid(row=2, column=2, padx=10)
      maxSetsLabel = tk.Label(self.startgame, text="Max Sets", font=("Verdana", 15), bg='#ececec')
      setsNum1Label = tk.Radiobutton(self.startgame, text="1 Set Game", font=("Verdana", 15), bg='#ececec', variable=self.setsVar, value=1)
      setsNum3Label = tk.Radiobutton(self.startgame, text="3 Set Game", font=("Verdana", 15), bg='#ececec', variable=self.setsVar, value=2)
      setsNum5Label = tk.Radiobutton(self.startgame, text="5 Set Game", font=("Verdana", 15), bg='#ececec', variable=self.setsVar, value=3)
      maxSetsLabel.grid(row=3, column=0)
      setsNum1Label.grid(row=3, column=1, padx=20)
      setsNum3Label.grid(row=4, column=1, pady=20)
      setsNum5Label.grid(row=5, column=1)
      startGameButton = tk.Button(self.startgame, text="Start", font=("bold", 20), anchor = 'c', bg="#ececec",  fg="#FFFFFF", image=blueButton, compound=tk.CENTER, command=self.background_setup)
      startGameButton.grid(row=6, column=1)
      '''
      # pack start game window
      #self.startgame = tk.Frame(root)
      # Assign all widgets and grid them
      titleLabel = tk.Label(self.startgame, text="Setup", font=("Verdana", 30, "bold"), fg="#FFFFFF",bg="#2980b9",anchor='n')
      titleLabel.grid(row=0, columnspan=4)
      name1Label = tk.Label(self.startgame, text= "Player 1: ", font=("Verdana", 20, "bold"), bg="#2980b9", fg="#FFFFFF")
      name2Label = tk.Label(self.startgame, text= "Player 2: ", font=("Verdana", 20, "bold"),  bg="#2980b9", fg="#FFFFFF")
      emptyLabel = tk.Label(self.startgame, width=3,  bg="#ececec")
      emptyLabel.grid(row=1, column=3)
      name1Label.grid(row=1, column=0, padx=10)
      name2Label.grid(row=2, column=0, padx=10)
      nameEntry1 = tk.Entry(self.startgame, textvariable=self.name1)
      nameEntry2 = tk.Entry(self.startgame, textvariable=self.name2)
      nameEntry1.grid(row=1, column=1, columnspan=2, pady = MIN_PAD/4)
      nameEntry2.grid(row=2, column=1, columnspan=2, pady = MIN_PAD/4)
      startGameButton = tk.Button(self.startgame, text="Start", font=("bold", 20), anchor = 'c', bg="#3498db",  fg="#FFFFFF", image=blueButton, compound=tk.CENTER, command=self.background_setup)
      startGameButton.grid(row=3, columnspan=4)
      '''
      self.startgame.pack()      

   def background_setup(self):
      global currServer, maxSet
      p1Name=self.name1.get()
      p2Name=self.name2.get()
      ending1.set(str(p1Name) + "'s point")
      ending2.set(str(p2Name) + "'s point")
      newGame()
      if (self.var==1):
         currServer = 0
      else:
         currServer = 1

      if (self.setsVar == 1):
         maxSet = 1
      elif (self.setsVar == 2):
         maxSet = 3
      elif (self.setsVar == 3):
         maxSet = 5
      updateGame()
      self.main_game()

   def update_stats(self, playerID = -1, faultOrNot = -1):
      global gameWinner
      print("game state is "+ str(gameState))
      global faultAmount, index
      print(last_five)
      if (faultOrNot != -1):
         faultAmount+=1
         print("Fault amount is " + str(faultAmount))
         if (faultAmount == 1):
            last_five.insert(index, "F")
            #index+=1
            #index%=5
         elif (faultAmount == 2):
            faultAmount = 0
            print("Resetting faultamount")
            print("Current server is " + str(currServer))
            if (currServer == 0 and gameState == 0):
               addPoints(2)
            elif (currServer == 0 and gameState == 1):
               tiebreakAddPoints(2)
            elif (currServer == 1 and gameState == 0):
               print("Adding points to player 0")
               addPoints(1)
            elif(currServer == 1 and gameState == 1):
               tiebreakAddPoints(1)

      print("Current server is " + currServerStringVar.get())
      if (playerID != -1):
         if (gameState == 0):
            addPoints(playerID)
         elif(gameState == 1):
            tiebreakAddPoints(playerID)
      updateGame()

      if (currServer == 0):
         currServerStringVar.set(self.name1.get())
         #print("Server is " + self.name1.get())
      else:
         currServerStringVar.set(self.name2.get())
      print("MAX SETS IS " + str(maxSet))
      print("GAME WINNER IS " + str(gameWinner))
      if (gameWinner != -1):
         print("THERE IS A GAME WINNER!")
         if (gameWinner == 1):
            self.winner.set(self.name1.get())
         elif (gameWinner == 2):
            self.winner.set(self.name2.get())
         self.winnerScreen()
      print("p2PointsStringVar is ", p2PointsStringVar.get())
      print("Inside update stats")
      print("===============")
      #self.main_game()

   def main_game(self):
      self.startgame.pack_forget()
      self.startwindow.pack_forget()
      self.maingame.configure(background="#ececec")
      titleLabel = tk.Label(self.maingame, text="Game", font=("Verdana", 36), fg="#76838e", bg="#ececec",anchor='c', )
      titleLabel.grid(row=0, columnspan=6, pady=20)
      player1TextLabel = tk.Label(self.maingame, textvariable=self.name1, font=("Verdana", 28), fg='#76838e', bg="#ececec", anchor='c')
      player2TextLabel = tk.Label(self.maingame, textvariable=self.name2, font=("Verdana", 28), fg='#76838e', bg="#ececec", anchor='c')
      player1TextLabel.grid(row=2, column=0, padx=18)
      player2TextLabel.grid(row=3, column=0, padx=18)
      #emptyLabel = tk.Label(self.maingame, anchor='c')
      #emptyLabel.grid(row=1, column=0, padx=20)
      playersTextLabel = tk.Label(self.maingame, text="Players", font=("Verdana", 20), fg='#76838e', bg="#ececec", anchor='c')
      playersTextLabel.grid(row=1, column=0)
      setsTextLabel = tk.Label(self.maingame, text="Sets", font=("Verdana", 14), fg='#76838e', bg="#ececec", anchor='c')
      gamesTextLabel = tk.Label(self.maingame, text="Games", font=("Verdana", 14), fg='#76838e', bg="#ececec", anchor='c')
      pointsTextLabel = tk.Label(self.maingame, text="Points", font=("Verdana", 14), fg='#76838e', bg="#ececec", anchor='c')
      setsTextLabel.grid(row=1, column=1)
      gamesTextLabel.grid(row=1, column=3, padx=10)
      pointsTextLabel.grid(row=1, column=5)

      setsLabelP1 = tk.Label(self.maingame, textvariable=p1SetsStringVar, font=("Verdana", 20),bg="#ececec")
      setsLabelP2 = tk.Label(self.maingame, textvariable=p2SetsStringVar, font=("Verdana", 20),bg="#ececec")
      gamesLabelP1 = tk.Label(self.maingame, textvariable=p1GamesStringVar, font=("Verdana", 20),bg="#ececec")
      gamesLabelP2 = tk.Label(self.maingame, textvariable=p2GamesStringVar, font=("Verdana", 20), bg="#ececec")
      pointsLabelP1 = tk.Label(self.maingame, textvariable=p1PointsStringVar, font=("Verdana", 20),bg="#ececec")
      pointsLabelP2 = tk.Label(self.maingame, textvariable=p2PointsStringVar, font=("Verdana", 20), bg="#ececec")

      colon1P1 = tk.Label(self.maingame, text=":", font=("Verdana", 20), bg="#ececec")
      colon2P1 = tk.Label(self.maingame, text=":", font=("Verdana", 20), bg="#ececec")
      colon1P2 = tk.Label(self.maingame, text=":", font=("Verdana", 20), bg="#ececec")
      colon2P2 = tk.Label(self.maingame, text=":", font=("Verdana", 20), bg="#ececec")

      colon1P1.grid(row=2, column=2)
      colon2P1.grid(row=2, column=4)
      colon1P2.grid(row=3, column=2, padx=10)
      colon2P2.grid(row=3, column=4, padx=10)

      setsLabelP1.grid(row=2, column=1)
      gamesLabelP1.grid(row=2, column=3, padx=10)
      pointsLabelP1.grid(row=2, column=5)

      setsLabelP2.grid(row=3, column=1, padx=10)
      gamesLabelP2.grid(row=3, column=3, padx=10)
      pointsLabelP2.grid(row=3, column=5)

      currentServerTextLabel = tk.Label(self.maingame, text="Current Server:", font=("Verdana", 20), bg="#ececec", fg='#76838e')
      serverPlayerLabel = tk.Label(self.maingame, width=10, textvariable=currServerStringVar, font=("Verdana", 20), bg="#ececec")

      currentServerTextLabel.grid(row=4, column=0)
      serverPlayerLabel.grid(row=4, column=1)

      scoreButtonP1 = tk.Button(self.maingame, text="Server's point", font=("Verdana", 20), anchor = 'c', image=blueButton, compound=tk.CENTER, relief="flat", highlightthickness = 0, borderwidth = 0, command= lambda: self.update_stats(1))
      scoreButtonP2 = tk.Button(self.maingame, text="Receiver's point", font=("Verdana", 20), anchor = 'c', image=blueButton, compound=tk.CENTER, relief="flat", highlightthickness = 0, borderwidth = 0, command=lambda: self.update_stats(2))
      faultButton = tk.Button(self.maingame, text="Server Fault", font=("Verdana", 20), anchor='c', image=blueButton, compound=tk.CENTER, relief="flat", highlightthickness = 0, borderwidth = 0, command=lambda: self.update_stats(-1, 0))
      faultButton.grid(row=7, column=0)
      scoreButtonP1.grid(row=5, column=0)
      scoreButtonP2.grid(row=6, column=0, pady=20)

      home = tk.Button(self.maingame, anchor='ne',bg="#ececec",image=homeButton, relief="flat", highlightthickness = 0, borderwidth = 0, command=lambda: self.start_window())
      home.grid(row=0, column=5)
      '''
      player1TextLabel = tk.Label(self.maingame, text="Player 1", font=("Verdana", 20), fg='#76838e', anchor='c')
      setsLabelP1 = tk.Label(self.maingame, textvariable=scoreP1, font=("Comic Sans MS", 20, "bold"))
      setsLabelP1.grid(row=1, column=0)
      setsLabelP2 = tk.Label(self.maingame, textvariable=scoreP2, font=("Comic Sans MS", 20, "bold"))
      setsLabelP2.grid(row=1, column=1)

      scoreLabelP1 = tk.Button(self.maingame, textvariable=ending1, font=("bold", 20), anchor = 'c', command=lambda : self.update_stats(1))
      scoreLabelP1.grid(row=2, column=0)
      scoreLabelP2 = tk.Button(self.maingame, textvariable=ending2, font=("bold", 20), anchor = 'c', command=lambda : self.update_stats(2))
      scoreLabelP2.grid(row=2, column=1, padx=0, pady=10)
      fault = tk.Button(self.maingame, text="Server Fault", font=("bold", 20), anchor='c', command=lambda : self.update_stats(-1, 0))
      fault.grid(row=3, column=1)
      currentServer = tk.Label(self.maingame, textvariable=currentServerString, font=("Comic Sans MS", 20, "bold"))
      #currentServer.grid(row=3, column=2, padx=10)
      firstIndex = tk.Label(self.maingame, textvariable=firstIndexRel, font=("Comic Sans MS", 20, "bold"))
      firstIndex.grid(row=4, column=0, padx=0)
      secondIndex = tk.Label(self.maingame, textvariable=secondIndexRel, font=("Comic Sans MS", 20, "bold"))
      thirdIndex = tk.Label(self.maingame, textvariable=thirdIndexRel, font=("Comic Sans MS", 20, "bold"))
      fourthIndex = tk.Label(self.maingame, textvariable=fourthIndexRel, font=("Comic Sans MS", 20, "bold"))
      fifthIndex = tk.Label(self.maingame, textvariable=fifthIndexRel, font=("Comic Sans MS", 20, "bold"))
      secondIndex.grid(row=4, column=1, padx=0)
      #thirdIndex.grid(row=4, column=2)
      #fourthIndex.grid(row=4,column=3)
      #fifthIndex.grid(row=5, column=4)
      '''
      self.maingame.pack()

   def winnerScreen(self):
      self.startgame.pack_forget()
      self.startwindow.pack_forget()
      self.maingame.pack_forget()
      self.winnerscreen.configure(background="#ececec")
      winnerText = tk.Label(self.winnerscreen)
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