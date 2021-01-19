import random
random.randint(1,10)


#Hero classes


class Flynn(object):
    health = 10
    attack = 10
    defense = 17
    melee = 5
    gold = 25
    luck = 2
    trianium = 1
    name = "Flynn"

class Cecily(object):
    health = 10
    attack = 15
    defense = 15
    melee = 4
    gold = 30
    trianium = 0
    luck = 3
    name = "Cecily"

class Rob(object):
    health = 10
    attack = 10
    defense = 20
    melee = 8
    gold = 15
    trianium = 0
    luck = 3
    name = "Rob"
   
#Enemy classes
    

class Morlock(object): 
    health = 5
    attack = 3
    intro = "TIK...PAU...!"
    defense = 15
    melee = 2
    gold = 0
    trianium = 0
    rarity = 1
    name = "Morlock"


class Outlaw (object):
    health = 8
    intro = "C'MON, YELLOWBELLY!"
    attack = 8
    defense = 20
    poison = 0
    gold = 200
    trianium = 0
    rarity = 2
    name = "Outlaw"



class Everlasting(object):
    health = 99
    attack = 1
    intro = "Go ahead, I'll let you take the first shot..."
    defense = 999
    melee = 10
    gold = 10000
    trianium = 2
    rarity = 2
    name = "Everlasting"


class Scavenger(object):
    health = 3
    attack = 3
    defense = 15
    melee = 0
    gold = 2
    trianium = 0
    rarity = 1
    name = "Scavenger"


class Martian(object):
    health = 20
    attack = 150
    intro = "ULLA!"
    defense = 150
    melee = 25
    gold = 0
    trianium = 1
    rarity = 3
    name = "Martian"

class Lamanian(object):
    health = 10
    attack = 3
    defense = 15
    melee = 0
    gold = 25
    trianium = 0
    rarity = 2
    name = "Lamanian"

class Kylebot(object):
    health = 10
    attack = 10
    intro = "You are in violation of order 802-701. Please remain still for immediate deactivation."
    defense = 25
    melee = 1
    gold = 20
    trianium = 1
    rarity = 2
    name = "Kylebot"

class Uranium(object): 
    health = 30
    attack = 50
    intro = "NIIIIIIIIIICE!!!!!" 
    defense = 1500
    melee = 50
    gold = 10000000
    trianium = 5
    rarity = 3
    name = "Uranium"

class lamanian_militant(object):
    health = 15
    attack = 20
    intro = "STOP RESISTING!"
    defense = 55
    melee = 0
    gold = 200
    trianium = 1
    rarity = 2
    name = "lamanian militant"

class coyote(object):
    health = 15
    attack = 6
    intro = "HOOOOWWWWWWL!!!!!"
    defense = 5
    melee = 0
    gold = 0
    trianium = 0
    rarity = 1
    name = "coyote"

class manna_addict(object):
    health = 10
    attack = 2
    intro = "Think I know where I'm gettin' my next hit!"
    defense = 5
    melee = 2
    gold = 2
    trianium = 0
    rarity = 1
    name = "manna_addict"

class Rattlesnake (object): 
    health = 3
    attack = 3
    intro = "HISSSSSSSS"
    defense = 15
    melee = 75
    gold = 0
    trianium = 0
    rarity = 1
    name = "Rattlesnake"

class Coelophysis(object):
    health = 50
    attack = 8
    intro = "*bird noises*"
    defense = 15
    melee = 3
    gold = 0
    trianium = 0
    rarity = 1
    name = "Coelophysis"

#Other

class Watcher(object): 
    health = 99999999
    attack = 0
    intro = "..."
    defense = 99999999
    melee = 0
    gold = 0
    trianium = 0
    rarity = 1

class TimeSpirit(object):
    health = 99999999
    attack = 0
    defense = 99999999
    melee = 0
    gold = 0
    trianium = 0
    rarity = 1
    
class Blockard(object):
    health = 30
    attack = 3
    defense = 15
    melee = 50
    gold = 9999999999
    trianium = 0
    rarity = 3

class Mike_Vander(object):
    health = 30
    attack = 3
    defense = 15
    melee = 0
    gold = 200
    trianium = 0
    rarity = 2
    
class Pastor_Vander(object):
    health = 30
    attack = 3
    intro = "There's a time for livin, and a time for dyin'. And your time...has come."
    defense = 15
    melee = 0
    gold = 300000
    trianium = 1
    rarity = 2




    
def inventoryWipe():
        file = open("inventory.txt","w")
        file.close()

def inventoryShow():
    print ("You have the following inventory...")
    global contents
    file = open("inventory.txt","r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    print(contents)
    length = len(contents)-1
    for i in range(length):
        print(contents[i])


def lootCheck(lootX):
    file = open("inventory.txt","r")
    contents = file.read()
    contents = contents.split(",")
    if lootX in contents:
        print("You already have this item.")
    else:
        inventory =(lootX)
        
def inventory(lootX):
    file = open("inventory.txt","a")
    file.write(str(lootX + ","))
    file.close()

def inventoryDelete(decisionX):
    file = open("inventory.txt","a")
    contents = file.read()
    file.close()
    print(contents)
    if decisionX in contents:
        i = contents.index(decisionX)
        del contents[i]
        print(contents)
        print(decisionX)
        contents = contents[:-1]
        print(contents)

def inventoryUse(decisionX, contents, lootX):
    if "energy drink" in contents and decisionX == "energy drink":
        print("You add 2 health")
        character.health == character.health + 2
        print ("You now have", character.health, "hitpoints.")
        inventoryDelete(decisionX)

    elif "health kit" in contents and decisionX == "health kit":
        print("You add 10 health")
        character.health == character.health + 10
        print ("You now have", character.health, "hitpoints.")
        inventoryDelete(decisionX)
              
    elif "gauze" in contents and decisionX == "gauze":
        print("You add 5 health")
        character.health == character.health + 5
        print ("You now have", character.health, "hitpoints.")
        inventoryDelete(decisionX)
        
    elif "kevlar vest" in contents and decisionX == "kevlar vest":
        print("You add 10 defense")
        character.defense == character.defense + 5
        print ("You now have", character.health, "defense.")
        
    elif "combat boots" in contents and decisionX == "combat boots":
        print("You add 2 defense")
        character.defense == character.defense + 2
        print ("You now have", character.health, "defense.")
        
    elif "SWAT helmet" in contents and decisionX == "SWAT helmet":
        print("You add 3 defense")
        character.defense == character.defense + 3
        print ("You now have", character.health, "defense.")
      
    elif "cowboy boots" in contents and decisionX == "cowboy boots":
        print("You add 1 defense")
        character.defense == character.defense + 1
        print ("You now have", character.health, "defense.")

    elif "cowboy hat" in contents and decisionX == "cowboy hat":
        print("You add 1 defense")
        character.defense == character.defense + 1
        print ("You now have", character.health, "defense.")

    elif "combat boots" in contents and decisionX == "combat boots":
        print("You add 2 defense")
        character.defense == character.defense + 2
        print ("You now have", character.health, "defense.")


    elif "police sidearm" in contents and decisionX == "police sidearm":
        print("You add 5 attack.")
        character.attack == character.attack + 5
        print("You now have", character.attack, "Attack.")
              

    elif "mace" in contents and decisionX == "mace":
        print("You add 1 attack.")
        character.attack == character.attack + 1
        print("You now have", character.attack, "Attack.")
        
              

    elif "shotgun" in contents and decisionX == "shotgun":
        print("You add 15 attack.")
        character.attack == character.attack + 15
        print("You now have", character.attack, "Attack.")

                  

    elif "rifle" in contents and decisionX == "rifle":
        print("You add 10 attack.")
        character.attack == character.attack + 10
        print("You now have", character.attack, "Attack.")
              
              

    elif "magnum" in contents and decisionX == "magnum":
        print("You add 12 attack.")
        character.attack == character.attack + 12
        print("You now have", character.attack, "Attack.")

              

    elif "buck knife" in contents and decisionX == "buck knife":
        print("You add 5 attack.")
        character.attack == character.attack + 5
        print("You now have", character.attack, "Attack.")

                  

    elif "heat ray" in contents and decisionX == "heat ray":
        print("You add 25 attack.")
        character.attack == character.attack + 25
        print("You now have", character.attack, "Attack.")
              

    elif "trianium actuator" in contents and decisionX == "trianium actuator":
        print("You add 50 attack.")
        character.attack == character.attack + 50
        print("You now have", character.attack, "Attack.")

              

    elif "crowbar" in contents and decisionX == "crowbar":
        print("You add 4 attack.")
        character.attack == character.attack + 4
        print("You now have", character.attack, "Attack.")
              
    else:
        print("Imaginary objects don't win real fights...")
    
def inventoryDelete(decisionX):
    file = open("inventory.txt","r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    print(contents)
    if decisionX in contents: 
        i = contents.index(decisionX)
        del contents[i]
        print(contents)
        print(decisionX)
        contents = contents[:-1]
        print(contents)
        
        file = open("inventory.txt","w")
        for x in range (0, len(contents)):
            print(contents[x])
            file.write(contents[x]+",")
        file.close()
def loot(enemyList, enemyNo):
    file = open("loot.txt", "r")
    lootTableCommon = file.readline()
    lootTableRare = file.readline()
    lootTablePriceless = file.readline()
    file.close()

    lootTableCommon = lootTableCommon.split(",")
    lootTableRare = lootTableRare.split(",")
    lootTablePriceless = lootTablePriceless.split(",")

    lootTableCommon = lootTableCommon[:-1]
    lootTableRare = lootTableRare[:-1]
    lootTablePriceless = lootTablePriceless[:-1]

    global lootX

    if enemyList[enemyNo].rarity ==0:
        length = (len(lootTableCommon))-1
        lootX = lootTableCommon[random.randint(0, length)]
        lootX = str(lootX)
        print("Your victim dropped...", lootX)
        lootCheck(lootX)

    elif enemyList[enemyNo].rarity ==1:
        length = (len(lootTableRare))-1
        lootX = lootTableRare[random.randint(0, length)]
        lootX = str(lootX)
        print("Your victim dropped...", lootX)
        lootCheck(lootX)

    else:
        length = (len(lootTablePriceless))-1
        lootX = lootTablePriceless[random.randint(0, length)]
        lootX = str(lootX)
        print("Your victim dropped...", lootX)
        lootCheck(lootX)

def battlestate():
    battlestate = 1
    enemyNo = random.randint(0,3)
    enemyList = [Morlock, Outlaw, Everlasting, Scavenger, Martian, Lamanian, Kylebot, coyote, Uranium, Coelophysis, manna_addict, Rattlesnake, lamanian_militant]
    attackList = [character.attack, character.melee]
    print ("An enemy approaches...")
    print("Its a", enemyList[enemyNo].name,"!!!!")
    print ("An overwhelming surge of adrenaline hits you as you raise your weapon.")
    decision = int(input("1. Attack\n2. Check Inventory \n3. Flee"))

    while decision > 3:
        print ("number not allowed...")
        decision = int(input("1. Attack\n2. Check Inventory \n3. Flee"))


    while battlestate == 1:
        if decision == 1:
            print ("you have 2 attack options...")
            attack = int(input("1. Attack\n2. Melee."))
            x = attack - 1

            miss = random.randint(0,10) + character.luck

            if miss > 8:
                print ("You missed...")
                print ("Your enemy strikes.")
                print(enemyList[enemyNo], "Makes a hit.")
                damage = round(enemyList[enemyNo].attack / character.defense, 2)
                character.health = character.health - damage
                print("You remaining health is...", character.health)
                if character.health<1:
                    print ("Everything slips away...you are dead.")
                    quit ("Darkness...nothing...")

            else:
                if attack == 1:
                    damage = round(attackList[x] / enemyList[enemyNo].defense, 2)
                    print ("You fire your weapon and do...", damage, "damage")
                    enemyList[enemyNo].health = enemyList[enemyNo].health - damage
                    print("Enemy health remaining:", enemyList[enemyNo].health)

                    if enemyList[enemyNo].health <1:
                        print ("You've defeated,enemyList[enemyNo]")
                        enemyList[enemyNo].health = 100
                        battlestate = 0

                        loot(enemyList, enemyNo)

                    else:
                        decision = int(input("1. Attack. Check Inventory. Flee"))

                elif attack==2:
                    damage = round(attackList[x] / enemyList[enemyNo].defense, 2)
                    print ("Your take a swing and do...", damage, "damage")
                    enemyList[enemyNo].health = enemyList[enemyNo].health - damage
                    print("Enemy health remaining:", enemyList[enemyNo].health)
                    
                    if enemyList[enemyNo].health <1:
                        print ("You've defeated",enemyList[enemyNo].name)
                        enemyList[enemyNo].health = 100
                        battlestate = 0

                        loot(enemyList, enemyNo)

                    else:
                        decision = int(input("1. Attack\n2. Check Inventory \n3. Flee"))
                else:
                    print("Not allowed...")
                    attack = int(input("1. Attack\n2. Melee."))
                    x = attack - 1
                    
        elif decision == 2:
            battlestate == 0
            inventoryShow()
            decisionX = input("What item do you use?")
            inventoryUse('decisionX', 'contents', 'lootX')
            battlestate = 1
            decision = int(input("1. Attack\n2. 2. Check Inventory \n3 3. Flee"))

        elif decision == 3:
            Flee = random.randint(1,2)
            if ("Flee") == 1:
                print ("You manage to get away.")
                battlestate = 0
            else:
                print("You feel your enemy pulling you back...the fight isn't over")
                decision = int(input("1. Attack\n2. Check Inventory \n3. Flee"))


        else:
            print("INVALID")
            decision = int(input("1.Attack\n2. Check Inventory\n3. Flee"))
        

print("Who would you like to play as?")
choice = input("1. Flynn\n2. Cecily\n3. Rob\n")

while choice != "1" and choice != "2" and choice != "3":
    print("Invalid Selection")
    choice = input("1. Flynn\n2. Cecily\n3. Rob\n")

if choice == "1":
    character = (Flynn)
elif choice == "2":
    character = (Cecily)
elif choice == "3":
    character = (Rob)

print("Hello,", character.name)

battlestate()
inventoryShow()
        
inventoryWipe()
