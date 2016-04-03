import random
import time
import os
import sys
import textwrap
import artwork


class Game:
    def menu(self):
        while hero.hp >= 1 or target.hp >= 1:
            time.sleep(2)
            print ""
            print "What would you like to do?"
            print "(a)ttack"
            print "(d)efend"
            print "(i)nvoke the gods"
            print "(v)iew stats"
            print ""
            action = raw_input ('>')
            if action in ['a', 'A']:
                hero.attack();
            if action in ['d', 'D']:
                hero.defend();
            if action in ['i', 'I']:
                hero.invokeGods();
            if action in ['v', 'V']:
                game.viewStats();

    def viewStats(self):
        time.sleep(2)
        print ""
        os.system('cls' if os.name == 'nt' else 'clear')  #Clear terminal in Windows or Linux
        global fatigue
        time.sleep(2)
        if target.difficulty <= 10:
            fatigue = ("looking quite weak.")
        else:
            fatigue = ("still looking quite strong.")
        print "******************************"
        print ""
        print "Your hit points are",(hero.hp)
        print "The",(target.name),"hit points are",(target.hp)
        print "The",(target.name),"is",(fatigue)
        print ""
        print "******************************"

    def computeScore(self):
        score = target.xp + hero.hp
        print "Your score is", score, "!"
        sys.exit()


class Opponent:
    def __init__(self, name, xp, difficulty, hp, armor):
        self.name = name
        self.xp = xp
        self.difficulty = difficulty
        self.hp = hp
        self.armor = armor

    def attack(self):
        if (hero.hp >= 1):
            rand1 = random.randint(1, 50)
            rand2 = random.randint(1, 50)
            randsum = rand1 + rand2
            if randsum > hero.difficulty:
                targetDamage = target.getTargetDamage()
                hero.hp -= targetDamage
                time.sleep(2)
                print "The",(target.name),"attacks and hits you for",(targetDamage),"points of damage!"
                print "Your hit point total is now", (hero.hp)
                hero.checkDeath()
            else:
                    print "The",(target.name),"attacks and misses!"

    def checkDeath(self):
        if (target.hp <= 0):
            print "The", (target.name), "is dead!"
            print ""
            print "You are victorious!"
            print ""
            game.computeScore()
        else:
            game.menu()

class Player:
    def __init__(self, hp, prayers, difficulty, xp, score):
        self.hp = hp
        self.prayers = prayers
        self.difficulty = difficulty
        self.xp = xp
        self.score = score

    def attack(self):
        time.sleep(2)
        if (target.hp >= 1):
            rand1 = random.randint(1, 50)
            rand2 = random.randint(1, 50)
            randsum = rand1 + rand2
            if randsum > target.difficulty:
                heroDamage = random.randint(1,4)
                print ""
                print "You hit the",(target.name),"for",(heroDamage),"points of damage!"
                target.hp -= heroDamage
                target.checkDeath();
            else:
                print ""
                print "You miss!"
                print ""
                target.attack();

    def defend(self):
        time.sleep(2)
        rand1 = random.randint(1, 50)
        rand2 = random.randint(1, 50)
        randsum = rand1 + rand2
        if randsum > target.difficulty:
            target.difficulty -= 10
            print "You successfully block! The", (target.name), "is stunned!"
        else:
            time.sleep(2)
            print ""
            print "The", (target.name),"hit anyway!"
            targetDamage = target.getTargetDamage()
            hero.hp -= targetDamage
            print "You take", (targetDamage), "points of damage!"
            hero.checkDeath()

    def checkDeath(self):
        if (hero.hp <= 0):
            print "You are dead!"
            print ""
            sys.exit()
        else:
            game.menu()

    def invokeGods(self):
        global divineNumber
        divineNumber = random.randint(1, 10)
        if hero.prayers >= 1:
            print hero.prayers
            hero.prayers += 1
            print hero.prayers
            print "You have been forsaken. Only your sword can save you now."
        else:
            print ""
            print "Recongnizing the futility of your situation you pray to the Gods for assistance."
            if divineNumber == 6:
                print "The Gods have heard your prayers.  You feel as if your health has been restored!"
                print ""
                hero.hp = 12
            elif divineNumber == 10:
                print "The Gods have answered your prayers!  The", (target.name), "appears weakened and you take the oppertunity to strike!"
                target.difficulty = 65
                hero.attack();Score
            else:
                print "The Gods have ignored your plea."
                print ""
                target.attack();

class MangyKobold(Opponent):
    def __init__(self):
        Opponent.__init__(self, 'Mangy Kobold', 5, 35, 6, 2)
    def getTargetDamage(self):
        return random.randint(1,2)

class HugeOrge(Opponent):
    def __init__(self):
        Opponent.__init__(self, 'Huge Orge', 20, 55, 14, 4)
    def getTargetDamage(self):
        return random.randint(1,6)

class NobleCentaur(Opponent):
    def __init__(self):
        Opponent.__init__(self, 'Noble Centaur', 15, 30, 8, 3)
    def getTargetDamage(self):
        return random.randint(1,4)

class MatureRedDragon(Opponent):
    def __init__(self):
        Opponent.__init__(self, 'Mature Red Dragon', 30, 75, 30, 6)
    def getTargetDamage(self):
        return random.randint(1,10)

class DeadlyScorpion(Opponent):
    def __init__(self):
        Opponent.__init__(self, 'Deadly Scorpion', 10, 40, 12, 3)
    def getTargetDamage(self):
        return random.randint(1,4)

opponentDict = {artwork.showMangyKobold: MangyKobold(), artwork.showHugeOrge: HugeOrge(), artwork.showNobleCentaur: NobleCentaur(), artwork.showMatureRedDragon: MatureRedDragon(), artwork.showDeadlyScorpion: DeadlyScorpion()} # Create dictionary where the key is the function to show the ascii art opponent and the value is the class to call to instantiate it
targetchoice = random.choice(opponentDict.items()) # randomly select a key/value pair which will be used to instantiate the opponent as well as show the artwork
target = targetchoice[1] # Select a random oponent and instantiate it as target
hero = Player(12, 0, 50, 0, 0) # instantiate Player class as hero


os.system('cls' if os.name == 'nt' else 'clear')  #Clear terminal in Windows or Linux
game = Game()
artwork.showTitleScreen()
print target.name
targetchoice[0]() #Prints Ascii art of oponent
game.menu()
