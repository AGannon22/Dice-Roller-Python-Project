#imports
from tkinter import *
from tkinter import ttk
import random 

# variables and functions
tempDice = "N/A"
diceOptionsList = ["d4","d6","d8","d10","d12","d20","d50","d100"]
diceList = []
rolledNumbers = []
def addDice():
    tempDice = diceDropdown.get()
    if len(diceList)<= 14:
        for x in diceOptionsList:
          if tempDice == x:
                diceList.append(tempDice)
                currentDiceText.config(text = diceList)
                errorText.config(text = "")
                diceDropdown.set('Pick a Die')
                break
          else:
            errorText.config(text = "Select a option and then click Add Dice")  
    else:
        errorText.config(text = "Too Many Dice!!")
temp = 0
def roll():
    rolledNumbers = []
    for y in diceList:
        rolledNumbers.append(random.randint(0,int(y.replace("d",""))))
    if len(rolledNumbers) == 0:
        reset()
        errorText.config(text = "Add Dice Before Rolling")
    else:
        rollText.config(text = "Rolled Numbers:" + str(rolledNumbers))

def reset():
    rolledNumbers = []
    diceList = []
    currentDiceText.config(text = "No Dice Added Yet")
    errorText.config(text = "")
    rollText.config(text = "Rolled Numbers:")
    
#Setup
mainWindow = Tk()
mainWindow.geometry("300x200")
title = Label(mainWindow,font = ('comic sans',14), fg = 'red', text = "Coolest Dice Roller Ever")
title.pack(padx = 10,pady=10)
frame = Frame(mainWindow)
diceDropdown = ttk.Combobox(frame,values = diceOptionsList,state = "readonly")
diceDropdown.set("Pick a die")
diceDropdown.pack()
addDiceButton = Button(frame, text = "Add Dice",command = addDice)
addDiceButton.pack(side = LEFT)
resetButton = Button(frame, text = "RESET",command = reset)
resetButton.pack(side = RIGHT)
currentDiceText = Label(mainWindow,text = "No Dice Added Yet")
currentDiceText.pack()
rollText = Label(mainWindow, text = 'Rolled Numbers:')
rollText.pack()
errorText = Label(mainWindow, text = "")
errorText.pack()
rollButton = Button(frame,text = "ROLL!",command = roll)
rollButton.pack(padx = 8, pady = 8)
frame.pack()

mainWindow.mainloop()