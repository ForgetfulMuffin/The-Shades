#!/usr/bin/python

#==============
#INITIALISATION
#==============

import termios, sys
description = ''
difficulty = 6
Game = ""
def init(): # Mets en place les elements du jeu.
    global Game
    print "Choose your language / Choisissez votre langue"
    print "[1] Francais" 
    print "[2] English"
    language = input()

    if language == 1:
        import GameFR as Game
    else:
        import GameEN as Game
    global description, difficulty
    description, difficulty = Game.init()

def display(): # Affiche certains elements du jeu et le texte relatif a la derniere action effectuee
    global description, difficulty
    Game.display(description,difficulty)

def interact(): # Releve toute interaction du joueur.
    global description
    description = Game.getAction()

def run():
    global difficulty
    while 1: # Boucle de simulation.
        Game.checkHealth()
        Game.checkTime(difficulty)
	Game.checkXp()
        display()
        interact()

def main(): # Fonction principale
    init()
    run()

#=========
#EXECUTION
#=========
main()
