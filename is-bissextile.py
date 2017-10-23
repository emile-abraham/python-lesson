#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

inputUser = input("Saisissez une année")
year = int(inputUser)
bissextile = False

if year % 400 :
    bissextile = True
elif year % 100 :
    bissextile = False
elif year % 4 :
    bissextile = True
else :
    bissextile = False

if bissextile :
    print("L'année saisie est bissextile")
else :
    print ("L'année saisie n'est pas bissextile")
