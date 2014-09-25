import random

# Liste des objets. Il est possible d'en rajouter en suivant le modele. ATTENTION: Le rapport rate (probabilite) / Modifier (modificateur) influe enormement sur la jouabilite.
items = (
	{"name" : "a Fairy" , "rate" : 4 , "type" : 0 , "Modifier" : 6 , "liste" : "A Fairy-------------+6 "},
	{"name" : "a Heart" , "rate" : 10 , "type" : 0 , "Modifier" : 1 , "liste" : "A Heart-------------+1 " },
	{"name" : "a Sausage Roll" , "rate" : 9 , "type" : 0 , "Modifier" : 2 , "liste" : "A Sausage Roll------+2 "},
	{"name" : "a Chocolate Frog" , "rate" : 6 , "type" : 0 , "Modifier" : 3 , "liste" : "A Chocolate Frog----+3 "},
	{"name" : "some Innards" , "rate" : 10 , "type" : 0 , "Modifier" : 1 , "liste" : "Some Innards--------+1 "},
	{"name" : "some Jelly Babies" , "rate" : 7 , "type" : 0 , "Modifier" : 4 , "liste" : "Some Jelly Babies---+4 "},
	{"name" : "a Fire Flower" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "A Fire Flower-------+1 "},
	{"name" : "a Bow" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "A Bow---------------+1 "},
	{"name" : "a Crossbow" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "A Crossbow----------+3 "},
	{"name" : "a Morningstar" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "A Morningstar-------+3 "},
	{"name" : "a Mace" , "rate" : 7 , "type" : 1 , "Modifier" : 2 , "liste" : "A Mace--------------+2 "},
	{"name" : "the Master Sword" , "rate" : 2 , "type" : 1 , "Modifier" : 6 , "liste" : "The Master Sword----+6 "},
	{"name" : "the BFG 9000" , "rate" : 1 , "type" : 1 , "Modifier" : 9 , "liste" : "The BFG 900--------+9 "},
	{"name" : "a Slingshot" , "rate" : 7 , "type" : 1 , "Modifier" : 1 , "liste" : "A Slingshot---------+1 "},
	{"name" : "a Catapult" , "rate" : 3 , "type" : 1 , "Modifier" : 5 , "liste" : "A Catapult----------+5 "},
	{"name" : "a Claymore" , "rate" : 5 , "type" : 1 , "Modifier" : 3 , "liste" : "A Claymore----------+3 "},
	{"name" : "a Katana" , "rate" : 6 , "type" : 1 , "Modifier" : 2 , "liste" : "A Katana------------+2 "},
	{"name" : "a Rare Candy" , "rate" : 6 , "type" : 2 , "Modifier" : 1 , "liste" : "A Rare Candy--------+1 "},
	{"name" : "a Ham" , "rate" : 1 , "type" : 2 , "Modifier" : 2 , "liste" : "A Ham---------------+2 "},
	{"name" : "an Old Musket" , "rate" : 6 , "type" : 1 , "Modifier" : 2 , "liste" : "An old Musket-------+2 "} )

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
