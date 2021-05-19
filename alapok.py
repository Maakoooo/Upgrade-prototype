import random as rnd

#tier 1 upgrade cost: 20, upgrade multiplier: 1.25, drop chance: 50%
#tier 2 Upgrade cost: 40 upgrade multiplier: 2.5, drop chance: 30%
#tier 3 upgrade cost: 60 upgrade multiplier: 5.0, drop chance: 5%
#minden itemnek van egy száma és minden számhoz tartozik még:
#az item jelenlegi szintje - akkor tér el egytől ha már birtokoljuk és fejlesztettük is
#item alapára - ezt fogjuk szorozni mindig, amikor fejlesztjük
#item alap buff-ja - ezt fogjuk szorozni, amikor fejlesztjük
#a tiert az item sorszáma, a szorzóját a tiere határozza meg

def upgrade(): #gomb lenyomásakor hívjuk meg
    pass

def dropItem():
    if (bossalive = False): #ezt az ifet kivesszük, ha készen lesz az a függvény, ami a boss halálakor meghívja ezt a függvényt
        dropResult = rnd.randInt(0,100)
        if (dropResult <= dropChance[2]):
            if (dropResult <= dropChance[1]):
                if (dropResult <= dropChance[0]):
                    ownedItems.append(rnd.randInt(20,30)) #tier 3-as itemek sorszámai: 21-30
                else:
                    ownedItems.append(rnd.randInt(10,20)) #tier 2-es itemek sorszámai: 11-20
            else:
                ownedItems.append(rnd.randInt(0,10)) #tier 1-es itemek sorszámai: 1-10
        else:
            #nem kapunk itemet

def addMoney():
    money += 30

dropChance = [5, 35, 85] #az első szám a tier 3 drop chance-e, a második a tier 2 és tier 3 összege, a harmadik az összes tier drop chance-e összeadva
dropResult = 0
bossAlive = True
money = 0
ownedItems = []  
