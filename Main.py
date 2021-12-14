#File: Main.py
#Imports Modules
import random
from numpy import random as npr
import numpy as np
#from data.appendData import storage
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
    if oMove == "r":
        Controller.adjustProbabilities("r")
    elif oMove == "p":
        Controller.adjustProbabilities("p")
    elif oMove == "s":
        Controller.adjustProbabilities("s")
    else:
        print("Invalid input")
        check()

#Loop in which the game is played in
for i in range(rounds):
    check()
    output = npr.choice(options, p = Controller.appendProbabilities())
    print(output)
    print(Controller.appendProbabilities())
