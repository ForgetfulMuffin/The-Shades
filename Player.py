#Module Player

import random
#===========================================================
#INITIALISATION
#===========================================================
player={ 'name' : 'Bob','position' : (0,0) ,'maxHealth' : 0 , 'health' : 0 , 'power' : 0 , 'time' : 0, 'xp' : 0 , 'level' : 1 , 'inventory' : [] , 'equip' : [] }

def setName(): # Defini le nom du joueur
	player['name'] = raw_input()

def setMaxHealth(): # Defini la vie max du joueur
	player['maxHealth'] = 12 + random.randint(1,6) + random.randint(1,6)
	player['health'] = player['maxHealth']

def setPower():
	player['power'] = random.randint(1,6) + random.randint(1,6)

#===========================================================
#ACCESSEURS
#===========================================================

def getMaxHealth(): # Renvoie la vie max du joueur
	return player['maxHealth']

def getHealth(): # Renvoie la vie du joueur
	return player['health']

def getName(): # Renvoie le nom du joueur
	return player['name']

def getPosition(): # Renvoie la position du joueur
	return player['position']

def getTime(): # Renvoie le temps passe par le joueur
	return player['time']

def getPower(): # Renvoie la force du joueur
	return player["power"]

def getEquipModifier(): # Renvoie le bonus de force de l'objet equipe
	if len(player['equip']):
		return player['equip']['Modifier'] 
	else:
		return 0

def isEquip(): # Renvoie 0 si aucun objet n'est equipe et 1 si un objet est equipe
	return len(player["equip"])
 
def isItem(): # Renvoie le nombre d'objets dans l'inventaire
	return len(player["inventory"])

def getItem(index): # Renvoie l'objet n index de l'inventaire
	return player["inventory"][index]

def getItemName(index): # Renvoie le nom de l'objet no index de l'inventaire
	return player["inventory"][index]["name"]

def getItemList(): # Renvoie la liste des objets de l'inventaire avec un index (wxcvbn) 
	descript = ""
	for i in range(len(player["inventory"])) :
		descript += "("
		descript += str(i+1) + ") "
		descript += player["inventory"][i]["liste"]
	return descript

def getXp(): # Renvoie la quantite d'xp du joueur
	return player['xp']

def getLevel(): # Renvoie la quantite d'xp du joueur
	return player['level']

#=============================================
#MODIFICATEURS
#=============================================

def editMaxHealth(modifier):
	player['maxHealth'] += modifier


def editHealth(modifier): # Modifie la vie du joueur d'une valeur egale a "modifier"
	player['health'] += modifier

def setHealth(value): # Defini la vie du joueur
	player['health'] = value

def editPower(modifier):
	player['power'] += modifier

def editXp(modifier): # Modifie l'experience du joueur d'une valeur egale a "modifier"
	player['xp'] += modifier

def setXp(modifier): # Definit une valeur fixe pour l'xp du joueur
	player['xp'] = modifier

def editLevel(modifier): # Modifie le niveau du joueur d'une valeur egale a "modifier"
	player['level'] += modifier

def move(direction): # Modifie la position du joueur dans la direction souhaitee
	if direction=="north":
		player['position'] = (player['position'][0] - 1 , player['position'][1] )
	elif direction=="south":
		player['position'] = (player['position'][0] + 1 , player['position'][1] )
	elif direction=="east":
		player["position"] = (player['position'][0] , player['position'][1] + 1 )
	elif direction=="west":
		player['position'] = (player['position'][0], player['position'][1]-1)

def editTime(modifier): # Modifie le temps passe par le joueur de modifier
	player['time'] = player['time'] + modifier

def addItem(item): # Ajoute un objet a l'inventaire
	player['inventory'].append(item)

def removeItem(index): # Retire un objet de l'inventaire
	player['inventory'].pop(index)

def equip(item): # Equipe un objet
        if len(player['equip']) == 1 :
		player['equip'] = []
	player['equip'] = dict(item)


