import sys
import os
import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.pots = 0

class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 10
GoblinIG = Goblin("Goblin")

class Skeleton:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 30
        self.health = self.maxhealth
        self.attack = 7
        self.goldgain = 8
SkeletonIG = Skeleton("Skeleton")

class Demon:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 90
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 20
Demon = Demon("Demon")

def main():
    os.system('cls')
    print("Welcome to the Thunder-Dome.")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option = input("--> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()

def start():
    os.system('cls')
    print("Hello, what is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start1():
    os.system('cls')
    print("Name: {0}".format(PlayerIG.name))
    print("Attack: {0} ".format(PlayerIG.attack))
    print("Gold: %d" % PlayerIG.gold)
    print("Potions: %d" % PlayerIG.pots)
    print("Health: %i /" % PlayerIG.health, PlayerIG.maxhealth)
    print("\n")
    print("1.) Dungeons")
    print("2.) Store")
    print("3.) Save")
    print("4.) Exit")
    option = input("--> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        pass
    elif option == "4":
        sys.exit()
    else:
        start1()

def prefight():
    global enemy
    enemynum = random.randint(1, 3)
    if enemynum == 1:
        enemy = GoblinIG
    if enemynum == 2:
        enemy = SkeletonIG
    else:
        enemy = Demon
    fight()



def fight():
    os.system('cls')
    print("{0}     vs     {1}".format(PlayerIG.name, enemy.name))
    print("{0}'s Health:  {1}/{2}      {3}'s Health: {4}/{5}".format(PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Potions:  %i \n" % PlayerIG.pots)
    print("1.) Attack")
    print("2.) Drink Potion")
    print("3.) Run")
    option = input("-->")
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack / 2, PlayerIG.attack)
    EAttack = random.randint(round(enemy.attack* 0.5), enemy.attack)
    if PAttack == PlayerIG.attack / 2:
        print("You missed!")
    else:
        enemy.health -= PAttack
        print("You deal %i damage!" % PAttack)
    if enemy.health <=0:
        win()
    option = input("--> ")
    os.system('cls')
    if EAttack == enemy.attack/2:
        print("Attack dodged!")
    else:
        PlayerIG.health -= EAttack
        print("The enemy deals {0} damage!".format(EAttack))
    option = input("--> ")
    if PlayerIG.health <= 0:
        die()
    else:
        fight()
def drinkpot():
    os.system('cls')
    if PlayerIG.pots == 0:
        print("You don't have any potions!")
    else:
        PlayerIG.heatlh += 50
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        print("You drank a potion!")
    option = input("--> ")
    fight()

def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have escaped the fight!")
        option = input("---> ")
        start1()
    else:
        print("You failed to get away!")
        option = input("---> ")
        os.system('cls')
        EAttack = random.randint(round(enemy.attack * 0.5), enemy.attack)
        if EAttack == enemy.attack / 2:
            print("Attack dodged!")
        else:
            PlayerIG.health -= EAttack
            print("The enemy deals {0} damage!".format(EAttack))
            option = input("--> ")
            if PlayerIG.health <= 0:
                die()
            else:
                fight()

def win():
    os.system('cls')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    print("You have defected the {0} !".format(enemy.name))
    print("You found {0} gold!".format(enemy.goldgain))
    option = input("---> ")
    start1()
def die():
    os.system('cls')
    print("You have died!")
    option = input("---> ")

def store():
    pass


main()
