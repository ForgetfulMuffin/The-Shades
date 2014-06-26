#==============
#INITIALISATION
#==============

import Game
import termios, sys
description = ''
difficulty = 6
def init(): # Mets en place les elements du jeu.
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
