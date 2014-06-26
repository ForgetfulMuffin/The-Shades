import random

# Liste des objets. Il est possible d'en rajouter en suivant le modele. ATTENTION: Le rapport rate (probabilite) / Modifier (modificateur) influe enormement sur la jouabilite.
items = (
	{"name" : "une Fee" , "rate" : 4 , "type" : 0 , "Modifier" : 6 , "liste" : "une Fee-------------+6 "},
	{"name" : "un Coeur" , "rate" : 10 , "type" : 0 , "Modifier" : 1 , "liste" : "un Coeur------------+1 " },
	{"name" : "une Galette Saucisse" , "rate" : 9 , "type" : 0 , "Modifier" : 2 , "liste" : "une Galette Saucisse+2 "},
	{"name" : "des Abats" , "rate" : 10 , "type" : 0 , "Modifier" : 1 , "liste" : "des Abats-----------+1 "},
	{"name" : "des Jelly Babies" , "rate" : 7 , "type" : 0 , "Modifier" : 4 , "liste" : "des Jelly Babies------+4 "},
	{"name" : "une Fleur de Feu" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "une Fleur de Feu----+1 "},
	{"name" : "un Arc" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "un Arc--------------+1 "},
	{"name" : "une Arbalette" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "une Arbalette-------+3 "},
	{"name" : "un Morgenstern" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "un Morgenstern------+3 "},
	{"name" : "une Masse" , "rate" : 7 , "type" : 1 , "Modifier" : 2 , "liste" : "une Masse-----------+2 "},
	{"name" : "la Master Sword" , "rate" : 2 , "type" : 1 , "Modifier" : 6 , "liste" : "la Master Sword-----+6 "},
	{"name" : "un Lance-Pierre" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "un Lance-Pierre-----+1 "},
	{"name" : "une Catapulte" , "rate" : 3 , "type" : 1 , "Modifier" : 5 , "liste" : "une Catapulte-------+5 "},
	{"name" : "une Claymore" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "une Claymore--------+3 "},
	{"name" : "un Katana" , "rate" : 6 , "type" : 1 , "Modifier" : 2 , "liste" : "un Katana-----------+2 "},
	{"name" : "un Superbonbon" , "rate" : 6 , "type" : 2 , "Modifier" : 1 , "liste" : "un Superbonbon------+1 "},
	{"name" : "un Tromblon" , "rate" : 6 , "type" : 1 , "Modifier" : 2 , "liste" : "un Tromblon---------+2 "} )

def checkList(): # Verifie que tous les elements de la liste sont bien parametres
    for i in range (len(items)):
        items[i]['name'], items[i]['liste'] == str(items[i]['name']), str(items[i]['liste'])
        if not ( isinstance(items[i]['rate'], int) and isinstance(items[i]['type'], int) and isinstance(items[i]['Modifier'], int)):
            items.pop(i)

def addRandom(): # Renvoie un objet aleatoire de la liste
	maxRate = 0
	for i in range (len(items)):
		maxRate += items[i]["rate"]
	item = random.randint(1,maxRate)
	rate = items[0]["rate"]
	index = 0
	while rate < item:
		rate += items[index + 1]["rate"]
		index += 1
	return items[index]
