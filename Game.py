#==================================================================================
#INITIALISATION
#==================================================================================

import Map
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
	myBackground=Background.create("background","victoire","defaite","menu","menu2")
	Background.show(myBackground,"menu")
	Player.setName()
	Player.setMaxHealth()
	Player.setPower()
	difficulty = setDifficulty()
	Map.generate(difficulty)
	descript = descript()
	tty.setcbreak(sys.stdin.fileno())
	return descript, difficulty

def setDifficulty():
	Background.show(myBackground,"menu2")
	difficulty = input()
	if isinstance(difficulty, int) and difficulty >= 6 and difficulty <= 100:
		return difficulty
	else :
		print "Vous devez fournir un entier compris entre 6 et 100 inclus."
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
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),0)
			elif throw == 1:
				return throwItem(Player.getPosition(),0)
			elif use == 1:
				return useItem(0)
		elif key == '2' :
			if int(key) > items:
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),1)
			elif throw == 1:
				return throwItem(Player.getPosition(),1)
			elif use == 1:
				return useItem(1)
		elif key == '3' :
			if int(key) > items:
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),2)
			elif throw == 1:
				return throwItem(Player.getPosition(),2)
			elif use == 1:
				return useItem(2)
		elif key == '4' :
			if int(key) > items:
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),3)
			elif throw == 1:
				return throwItem(Player.getPosition(),3)
			elif use == 1:
				return useItem(3)
		elif key == '5' :
			if int(key) > items:
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),4)
			elif throw == 1:
				return throwItem(Player.getPosition(),4)
			elif use == 1:
				return useItem(4)
		elif key == '6' :
			if int(key) > items:
				return "Cet objet n'existe pas!" 
			elif pick == 1:
				return pickItem(Player.getPosition(),5)
			elif throw == 1:
				return throwItem(Player.getPosition(),5)
			elif use == 1:
				return useItem(5)
		elif key == 'z' :
			pick, throw, use = 0,0,0
			return move('north')
		elif key == 'q' :
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
		elif key == 'r' :
			pick, throw, use = 0,0,0
			return pickList()
		elif key == 'j' :
			pick, throw, use = 0,0,0
			return throwList()
		elif key == 'e' :
			pick, throw, use = 0,0,0
			return useList()
		elif key == 'a' :
			pick, throw, use = 0,0,0
			return attack()
		elif key == '\x1b' :
			exitGame()
			time.sleep(0.2)	

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
			return 'Il y a un mur dans cette direction'
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
		return "Votre adversaire vous attrappe par le col et frappe a l'estomac. Battez-vous que diable!"

def pickList(): #Renvoie la liste des objets ramassables
	global items, pick
	items = Map.isItem(Player.getPosition())
	if Map.isMonster(Player.getPosition()) == 0 :
		if items == 0:
			return "Il n'y a pas d'objets dans cette zone."
		elif Player.isItem() == 6:
			return "Vous n'avez plus de place dans votre inventaire."
		else:
			pick = 1
			return "Quel objet voulez-vous ramasser? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Map.getItemList(Player.getPosition())
	else :
		return "Ramasser un objet qu'un adversaire garde n'est jamais une bonne idee. "

def pickItem(position,index): #Ramasse un objet
	global pick
	pick = 0
	print "add"
	Player.addItem(Map.getItem(position,index))
	print "describe"
	descript = "Vous ramassez " + Map.getItemName(position,index)
	print "remove"
	Map.removeItem(position,index)
	print "return"
	return descript

def throwList(): #Renvoie la liste des objets jetables
	global items, throw
	items = Player.isItem()
	if items == 0:
		return "Vous n'avez pas d'objets dans votre inventaire."
	else:
		throw = 1
		return "Quel objet voulez-vous jeter? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def throwItem(position,index): #Jette un objet
	global throw
	throw = 0
	Map.addItem(position,Player.getItem(index))
	descript = "Vous jetez " + Player.getItemName(index)
	Player.removeItem(index)
	return descript

def useList(): #Renvoie la liste des objets utilisables
	global items, use
	items = Player.isItem()
	if items == 0:
	 return "Vous n'avez pas d'objets dans votre inventaire."
	else:
		use = 1
		return "Quel objet voulez-vous utiliser? (Tapez le numero correspondant) ~~~~~~~~~~~~~~~~~~~~~~~~~~ " + Player.getItemList()

def useItem(index): #Utilise un objet
	global use, levelUp
	use = 0
	item = Player.getItem(index)
	if item["type"] == 0 :
		Player.editHealth(item["Modifier"])
		descript = "Vous mangez " + Player.getItemName(index)
		Player.removeItem(index)
	elif item["type"] == 1 :
		Player.equip(item)
		descript = "Vous equipez " + Player.getItemName(index)
	elif item['type'] == 2 :
		for i in range (item['Modifier']):
			Player.setXp(levelUp)
			checkXp()
		descript = "Vous mangez " + Player.getItemName(index)
		Player.removeItem(index)
	return descript

def attack(): #Gestion du combat
	if Map.isMonster(Player.getPosition()) == 0:
		descript = "Qui voulez-vous attaquer dites-moi? Les murs?"
	else :
		playerPow = Player.getPower()
		monsterPow = Map.getMonsterPower(Player.getPosition())
		player1, player2, monster1, monster2 = random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)
		if Player.isEquip() == 1:
			equipPow = Player.getEquipModifier()
		else:
			equipPow = 0
		descript = "Vous chargez tous les deux."
		if playerPow+player1+player2+equipPow >= monsterPow+monster1+monster2:
			Map.editMonsterHealth(Player.getPosition(),-2)
			descript += "Vous blessez votre adversaire."
		else:
			Player.editHealth(-2)
			descript += "Votre adversaire vous blesse. "
		if Map.getMonsterHealth(Player.getPosition()) <= 0:
			descript += "CE coup lui est fatal. Son corps tombe tel un pantin desarticule et, quelques secondes plus tard, il se desintegre." 
			Player.editXp(Map.getMonsterXp(Player.getPosition()))
			Map.removeMonster(Player.getPosition())
	Player.editTime(1)
	return descript

def checkXp(): # Verifie si le joueur change de niveau)
	global levelUp
	if Player.getXp() >= levelUp :
		Player.editLevel(1)
		Player.editMaxHealth(3)
		Player.editPower(1)
		Player.setHealth(Player.getMaxHealth())
		Player.setXp(Player.getXp()-levelUp)
		levelUp += Player.getLevel()*100
	return

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
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,67,Player.getName()))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (22,98,str(Player.getLevel())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,71,str(Player.getMaxHealth())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,83,str(Player.getHealth())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (23,97,str(Player.getPower()+Player.getEquipModifier())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,97,str(difficulty*difficulty)))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (24,76,str(Player.getTime())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,96,str(visited)))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (25,76,str(difficulty*difficulty*14)))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (26,74,str(Player.getXp())))
	sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (27,77,str(levelUp)))
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
	time.sleep(5)
	os.system("clear")
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, defaultTerminal)
	sys.exit()

def win(): # Affiche l'ecran de victoire
	Background.show(myBackground,"win")	
  
def lose(cause): # Affiche l'ecran de victoire
	Background.show(myBackground,"lose")	
  
