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
    move = input("Opponents move: ")
    oMove = move.lower()
    if not(oMove == "r" or "p" or "s"):
        print("Invalid input")
        check()
    else:
        return oMove

#Loop in which the game is played in
for i in range(rounds):
    move = check()
    output = npr.choice(options, p = Controller.appendProbabilities())
    print(output)
    print(Controller.adjustProbabilities(move))
