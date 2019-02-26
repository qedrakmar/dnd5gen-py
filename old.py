from random import randint

races=['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Tiefling','Aasimar']

classlist=[
    'Barbarian',
    'Lore Bard',
    'Valor Bard',
    'Caster Cleric',
    'Combat Cleric',
    'Land Druid',
    'Moon Druid',
    'Fighter',
    'Eldritch Knight',
    'Monk',
    'Paladin',
    'Ranger', 
    'Rogue', 
    'Arcane Trickster', 
    'Sorcerer', 
    'Warlock', 
    'Wizard', 
    'Enchanter',
    ]

classes={
    'Barbarian': [
        ('Str',1),
        ('Dex',3),
        ('Con',2),
        ('Int',5),
        ('Wis',4),
        ('Cha',6),
        ],
    'Lore Bard': [
        ('Str',6),
        ('Dex',3),
        ('Con',5),
        ('Int',2),
        ('Wis',4),
        ('Cha',1),
        ],
    'Valor Bard': [
        ('Str',5),
        ('Dex',2),
        ('Con',4),
        ('Int',3),
        ('Wis',6),
        ('Cha',1),
        ],
    'Caster Cleric': [
        ('Str',6),
        ('Dex',3),
        ('Con',4),
        ('Int',5),
        ('Wis',1),
        ('Cha',2),
        ],
    'Combat Cleric': [
        ('Str',3),
        ('Dex',6),
        ('Con',2),
        ('Int',5),
        ('Wis',1),
        ('Cha',4),
        ],
    'Land Druid': [
        ('Str',5),
        ('Dex',4),
        ('Con',2),
        ('Int',3),
        ('Wis',1),
        ('Cha',6),
        ],
    'Moon Druid': [
        ('Str',5),
        ('Dex',6),
        ('Con',4),
        ('Int',2),
        ('Wis',1),
        ('Cha',3),
        ],
    'Fighter': [
        ('Str',1),
        ('Dex',3),
        ('Con',2),
        ('Int',5),
        ('Wis',4),
        ('Cha',6),
        ],
    'Eldritch Knight': [
        ('Str',1),
        ('Dex',5),
        ('Con',3),
        ('Int',2),
        ('Wis',4),
        ('Cha',6),
        ],
    'Monk': [
        ('Str',6),
        ('Dex',1),
        ('Con',3),
        ('Int',4),
        ('Wis',2),
        ('Cha',5),
        ],
    'Paladin': [
        ('Str',1),
        ('Dex',5),
        ('Con',4),
        ('Int',6),
        ('Wis',3),
        ('Cha',2),
        ],
    'Ranger': [
        ('Str',5),
        ('Dex',1),
        ('Con',3),
        ('Int',4),
        ('Wis',2),
        ('Cha',6),
        ],
    'Rogue': [
        ('Str',4),
        ('Dex',1),
        ('Con',5),
        ('Int',3),
        ('Wis',6),
        ('Cha',2),
        ],
    'Arcane Trickster': [
        ('Str',5),
        ('Dex',1),
        ('Con',6),
        ('Int',2),
        ('Wis',4),
        ('Cha',3),
        ],
    'Sorcerer': [
        ('Str',6),
        ('Dex',3),
        ('Con',2),
        ('Int',4),
        ('Wis',5),
        ('Cha',1),
        ],
    'Warlock': [
        ('Str',5),
        ('Dex',4),
        ('Con',2),
        ('Int',6),
        ('Wis',3),
        ('Cha',1),
        ],
    'Wizard': [
        ('Str',6),
        ('Dex',2),
        ('Con',3),
        ('Int',1),
        ('Wis',4),
        ('Cha',5),
        ],
    'Enchanter': [
        ('Str',6),
        ('Dex',4),
        ('Con',5),
        ('Int',1),
        ('Wis',3),
        ('Cha',2),
        ],
    }

def race():
    num1 = randint(0,len(races)-1)
    return races[num1]

def clas():
    num1 = randint(0,len(classes)-1)
    return classes.keys()[num1]

myrace = race()
myclass = clas()

print "Your character is a %s %s" % (myrace, myclass)
# print myclass
# print classes

stats=[]

def fourd6():
    num1 = randint(1,6)
    low = num1
    num2 = randint(1,6)
    if (num2 < low):
        low = num2
    num3 = randint(1,6)
    if (num3 < low):
        low = num3
    num4 = randint(1,6)
    if (num4 < low):
        low = num4
    score = num1 + num2 + num3 + num4 - low    
    nums = [num1, num2, num3, num4, "Score = "+str(score)]
    stats.append(score)    
    return nums

for x in range(0,6):
    fourd6()

def assignstats():
    stats.sort()
    stats.reverse()
    stre = stats[classes[myclass][0][1]-1]
    con = stats[classes[myclass][1][1]-1]
    dex = stats[classes[myclass][2][1]-1]
    inte = stats[classes[myclass][3][1]-1]
    wis = stats[classes[myclass][4][1]-1]
    cha = stats[classes[myclass][5][1]-1]
    ordered = [stre, con, dex, inte, wis, cha]
    return ordered

orderedstats = assignstats()

print stats 
print "Without any racial modifiers:"
print "Str = " + str(orderedstats[0]) + ", with a " + str(int((orderedstats[0] - 10)/2)) + " Bonus"
print "Dex = " + str(orderedstats[1]) + ", with a " + str(int((orderedstats[1] - 10)/2)) + " Bonus"
print "Con = " + str(orderedstats[2]) + ", with a " + str(int((orderedstats[2] - 10)/2)) + " Bonus"
print "Int = " + str(orderedstats[3]) + ", with a " + str(int((orderedstats[3] - 10)/2)) + " Bonus"
print "Wis = " + str(orderedstats[4]) + ", with a " + str(int((orderedstats[4] - 10)/2)) + " Bonus"
print "Cha = " + str(orderedstats[5]) + ", with a " + str(int((orderedstats[5] - 10)/2)) + " Bonus"
