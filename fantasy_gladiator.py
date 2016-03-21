import random
import time
import os
import sys
import textwrap

global heroDifficulty
global targetDamage
global xp
global score
global heroHP
global randsum
global difficulty
global heroDamage
global action

prayers = 0
score = 0
xp = 0
targetDamage = 0
heroDifficulty = 50
heroHP = 12


clear = lambda: os.system('cls')  #This sets up ...
clear()                           #which clears the screen in Windows

#os.system('clear')   This clears the screen in Linux
 
print"  ___                                     __                                    "    
print" /              /                        /    /         | /      /              "    
print"(___  ___  ___ (___  ___  ___           ( __ (  ___  ___|   ___ (___  ___  ___  "
print"|    |   )|   )|    |   )|___ \   )     |   )| |   )|   )| |   )|    |   )|   ) "
print"|    |__/||  / |__  |__/| __/  \_/      |__/ | |__/||__/ | |__/||__  |__/ |     "
print"                                /                                               "
 
print "A gate lifts and the burning sunlight dazzles your eyes.  Your vision clears and you gaze upon a huge arena."
print "You walk out into the center of the arena to the cheers and ridicule of a rowdy audience.  Another gate at the"
print "far end of the arena slowly opens and you find yourself face to face with a...."
print ""
time.sleep(5)

 
def targetChoice():
    global target
    global targetnum
    time.sleep(2)  #delays for 3 seconds
    targetnum = random.randint(1, 5)    
    if targetnum == 1:
            target = "mangy kobold"
            xp = 5
            printKobold();
    elif targetnum == 2:
            target = "huge Orge"
            xp = 20
            printOgre();
    elif targetnum == 3:
            target = "noble Centaur"
            xp = 15
            printCentaur();
    elif targetnum == 4:
            target = "mature Red Dragon"
            xp = 30
            printDragon();
    else:
            target = "deadly scorpion"
            xp = 10
            printScorpion();
    print "...",(target),"!"
    print ""
    #print(targetnum)
 
def setupCombat():
    global difficulty
    global targetHP
    global targetDamage
    global targetArmor
    if targetnum == 1:       #Kobold
        difficulty = 35
        targetHP = 6
        targetArmor = 2
    elif targetnum == 2:     #Ogre
        difficulty = 55
        targetHP = 14
        targetArmor = 4
    elif targetnum == 3:     #Human
        difficulty = 30
        targetHP = 8
        targetArmor = 3
    elif targetnum == 4:     #Dragon
        difficulty = 75
        targetHP = 30
        targetArmor = 6
    else:
        difficulty = 40      #Scorpion
        targetHP = 12
        targetArmor = 3

 
 
def menu():
    global action
    global prayers
    #print prayers
    while heroHP >= 1 or targetHP >= 1:
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
            heroAttack();
        if action in ['d', 'D']:
            heroDefend();
        if action in ['i', 'I']:
            invokeGods();
        if action in ['v', 'V']:
            viewStats();
 
 
def viewStats():
    time.sleep(2)
    print ""
    #os.system('clear')       #Linux clear screen
    clear()                   #clears the screen in Windows
    global fatigue
    time.sleep(2)
    if difficulty <= 10:
        fatigue = ("looking quite weak.")
    else:
        fatigue = ("still looking quite strong.")
    print "******************************"
    print ""
    print "Your hit points are",(heroHP)
    print "Thet",(target),"hit points are",(targetHP)
    print "The",(target),"is",(fatigue)
    print ""
    print "******************************"


def invokeGods():
    time.sleep(2)
    global difficulty
    global divineNumber
    global prayers
    divineNumber = random.randint(1, 10)
    if prayers >= 1:
        print prayers
        prayers = prayers + 1
        print prayers
        print "You have been forsaken. Only your sword can save you now."
    else:
        print ""
        print "Recongnizing the futility of your situation you pray to the Gods for assistance."
        if divineNumber == 1:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 2:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 3:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 4:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 5:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 6:
            print "The Gods have heard your prayers.  You feel as if your health has been restored!"
            print ""
            heroHP = 12
        elif divineNumber == 7:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 8:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        elif divineNumber == 9:
            print "The Gods have ignored your plea."
            print ""
            targetAttack();
        else:
            print "The Gods have answered your prayers!  The", (target), "appears weakened and you take the oppertunity to strike!"
            difficulty = 65
            heroAttack();
        
 
def heroAttack():
    global targetHP
    #print difficulty 
    time.sleep(2)
    if (targetHP >= 1):
        rand1 = random.randint(1, 50)
        rand2 = random.randint(1, 50)
        randsum = rand1 + rand2
        if randsum > difficulty:
            heroDamage = random.randint(1,4)
            print ""
            print "You hit the",(target),"for",(heroDamage),"points of damage!"
            targetHP = targetHP - heroDamage
            checkTargetDeath();
        else:
            print ""
            print "You miss!"
            print ""
            targetAttack();
             
 
def heroDefend():
    global heroHP
    global difficulty
    targetDamage = 0
    time.sleep(2)
    rand1 = random.randint(1, 50)
    rand2 = random.randint(1, 50)
    randsum = rand1 + rand2
    if randsum > difficulty:
        difficulty = difficulty - 10
        print "You successfully block! The", (target), "is stunned!"
    else:
        time.sleep(2)
        print ""
        print "The", (target),"hit anyway!"
        if targetnum == 1:
                targetDamage = random.randint(1,2)
        elif targetnum == 2:
                targetDamage = random.randint(1,6)
        elif targetnum == 3:
                targetDamage = random.randint(1,4)
        elif targetnum == 4:
                targetDamage = random.randint(1,10)
        heroHP = heroHP - targetDamage
        print "You take", (targetDamage), "points of damage!"
        checkHeroDeath()
        
 
def targetAttack():
    global heroHP
    #heroHP = 12
    if (heroHP >= 1):
        rand1 = random.randint(1, 50)
        rand2 = random.randint(1, 50)
        randsum = rand1 + rand2
        #print randsum
        if randsum > heroDifficulty:
            if targetnum == 1:
                targetDamage = random.randint(1,2)
            elif targetnum == 2:
                targetDamage = random.randint(1,6)
            elif targetnum == 3:
                targetDamage = random.randint(1,4)
            elif targetnum == 4:
                targetDamage = random.randint(1,10)
            else:
                targetDamage = random.randint(1,4)
            heroHP = heroHP - targetDamage
            time.sleep(2)
            print "The",(target),"attacks and hits you for",(targetDamage),"points of damage!"
            print "You're hit point total is now", (heroHP) 
            checkHeroDeath()    
        else: 
                print "The",(target),"attacks and misses!"

         
 
def checkHeroDeath():
    global heroHP
    if (heroHP <= 0):
        print "You are dead!"
        print ""
        sys.exit()
    else:
        menu()
 
 
def checkTargetDeath():
    global targetHP
    global target
    if (targetHP <= 0):
        print "The", (target), "is dead!"
        print ""
        print "You are victorious!"
        print ""
        computeScore()
    else:
        menu()

def computeScore():
    global score
    global xp
    score = xp + heroHP
    print "Your score is", score, "!"
    sys.exit()


def printCentaur():
    print textwrap.dedent(r"""

                    ,---.
                 ,-'     `----.
               ,'      )       `-._
             ,'       ;            `-.
           ,'       ,'`-.             `.        /\
         ,'     _,-'     `._            `._____( (
       ,'     ,'            `._           :<<<<<\ \_.--. /\
      ;      |           <,'   `.__,      :<<<<<<<<<<<<<`) )
     /       )         <,'                ;<<<<<<<,'  `<<<:
    (       /         <;                 ;<<<<<<<<\     `<:
    `\\\\\\(        <,'                 ;<<<<<<<<,' <@   `;
      \\\\\\      <,'                  :<<<<_\<<;      \@,
       \\\\\\   ,-'                    ;<,-' `<:     `._)
        `````  /                (.)   :,','    :        )
              /       \              ;  :       `.  <Vv>
             :         \          _,'   :         `.__/
             :          `.     ,-'      :
             ;            `.      (.)   ;
            :               `-. _,-'  ,'
            :                  \    ,'
            :                   `. ;               _/ //
           ,'                    ::             ,-' _///
          :                      :          _,-' ),'_///
          :                      :---------'   ,'  ,_//
          :                    _,:          ________.'
           :         -._____,-',xxx`._   _,-'
           :               ,xxxxxxx'   `-._
           :             ,xxxxx'           `-._
           (`.         ,xxxx'                  `-._
           :  \       ,xxxx'                       `-.
           :   \      xxxxx                           `.
           :    :    ,xxxx'                             `-._
           :    :    xxxx'                         _        `.
           :     \   xxxx                           `--._     `.
           :      \  xxxx                           ;    `-.    `.
          :  (  ) :\ 'xxx.                         ;      : `-.   `.
          :       : `.xxxx      `-.               ;       :    `.   `.
          :       :    `-._        `.            :        :      `.   :
          :       ;        :`-------.:           :         :       :   :
          :      :         :      ;  :           :         :        :  :
          :      ;         :     ;   :           :`.        `.      :  :
          :     :         :     ;     `.          : `.        :     :  :
           :    ;        :     ;        `.         :  `.       `.   ; ;
           ;   :         :    :           `.        :   `.       : ; ;
          :    (         :    :             `.       :    `.      : ;
        _,'     `.___  _/    :                `.      :     `.   ; ;
       (___,---.____-'/       `._               `.    :       :,',':
                    -__,----^----'                :    :    ,-','   :
                                                   :   : ,-',' :    :
                                                   : _,-=-'     :   :
                                                 _,-'   :_    _,:   `._
                                             _,-' _,:     `._,'        )
                                          _,'  _,'         _)_,-.___,-'
                                      _,,'   <___,-.___,--'
                                   ,-' (
                                 ,' _,--'
                                /_,'

        """)

def printScorpion():
    print textwrap.dedent(r"""

           ___ __ 
     _{___{__}\
    {_}      `\)            
   {_}        `            _.-''''--.._
   {_}                    //'.--.  \___`.
    { }__,_.--~~~-~~~-~~-::.---. `-.\  `.)
     `-.{_{_{_{_{_{_{_{_//  -- 8;=- `
        `-:,_.:,_:,_:,.`\\._ ..'=- , 
            // // // //`-.`\`   .-'/
           << << << <<    \ `--'  /----)
            ^  ^  ^  ^     `-.....--'''

    """)
            

def printKobold():
    print textwrap.dedent(r"""

                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
                  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

        """)


def printOgre():
    print textwrap.dedent(r"""

                           __,='`````'=/__
                          '//  (o) \(o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo

     """)


def printDragon():
    print textwrap.dedent(r"""

                                                 /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \
                   {\__--_/}    / \\_>- )<__\      \
                   /'   (_/  _-~  | |__>--<__|      | 
                  |0  0 _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |  
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~              
                ,/|           /__>--<__/     _-~                 
             ,//('(          |__>--<__|     /                  .----_ 
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/ 
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~ 
   ;'( ')/ ,)(                              ~~~~~~~~~~ 
  ' ') '( (/
    '   '  `

    """)

 
 
targetChoice()
setupCombat()
menu()
