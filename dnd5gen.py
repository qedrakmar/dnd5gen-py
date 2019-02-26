import sys
import random
from random import randint

### Maybe the character info needs to be a class instead of a dict?
### Or maybe it should just be a whole bunch of flat functions?
### I think I might need to reorder things in side the class.
### If I make it all flat functions, then can I just invoke them last so order becomes irrelevant?
### Do functions that call other functions need to be def'd in order?

class character:
    def __init__(self):
# Don't forget random.seed()
        random.seed()
        self.attribs = attributes(self) #returns sorted array of 4d6_drop_lowest stats
        self.clas = clas(self) # returns base class, not archetype
        self.race = race(self) # returns ... hmm...  base race or subrace?
        self.align = alignfunc(self) # returns string of alignment
        self.skills = skillsfunc(self)
        self.combat = combatfunc(self) # To hit, init, HP, Hit dice, etc

    def attributes(self):
        self.hpbonus=0
        statsarray = []
        for i in range(6):
            statsarray.append(fourd6())
        statsarray.sort()
        return statsarray
        # assignstats(self.clas)
        # for each stat in listofstats, self.stat.bonus = bonus(self.stat)  Naaah.
        # self.stre.base, self.stre.racial, etc

    def clas(self):
        # Maybe a weighted selection for class?  Percentile?
        classlist=['barbarian','bard','cleric','druid','fighter','monk','paladin','ranger','rogue','sorcerer','warlock','wizard']
        myclass='barbarian'
        #myclass=random.choice(classlist)
        getattr(sys.modules[__name__],myclass)() #does the function need to be def'd before this line?
 #       if myclass == 'barbarian':
 #           barbarian(self)
 #       if myclass == 'bard':
 #           bard(self)
 #       if myclass == 'cleric':
 #           cleric(self)
 #       if myclass == 'druid':
 #           druid(self)
 #       if myclass == 'fighter':
 #           fighter(self)
 #       if myclass == 'monk':
 #           monk(self)
 #       if myclass == 'paladin':
 #           paladin(self)
 #       if myclass == 'ranger':
 #           ranger(self)
 #       if myclass == 'rogue':
 #           rogue(self)
 #       if myclass == 'sorcerer':
 #           sorcerer(self)
 #       if myclass == 'warlock':
 #           warlock(self)
 #       if myclass == 'wizard':
 #           wizard(self)
        return myclass

        # Do all archetypes?
        ## classlist=['Barbarian', 'Lore Bard', 'Valor Bard', 'Caster Cleric', 'Combat Cleric', 'Land Druid', 'Moon Druid',
        #'Fighter', 'Eldritch Knight', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Arcane Trickster', 'Sorcerer', 'Warlock', 'Wizard', 
        #'Enchanter']

    def race(self):
        racelist = ['Dwarf','Elf','Halfling','Human','Dragonborn','Gnome','Half-Elf','Half-Orc','Tiefling','Aasimar']
        self.dwarf()
        # choose race from list
        # subrace(return subrace, else return race)
        # or dwarf(), human(), etc

    def alignfunc():
        # one of 9 alignments: LG, NG, CG, LN, N, CN, LE, NE, CE
        # probably add weighting: 9+9+9+4+4+4+1+1+1 -> randint(1,42)
        a=range(42)
        if a<9:
            return "Lawful Good"
        elif a<18:
            return "Neutral Good"
        elif a<27:
            return "Chaotic Good"
        elif a<31:
            return "Lawful Neutral"
        elif a<35:
            return "True Neutral"
        elif a<39:
            return "Chaotic Neutral"
        elif a<40:
            return "Lawful Evil"
        elif a<41:
            return "Neutral Evil"
        else:
            return "Chaotic Evil"

    def skillsfunc():
        self.classskills = sample([self.potentialskills], k=self.numskills)
        # skills as a dict?  {"skill1":val1,"skill2":val2}

    def combatfunc():
        self.tohitstr = 0
        self.tohitdex = 0
        self.hp.total = self.hp.clas + self.hp.bonus

    def fourd6():
        rolling = []
        for i in range(4):
            rolling.append(randint(1,6))
        rolling.sort()
        return rolling.pop()+rolling.pop()+rolling.pop()
    
    def dwarf(): # use random.gauss()?
        self.age = 17 + randint(1,100)
        self.height = 47 + randint(1,12)
        self.weight = 125 + randint(1,75)
        #flip coin
        subrace = randint(1,2)
        if subrace == 1:
            self.race = "Hill Dwarf"
            self.conracial = 2
            self.wisracial = 1
            self.racialspecial = "All Racial specials text goes here"
        if subrace == 2:
            self.race = "Mountain Dwarf"
            self.conracial = 2
            self.strracial = 2
            self.racialspecial = "All Racial specials text goes here"
    

    def printstats():
        self.stre = self.strbase + self.strracial


# Call the class and print it out
MyPC = character()
MyPC.printstats() 

####  Previous Reference Notes
####

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

# def clas():
#     num1 = randint(0,len(classes)-1)
#     return classes.keys()[num1]  # .keys because we're invoking a dict


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
print "Str = " + str(orderedstats[0]) + ", with a " + str(int((orderedstats[0] - 10)/2)) + " Bonus"
print "Dex = " + str(orderedstats[1])
print "Con = " + str(orderedstats[2])
print "Int = " + str(orderedstats[3])
print "Wis = " + str(orderedstats[4])
print "Cha = " + str(orderedstats[5])


# If skill != tag then tag, else selectfromskilllist()
