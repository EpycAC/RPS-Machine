#File: Main.py
#python RPSMachine.py

#Imports Modules
import random
from numpy import random as npr
import numpy as np
#Imports Classes
from settings.config import settings
from data.dataControl import Controller
Controller.setUp()

#Sets the number of rounds
rounds = settings.rounds

#Sets the 3 values
options = ["Rock", "Paper", "Sizzors"]

#Defines the input function
def check():
    move = input("What was your move?: ")
    oMove = move.lower()
    if not(oMove == "r" or "p" or "s"):
        print("Invalid input")
        check()
    else:
        return oMove

#Loop in which the game is played in
pWins = 0
cWins = 0
for i in range(rounds):
    a = input("Press enter to continue:")
    output = npr.choice(options, p = Controller.appendProbabilities())
    print(output)
    move = check()
    o1 = list(output.lower())
    osimplified = o1[0]
    if (move == "p") and (output == "Rock"):
        pWins += 1
        print("You Won!")
    elif (move == "s") and (output == "Paper"):
        pWins += 1
        print("You Won!")
    elif (move == "r") and (output == "Sizzors"):
        pWins += 1
        print("You Won!")
    elif  move == osimplified:
        print("tie")
    else:
        cWins += 1
        print("You Lost")
    Controller.adjustProbabilities(move)

print('''OVERALL RESULTS:
---''')
if cWins > pWins:
    print("You Lost " + str(pWins) + " to " + str(cWins))
elif pWins > cWins:
    print("You Won! " + str(pWins) + " to " + str(cWins))
else:
    print("Draw")
