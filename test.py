import random as rnd

#feladat: fejlesztés - prototípus

#tier 1 upgrade cost: 20, upgrade multiplier: 1.25, drop chance: 60%
#tier 2 Upgrade cost: 40 upgrade multiplier: 2.5, drop chance: 35%
#tier 3 upgrade cost: 60 upgrade multiplier: 5.0, drop chance: 5%


def dropItem():
    pass

def addMoney():
    money += 30

money = 0
itemLevels = {
    "damage":1,
    "speed":1,
    "luck":1
}
ownedItems = []

print(rnd.randInt(0, 100))
