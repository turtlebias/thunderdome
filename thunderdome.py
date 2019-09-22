import sys
import os
import time
import random
import pickle
import socket


weapons = {"Great Sword":40, "Knight's Sword":100, "Demon Slayer":200, "Angel's Scythe":350, "Homing Bow":300}


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 3
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5

        if self.curweap == "Great Sword":
            attack += 15

        if self.curweap == "Knight's Sword":
            attack += 25

        if self.curweap == "Demon Slayer":
            attack += 35

        if self.curweap == "Angel's Scythe":
            attack += 45

        if self.curweap == "Homing Bow":
            attack += 30


        return attack



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

class Rouge:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 15
        self.goldgain = 30
Rouge = Rouge("Rouge Angel")

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
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded Save State!")
            option = input("---> ")
            start1()
        else:
            print("You have no current saves.")
            option = input("---> ")
            main()


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
    print("Current Weapon: {0}".format(PlayerIG.curweap))
    print("Potions: %d" % PlayerIG.pots)
    print("Health: %i /" % PlayerIG.health, PlayerIG.maxhealth)
    print("\n")
    print("1.) Dungeons")
    print("2.) Store")
    print("3.) Save")
    print("4.) Exit")
    print("5.) Inventory")
    option = input("--> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nThe game has been successfully saved!\n")
        option = input("---> ")
        start1()
    elif option == "4":
        sys.exit()
    elif option == "5":
        inventory()
    else:
        start1()

def inventory():
    os.system('cls')
    print("What do you wish to do?")
    print("1.) Equip Weapon")
    print("b.) Back")
    option = input("---> ")
    if option == "1":
        equip()
    elif option == "b":
        start1()

def equip():
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("b.) Back")
    option = input("---> ")
    if option == PlayerIG.curweap:
        os.system('cls')
        print("Item is already equipped.")
        option = input("---> ")
        equip()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weap:
        os.system('cls')
        PlayerIG.curweap = option
        print("You have equipped: {0}".format(option))
        option = input("---> ")
        equip()
    else:
        os.system('cls')
        print("You do not own this weapon.")
        option = input("---> ")
        equip()

def prefight():
    global enemy
    enemynum = random.randint(1, 4)
    if enemynum == 1:
        enemy = GoblinIG
    if enemynum == 2:
        enemy = SkeletonIG
    if enemynum == 3:
        enemy = Demon
    else:
        enemy = Rouge
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
        option = input("---> ")
        fight()
    if PlayerIG.pots >= 1:
        PlayerIG.health += 50
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
    os.system('cls')
    print("Welcome to the shop!")
    print("\nWhat would you like to buy?\n")
    print("1.) Great Sword")
    print("2.) Knight's Sword")
    print("3.) Demon Slayer")
    print("4.) Angel's Scythe")
    print("5.) Homing Bow")
    print("\nPotions\n")
    print("1.) Health Potion")
    print("b.) Back")
    print("  ")
    option = input("---> ")

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            os.system('cls')
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print("You have purchased the {0} !".format(option))
            option = input("---> ")
            store()

        else:
            os.system('cls')
            print("You don't have enough gold for this item.")
            option = input("---> ")
            store()

    if option == "Health Potion":
        if PlayerIG.gold >= 40:
            os.system('cls')
            PlayerIG.gold -= 40
            PlayerIG.pots += 1
            print("You have purchased a %s !" % option)
            option = input("---> ")
            store()
        else:
            os.system('cls')
            print("You do not have enough gold for this item.")

    elif option == "Back":
        start1()
    else:
        os.system('cls')
        print("We don't have that item in stock at the moment!")
        option = input("---> ")
        store()

main()
