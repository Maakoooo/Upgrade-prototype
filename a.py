import random as rnd

#feladat: fejlesztés - prototípus

#tier 1 upgrade cost: 20, upgrade multiplier: 1.25, drop chance: 50%
#tier 2 Upgrade cost: 40 upgrade multiplier: 2.5, drop chance: 30%
#tier 3 upgrade cost: 60 upgrade multiplier: 5.0, drop chance: 5%

def Upgrade(): #gomb lenyomásakor haíjuk meg
    pass

def dropItem():
    if (bossalive = False): #ezt az ifet kivesszük, ha készen lesz az a függvény, ami a boss halálakor meghívja ezt a függvényt
        dropResult = rnd.randInt(0,100)
        if (dropResult <= dropChance[2]):
            if (dropResult <= dropChance[1]):
                if (dropResult <= dropChance[0]):
                    whichTier = 3
                else:
                    whichTier = 2
            else:
                whichTier = 1
        else:
            whichTier = 0 #nem kapunk itemet


def addMoney():
    money += 30

whichTier = 0
dropChance = [5, 35, 85]
dropResult = 0
bossAlive = True
money = 0
itemLevels = {
    "damage":1,
    "speed":1,
    "luck":1
}
ownedItems = []

print(rnd.randInt(0, 100))
