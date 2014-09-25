import random

# Liste des monstres. Il est possible d'en rajouter en suivant le modele. ATTENTION: Le rapport rate (probabilite) / power (force) / health (vie) influe enormement sur la jouabilite.
monsters = (
    {"name" : "Une Licorne Rose Touffue", "rate" : 1, "power" : 1, "health" : 1, "levels" : [1] , 'xp' : 10 },
    {"name" : "Un Rat", "rate" : 2, "power" : 4, "health" : 4, "levels" : [1] , 'xp' : 30 },
    {"name" : "Un Gobelin", "rate" : 3, "power" : 5, "health" : 6, "levels" : [1,2] , 'xp' : 40 },
    {"name" : "Un Mendiant Affame", "rate" : 3, "power" : 6, "health" : 6, "levels" : [1,2] , 'xp' : 50 },
    {"name" : "Un Mendiant", "rate" : 4, "power" : 7, "health" : 6, "levels" : [1,2] , 'xp' : 50 },
    {"name" : "Un Mendiant en Colere", "rate" : 6, "power" :  7, "health" : 8, "levels" : [2,3] , 'xp' : 60 },
    {"name" : "Un Chien Enrage", "rate" : 7, "power" : 8, "health" : 8, "levels" : [2,3] , 'xp' : 60 },
    {"name" : "Un Octorok", "rate" : 9, "power" : 7, "health" : 8, "levels" : [2,3,4] , 'xp' : 60 },
    {"name" : "Un Squelette", "rate" : 6, "power" : 9, "health" : 8, "levels" : [3,4] , 'xp' : 70 },
    {"name" : "Un Vieux Kobold", "rate" : 7, "power" :  8, "health" : 10, "levels" : [3,4] , 'xp' : 70 },
    {"name" : "Un Kobold", "rate" : 8, "power" :  8, "health" : 10, "levels" : [3,4] , 'xp' : 70 },
    {"name" : "Un Dude", "rate" : 10, "power" :  9, "health" : 10, "levels" : [4,5] , 'xp' : 80 },
    {"name" : "Un Orc", "rate" : 8, "power" :  9, "health" : 10, "levels" : [4,5] , 'xp' : 80 },
    {"name" : "Un Bandit Manchot", "rate" : 9, "power" :  9, "health" : 12, "levels" : [4,5] , 'xp' : 80 },
    {"name" : "Un Bandit Cul-De-Jatte", "rate" : 8, "power" : 9, "health" : 12, "levels" : [5,6] , 'xp' : 90 },
    {"name" : "Un Assassin", "rate" : 7, "power" :  9, "health" : 14, "levels" : [5,6] , 'xp' : 90 },
    {"name" : "Un Chef De Gang", "rate" : 6, "power" :  10, "health" : 14, "levels" : [6,7] , 'xp' : 100 },
    {"name" : "Un Vampire", "rate" : 6, "power" :  10, "health" : 14, "levels" : [7,8] , 'xp' : 110 },
    {"name" : "Un Lama", "rate" : 5, "power" : 10, "health" : 10, "levels" : [7,8] , 'xp' :110 },
    {"name" : "Un Loup-Garou", "rate" : 5, "power" : 10, "health" : 14, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Un Troll", "rate" : 5, "power" : 11, "health" : 14, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Un Ange Pleureur", "rate" : 5, "power" : 11, "health" : 14, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Un Detraqueur", "rate" : 5, "power" : 10, "health" : 16, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Lord Helix", "rate" : 5, "power" : 12 , "health" : 14, "levels" : [9,10] , 'xp' : 130 },
    {"name" : "Un Alduin", "rate" : 3, "power" : 12, "health" : 16, "levels" : [9,10] , 'xp' : 130 },
    {"name" : "Un Balrog", "rate" : 3, "power" :  12, "health" : 20, "levels" : [10] , 'xp' : 130 },
    {"name" : "Une Licorne Rose Invisible", "rate" : 1, "power" :  14, "health" : 20, "levels" : [10] , 'xp' : 150 }, 
    {"name" : "Un Doopelganger", "rate" : 1, "power" :  1, "health" : 1, "levels" : [1,2,3,4,5,6,7,8,9,10] , 'xp' : 150 } )

def checkList(): # Verifie que tous les elements de la liste sont bien parametres
    for i in range (len(monsters)):
        monsters[i]['name'] == str(monsters[i]['name'])
        if not ( isinstance(monsters[i]['rate'], int) and isinstance(monsters[i]['power'], int) and isinstance(monsters[i]['health'], int) and isinstance(monsters[i]['xp'], int)) :
            monsters.pop(i)

def doppel(health,power):
	monsters[len(monsters)-1]['power'] = power
	monsters[len(monsters)-1]['health'] = health

def addRandom(level): # Renvoie un monstre aleatoire de la liste
    selection = []
    for i in range (len(monsters)):
        for j in range (len(monsters[i]['levels'])):
		if monsters[i]['levels'][j] == level:
			selection.append(monsters[i])   
    rate = selection[0]["rate"]
    maxRate = 0
    for i in range (len(selection)):
        maxRate += selection[i]["rate"]
    monster = random.randint(1,maxRate)
    index = 0
    while rate < monster:
        rate += selection[index + 1]["rate"] 
        index += 1
    return selection[index]

def getDoppel():
	return monsters[len(monsters)-1]
