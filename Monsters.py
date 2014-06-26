import random

# Liste des monstres. Il est possible d'en rajouter en suivant le modele. ATTENTION: Le rapport rate (probabilite) / power (force) / health (vie) influe enormement sur la jouabilite.
monsters = (
    {"name" : "Une licorne rose touffue", "rate" : 1, "power" : 1, "health" : 1, "levels" : [1] , 'xp' : 10 },
    {"name" : "Un mendiant affame", "rate" : 3, "power" : 6, "health" : 6, "levels" : [1,2] , 'xp' : 50 },
    {"name" : "Un mendiant", "rate" : 4, "power" : 7, "health" : 6, "levels" : [1,2] , 'xp' : 50 },
    {"name" : "Un mendiant en colere", "rate" : 6, "power" :  7, "health" : 8, "levels" : [2,3] , 'xp' : 60 },
    {"name" : "Un chien enrage", "rate" : 7, "power" : 8, "health" : 8, "levels" : [2,3] , 'xp' : 60 },
    {"name" : "Un vieux kobold", "rate" : 7, "power" :  8, "health" : 10, "levels" : [3,4] , 'xp' : 70 },
    {"name" : "Un kobold", "rate" : 8, "power" :  8, "health" : 10, "levels" : [3,4] , 'xp' : 70 },
    {"name" : "Un Dude", "rate" : 10, "power" :  9, "health" : 10, "levels" : [4,5] , 'xp' : 80 },
    {"name" : "Un bandit manchot", "rate" : 9, "power" :  9, "health" : 12, "levels" : [4,5] , 'xp' : 80 },
    {"name" : "Un bandit cul-de-jatte", "rate" : 8, "power" : 9, "health" : 12, "levels" : [5,6] , 'xp' : 90 },
    {"name" : "Un assassin", "rate" : 7, "power" :  9, "health" : 14, "levels" : [5,6] , 'xp' : 90 },
    {"name" : "Un chef de gang", "rate" : 6, "power" :  10, "health" : 14, "levels" : [6,7] , 'xp' : 100 },
    {"name" : "Un vampire", "rate" : 6, "power" :  10, "health" : 14, "levels" : [7,8] , 'xp' : 110 },
    {"name" : "Un lama", "rate" : 5, "power" : 10, "health" : 10, "levels" : [7,8] , 'xp' :110 },
    {"name" : "Un loup-garou", "rate" : 5, "power" : 10, "health" : 14, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Un troll", "rate" : 5, "power" : 11, "health" : 14, "levels" : [8,9] , 'xp' : 120 },
    {"name" : "Lord helix", "rate" : 5, "power" : 12 , "health" : 14, "levels" : [9,10] , 'xp' : 130 },
    {"name" : "Un Alduin", "rate" : 3, "power" : 12, "health" : 16, "levels" : [9,10] , 'xp' : 130 },
    {"name" : "Une licorne rose invisible", "rate" : 1, "power" :  14, "health" : 20, "levels" : [10] , 'xp' : 150 } )

def checkList(): # Verifie que tous les elements de la liste sont bien parametres
    for i in range (len(monsters)):
        monsters[i]['name'] == str(monsters[i]['name'])
        if not ( isinstance(monsters[i]['rate'], int) and isinstance(monsters[i]['power'], int) and isinstance(monsters[i]['health'], int) and isinstance(monsters[i]['xp'], int)) :
            monsters.pop(i)
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

