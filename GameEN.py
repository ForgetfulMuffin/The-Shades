#==================================================================================
#INITIALISATION
#==================================================================================

import MapEN as Map
import Player
import Background
import select, tty, termios, sys, time, random, os
defaultTerminal = termios.tcgetattr(sys.stdin)
items = 0
pick = 0
throw = 0
use = 0
key = 0
levelUp = 100
visited = 1
def init(): # Defini les variables de depart
	global descript, myBackground
	myBackground=Background.create("backgroundEN","winEN","loseEN","menuEN","menu2EN")
	Background.show(myBackground,"menu")
	Player.setName()
	Player.setMaxHealth()
	Player.setPower()
	difficulty = setDifficulty()
	Map.generate(difficulty)
	descript = descript()
	tty.setcbreak(sys.stdin.fileno())
        Map.doppel(Player.getMaxHealth(),Player.getPower())
	return descript, difficulty

def setDifficulty():
	Background.show(myBackground,"menu2")
	difficulty = input()
	if isinstance(difficulty, int) and difficulty >= 6 and difficulty <= 100:
		return difficulty
	else :
		print "You must enter an iteger between 6 and 100."
		time.sleep(2)
		setDifficulty()	

#==================================================================================
#Accessories
#==================================================================================

def fact(n):
	if n < 2:
		return 1
	else :
		return n*(fact(n-1))

#==================================================================================
# Interaction
#==================================================================================

def isInput(): # Recupere les actions du clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def getAction(): # Traite les interactions clavier
	global items, pick, throw, use
	key = 0
	while 1:
		if isInput():
			key = sys.stdin.read(1)
		if key == '1' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),0)
			elif throw == 1:
				return throwItem(Player.getPosition(),0)
			elif use == 1:
				return useItem(0)
		elif key == '2' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),1)
			elif throw == 1:
				return throwItem(Player.getPosition(),1)
			elif use == 1:
				return useItem(1)
		elif key == '3' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),2)
			elif throw == 1:
				return throwItem(Player.getPosition(),2)
			elif use == 1:
				return useItem(2)
		elif key == '4' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),3)
			elif throw == 1:
				return throwItem(Player.getPosition(),3)
			elif use == 1:
				return useItem(3)
		elif key == '5' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),4)
			elif throw == 1:
				return throwItem(Player.getPosition(),4)
			elif use == 1:
				return useItem(4)
		elif key == '6' :
			if int(key) > items:
				return "This item doesn't exist!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),5)
			elif throw == 1:
				return throwItem(Player.getPosition(),5)
			elif use == 1:
				return useItem(5)
		elif key == 'w' :
			pick, throw, use = 0,0,0
			return move('north')
		elif key == 'a' :
			pick, throw, use = 0,0,0
			return move('west')
		elif key == 's' :
			pick, throw, use = 0,0,0
			return move('south')
		elif key == 'd' :
			pick, throw, use = 0,0,0
			return move('east')
		elif key == 'o' :
			pick, throw, use = 0,0,0
			return altDescript()
		elif key == 'p' :
			pick, throw, use = 0,0,0
			return pickList()
		elif key == 't' :
			pick, throw, use = 0,0,0
			return throwList()
		elif key == 'e' :
			pick, throw, use = 0,0,0
			return useList()
		elif key == 'f' :
			pick, throw, use = 0,0,0
			return attack()
		elif key == '\x1b' :
			exitGame()
			time.sleep(0.2)	
		elif key == 'c' :
			termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
			cheat = raw_input("Enter cheat code : ")
			tty.setcbreak(sys.stdin.fileno())
			if cheat == "doppel":
				Map.addDoppel(Player.getPosition())
				return "There is now a Doppelganger in front of you!"
			elif cheat == "pepperonipizza":
				Player.addItem({"name" : "a Pizza" , "rate" : 9 , "type" : 0 , "Modifier" : 100 , "liste" : "A Pepperoni Pizza ---- "})
				return "A Pepperoni Pizza materialises in your inventory!"
			elif cheat == "konami":
				while Player.getLevel()<10:
					Player.setXp(levelUp)
                        		checkXp()
				if Player.isItem() <= 5:
					Player.addItem({"name" : "the NES Zapper" , "rate" : 0 , "type" : 1 , "Modifier" : 10 , "liste" : "The NES Zapper --+10 "})
					return "KONAMI Levels you up to the maximum level and gives you NES Zapper!"
				else:
					return "KONAMI Levels you up to the maximum level!"
			else:
				return "Don't cheat if you don't know how to!"
					
#==================================================================================
#ACTIONS
#==================================================================================

def descript(): # Recupere la description de base de la zone active
	return  Map.getDescript(Player.getPosition())

def altDescript(): # Recupere la description avancee de la zone active
	return Map.getAltDescript(Player.getPosition())

def move(direction): # Deplace le joueur si possible
	global visited
	flee = random.randint(1,6)
	if Map.isMonster(Player.getPosition()) == 0 or flee == 6:
		answer = Map.check(Player.getPosition(),direction)
		if answer == 0:
			return 'There is a wall in this direction.'
		elif answer == 1 :
			Player.move(direction)
			Player.editTime(10)
			if Map.getVisited(Player.getPosition()) == 0:
				Map.setMonster(Player.getPosition(),Player.getLevel())
				Map.setVisited(Player.getPosition())
				visited += 1
			return Map.getDescript(Player.getPosition())
		else :
			win()
			exitGame()
	else:
		Player.editHealth(-1)
		Player.editTime(1)
		return "You opponent pulls you by the collar and punches you in the stomach. Fight for heaven's sake!"

def pickList(): #Renvoie la liste des objets ramassables
	global items, pick
	items = Map.isItem(Player.getPosition())
	if Map.isMonster(Player.getPosition()) == 0 :
		if items == 0:
			return "There aren't any items in this area."
		elif Player.isItem() == 6:
			return "Your inventory is already full."
		else:
			pick = 1
			return "Which item do you want to pick up? (Type in the corresponding number) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Map.getItemList(Player.getPosition())
	else :
		return "Trying to take an items guarded by an opponent is never a clever idea. "

def pickItem(position,index): #Ramasse un objet
	global pick
	pick = 0
	print "add"
	Player.addItem(Map.getItem(position,index))
	print "describe"
	descript = "You pick up " + Map.getItemName(position,index)
	print "remove"
	Map.removeItem(position,index)
	print "return"
	return descript

def throwList(): #Renvoie la liste des objets jetables
	global items, throw
	items = Player.isItem()
	if items == 0:
		return "Your inventory is empty."
	else:
		throw = 1
		return "Which item do you want to throw away? (Type in the corresponding number) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def throwItem(position,index): #Jette un objet
	global throw
	throw = 0
	Map.addItem(position,Player.getItem(index))
	descript = "You throw " + Player.getItemName(index) + " away."
	Player.removeItem(index)
	return descript

def useList(): #Renvoie la liste des objets utilisables
	global items, use
	items = Player.isItem()
	if items == 0:
	 return "Your inventory is empty."
	else:
		use = 1
		return "Which item do you want to use? (Type in the corresponding number) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def useItem(index): #Utilise un objet
	global use, levelUp
	use = 0
	item = Player.getItem(index)
	if item["type"] == 0 :
		Player.editHealth(item["Modifier"])
		descript = "You eat " + Player.getItemName(index)
		Player.removeItem(index)
	elif item["type"] == 1 :
		Player.equip(item)
		descript = "You equip " + Player.getItemName(index)
	elif item['type'] == 2 :
		for i in range (item['Modifier']):
			Player.setXp(levelUp)
			checkXp()
		descript = "You eat " + Player.getItemName(index)
		Player.removeItem(index)
	descript += "."
	return descript

def attack(): #Gestion du combat
	if Map.isMonster(Player.getPosition()) == 0:
		descript = "Tell me, who are you trying to fight? The walls perhaps?"
	else :
		playerPow = Player.getPower()
		monsterPow = Map.getMonsterPower(Player.getPosition())
		player1, player2, monster1, monster2 = random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)
		if Player.isEquip() == 1:
			equipPow = Player.getEquipModifier()
		else:
			equipPow = 0
		descript = "You both charge at the other."
		if playerPow+player1+player2+equipPow >= monsterPow+monster1+monster2:
			Map.editMonsterHealth(Player.getPosition(),-2)
			descript += "You hit your opponent."
		else:
			if random.randint(1,6) == 6:
				Player.editHealth(-2)
			else :
				Player.editHealth(-1)
			descript += "Your opponent hits you. "
		if Map.getMonsterHealth(Player.getPosition()) <= 0:
			descript += "THIS blow is deadly. It's body falls like a ragdoll and, a few seconds later, it disintegrates." 
			Player.editXp(Map.getMonsterXp(Player.getPosition()))
			Map.removeMonster(Player.getPosition())
	Player.editTime(1)
	return descript

def checkXp(): # Verifie si le joueur change de niveau)
	global levelUp
	if Player.getXp() >= levelUp :
		if Player.getLevel() < 10:
			Player.editLevel(1)
			Player.editMaxHealth(2)
			if Player.getLevel()%2 == 0:
				Player.editPower(1)
			Player.setXp(Player.getXp()-levelUp)
			levelUp += Player.getLevel()*100
			Map.doppel(Player.getMaxHealth(),Player.getPower()+Player.getEquipModifier())
		Player.setHealth(Player.getMaxHealth())		
			
#==================================================================================
#AFFICHAGE
#==================================================================================

def display(description,difficulty): # Affiche la description correspondant a la derniere action effectuee
	global visited
	Background.show(myBackground,"bg")
	description = description.split()
	descript = [""]
	word, line = 0, 0
	while word < len(description):
		if len(descript[line]) + len(description[word]) + 1 <= 27:
			descript[line] += " " + description[word]
			word += 1
		elif word < len(description):
			descript.append("")
			line +=1
	for line in range (len(descript)):
		sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (6+line, 10, descript[line]))
	sys.stdout.write("\033[1;34m")
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,68,Player.getName()))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,97,str(Player.getLevel())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,70,str(Player.getMaxHealth())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,97,str(Player.getPower()+Player.getEquipModifier())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (27,74,str(levelUp)))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,74,str(difficulty*difficulty*14)))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,97,str(difficulty*difficulty)))
        if Player.getXp() >= levelUp*80/100:
                sys.stdout.write("\033[1;32m")
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (26,74,str(Player.getXp())))
	if Player.getHealth() > Player.getMaxHealth()*20/100:
		sys.stdout.write("\033[1;32m")
	else:
		sys.stdout.write("\033[1;31m")
        sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,82,str(Player.getHealth())))
        if Player.getTime() < difficulty*difficulty*14*80/100:
                sys.stdout.write("\033[1;32m")
        else:
                sys.stdout.write("\033[1;31m")
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,74,str(Player.getTime())))
        if visited < difficulty*difficulty*80/100:
                sys.stdout.write("\033[1;32m")
        else:
                sys.stdout.write("\033[1;31m")
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,96,str(visited)))
	sys.stdout.flush()

#==================================================================================
#FIN DE PARTIE
#==================================================================================

def checkHealth(): # Verifie si le joueur est vivant
	if Player.getHealth()<= 0:
		lose(1)
		exitGame()
	elif Player.getHealth() > Player.getMaxHealth():
		Player.setHealth(Player.getMaxHealth())

def checkTime(difficulty): # Verifie si le joueur est considere comme perdu a jamais
	if (Player.getTime()>difficulty*14*difficulty):
		lose(0)
		exitGame()

def exitGame(): # Quitte le jeu en remettant les parametres par defaut
	global defaultTerminal
	sys.stdout.write("\033[0;37m")
	time.sleep(5)
	os.system("clear")
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
	sys.exit()

def win(): # Affiche l'ecran de victoire
	Background.show(myBackground,"win")	
  
def lose(cause): # Affiche l'ecran de victoire
	Background.show(myBackground,"lose")	
  
