import random, MonstersFR as Monsters, ItemsFR as Items
map=[]
path=[]
visited=0
i=0
j=0

#===============================
# INITIALISATION
#===============================

def generate(size): # Fonction principale du module
    global i,j,visited
    createEmpty(size)
    visiting = random.randint(0,size - 1),random.randint(0,size - 1)
    i = visiting[0]
    j = visiting[1]
    path.append(visiting)
    visited = 1

    while visited < size*size :
        createMaze(size)
    addExits(size)
    setItems(size)

def createEmpty(size): # Cree une carte vide caree de size*size cases.
    for i in range (size):
        map.append([])
        for j in range (size):
            map[i].append({'items':[],'north':0,'south':0,'east':0,'west':0, "monster" : [], 'visited' : 0})

    
def createMaze(size): # Cree un labyrinthe parfait (bas de boucles, pas de zones innaccessibles)
    global visited,i,j
    chosen = 0
    n = 0
    s = 0
    e = 0
    w = 0
    dir = 0

    if i>0 :
        if map[i-1][j]['north']== 0 and map[i-1][j]['south']== 0 and map[i-1][j]['east']== 0 and map[i-1][j]['west']== 0 :
            n = 1
    if i<size - 1 :
        if map[i+1][j]['north']== 0 and map[i+1][j]['south']== 0 and map[i+1][j]['east']== 0 and map[i+1][j]['west']== 0 :
            s = 1
    if j>0 :
        if map[i][j-1]['north']== 0 and map[i][j-1]['south']== 0 and map[i][j-1]['east']== 0 and map[i][j-1]['west']== 0 :
            w = 1
    if j<size - 1 :
        if map[i][j+1]['north']== 0 and map[i][j+1]['south']== 0 and map[i][j+1]['east']== 0 and map[i][j+1]['west']== 0 :
            e = 1
    if n+s+e+w > 0:
        while chosen == 0:
            dir = random.randint(0,3)
            if dir == 0 and w == 1:
                chosen = 1
                map[i][j]['west'] = 1
                map[i][j-1]['east'] = 1
                j = j - 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'west'
            elif dir == 1 and e == 1:
                chosen = 1
                map[i][j]['east'] = 1
                map[i][j+1]['west'] = 1
                j = j + 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'east'
            elif dir == 2 and s == 1:
                chosen = 1
                map[i][j]['south'] = 1
                map[i+1][j]['north'] = 1
                i = i + 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'south'
            elif dir == 3 and n == 1:
                chosen = 1
                map[i][j]['north'] = 1
                map[i-1][j]['south'] = 1
                i = i - 1
                visiting = i,j
                path.append(visiting)
                visited = visited + 1
#                printMap()
#                print 'north'
    else:
#         print 'BACK'
         path.pop(len(path)-1)
         i = path[len(path) - 1][0]
         j = path[len(path) - 1][1]
    map[0][0]['visited'] = 1
def printMap(): # Affiche un visuel de la carte. Destine aux developpeurs. (^ signifie un mur au nord, _ au sud, = les deux et | a l'est ou a l'ouest en fonction du cote.)
    line=['','','','','','']
    for i in range (size): 
        for j in range (size):
            if map[i][j]['west']== 0:
                line[i]=line[i]+'|'
            else:
                line[i]=line[i]+' '
            if map[i][j]['north']== 0 and map [i][j]['south']== 0:
                line[i]=line[i]+'='
            elif map[i][j]['north']== 0:
                line[i]=line[i]+'^'
            elif map[i][j]['south']== 0:
                line[i]=line[i]+'_'
            else:
                line[i]=line[i]+' '
            if map[i][j]['east']== 0:
                line[i]=line[i]+'|'
            else:
                line[i]=line[i]+' '
        print line[i]

def addExits(size): # Ajoute des sorties (condition de victoire) au labyrinthe au sud et/ou a l'est
    quantum = random.randint(2,4)
    for exit in range(quantum):
        side = random.randint(0,1)
        if side == 0:
            map[size - 1][random.randint(0,size - 1)]['south'] = 2
        else:
            map[random.randint(0,size - 1)][size - 1]['east'] = 2

def setItems(size): # defini aleatoirement la presence d'objets dans chaque zone
    Items.checkList()
    for i in range (size):
        for j in range (size):
            if (i,j) != (0,0) :
                site = random.randint(0,4)
                if site >= 3:
                    map[i][j]["items"].append(Items.addRandom())

def setMonster(position, level):
	site = random.randint(0,4)
	if site >=3:
		map[position[0]][position[1]]["monster"] = dict(Monsters.addRandom(level))

def setVisited(position):
	map[position[0]][position[1]]["visited"] = 1

#========================================
# ACCESSEURS
#========================================

def check(position, direction): # Verifie la presence d'un mur dans la direction demandee et renvoie la reponse.
    answer = map[position[0]][position[1]][direction]
    return answer

def getDescript(position): # Genere la description de la zone dans laquelle se trouve le joueur et la renvoie.
    n = check(position,'north')
    s = check(position,'south')
    e = check(position,'east')
    w = check(position,'west')
    descript = 'La zone dans laquelle vous vous trouvez a'
    if n>0 and s+e+w>0 :
        descript = descript + " une sortie au nord"
        if s > 0 and e+w>0:
            descript = descript + ", une sortie au sud"
            if e>0 and w>0:
                descript = descript + ", une sortie a l'est et une sortie a l'ouest."
            elif e>0 and w==0:
                descript = descript + " et une sortie a l'est."
            else :
                descript = descript + " et une sortie a l'ouest."
        elif s>0 :
            descript = descript + " et une sortie au sud."
        elif e>0 and w>0:
            descript = descript + ", une sortie a l'est et une sortie a l'ouest."
        elif e>0 and w==0:
            descript = descript + " et une sortie a l'est."
        else:
            descript = descript + " et une sortie a l'ouest."
    elif n>0:
        descript = descript + " une sortie au nord."
    elif s > 0 and e+w>0:
        descript = descript + " une sortie au sud"
        if e>0 and w>0:
            descript = descript + ", une sortie a l'est et une sortie a l'ouest."
        elif e>0 and w==0:
            descript = descript + " et une sortie a l'est."
        else:
            descript = descript + " et une sortie a l'ouest."
    elif s>0:
        descript = descript + " une sortie au sud."
    elif e>0 and w>0:
        descript = descript + " une sortie a l'est et une sortie a l'ouest."
    elif e>0 and w==0:
        descript = descript + " une sortie a l'est."
    else:
        descript = descript + " une sortie a l'ouest."
    if len(map[position[0]][position[1]]["monster"]) != 0:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~ " + map[position[0]][position[1]]["monster"]["name"] + " sauvage vous attaque! Il faut vous battre!"
    return descript

def getAltDescript(position): # Ajoute quelques informations a la description de base
    descript = getDescript(position)
    s = check(position,'south')
    e = check(position,'east')
    if s == 2:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ La sortie sud est particulierement lumineuse."
    if e == 2:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ La sortie est est particulierement lumineuse."
    list = map[position[0]][position[1]]["items"]
    if len(list) > 0:
        descript += " ~~~~~~~~~~~~~~~~~~~~~~~~~ Au sol, vous voyez "
        for i in range (len(list)):
            descript += list[i]["name"]
            if len(list) - i ==1:
                descript += "."
            elif len(list) - i == 2:
                descript += " et "
            else:
                descript += ", "
    return descript

def isItem(position): # Renvoie le nombre d'objets dans la zone.
    return len(map[position[0]][position[1]]["items"])

def getItemList(position): # Renvoie la liste d'objets dans la zone et leur donne un index (wxcvbn) 
    descript = ""
    for i in range(len(map[position[0]][position[1]]["items"])) :
        descript += "("
        descript += str(i+1) + ") "
        descript += map[position[0]][position[1]]["items"][i]["liste"]
    return descript

def getItem(position, index): # Renvoie l'objet n^index de la zone
    return map[position[0]][position[1]]["items"][index]

def getItemName(position, index): # Renvoie le nom de l'objet n^index de la zone
    return map[position[0]][position[1]]["items"][index]["name"]

def isMonster(position): # Renvoie le nombre de monstre de la zone
    return len(map[position[0]][position[1]]["monster"])

def getMonsterHealth(position): # Renvoie la vie du monstre de la zone
    return map[position[0]][position[1]]["monster"]["health"]

def getMonsterXp(position): # Renvoie l'experienceque donne le monstre de la zone
    return map[position[0]][position[1]]["monster"]["xp"]

def getMonsterPower(position): # Renvoie la force du monstre de la zone
    return map[position[0]][position[1]]["monster"]["power"]

def getVisited(position): # Renvoie si la zone a deja ete visitee
    return map[position[0]][position[1]]["visited"]

#==================================
# MODIFICATEURS
#==================================

def doppel(health,power):
	Monsters.doppel(health,power)

def addItem(position,item): # ajoute un objet a une zone
    map[position[0]][position[1]]['items'].append(item)            

def removeItem(position,index): # retire un objet a une zone
    map[position[0]][position[1]]['items'].pop(index)            


def editMonsterHealth(position, modifier): # Modifie la valeur de la vie du monstre de la zone
    map[position[0]][position[1]]["monster"]["health"] += modifier

def removeMonster(position): # Retire le monstre de la zone
	map[position[0]][position[1]]["monster"]=[]

def addDoppel(position):
	map[position[0]][position[1]]["monster"]=Monsters.getDoppel()
