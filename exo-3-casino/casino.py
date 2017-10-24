#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

#### MODULES

import math
import random

#### SCRIPT
#Get the bid and the bet of user
userBid = -1
while(userBid < 0):
    userInputBid = input("\n Choissez votre mise : \n")
    try :
        userBid = int(userInputBid)
    except :
        print("erreur de saisie : ")
        userBid = -1

userBet = 0
while(userBet < 1 or userBet > 49):
    userInputBet = input ("\n Choisissez un chiffre entre 0 et 49 : \n")
    try :
        print("erreur de saisie : ")
        userBet = int(userInputBet)
    except :
        userBid = -1

#Get the random draw
draw = random.randrange(50)
print ("Et le résultat est : ", draw)

#Calculation of winnings
if userBet == draw :
    userWinnings = 4 * userBet
    print("Félicitations ! (Pile poil) Vous empochez : ", userWinnings)
elif userBet%2 == draw%2 :
    userWinnings = math.ceil(userBet  + (userBet / 2))
    print("Félicitations ! (Parité) Vous empochez : ", userWinnings)
else :
    print ("Dommage... Vous avez perdu...")
