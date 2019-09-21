import sys
import os
import time
import random
import pickle
import socket

weapons = {"Great Sword":40}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 40
        self.pots = 0
        self.weap = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == "Rusty Sword":
            attack += 5

        if self.curweap == "Great Sword":
            attack += 15

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
    print("6.) Multiplayer Duels")
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
    elif option == "6":
        Mp_Main()
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
        print("Item is already equipped.")
        option = input("---> ")
        equip()
    elif option == "b":
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.curweap = option
        print("You have equipped: {0}".format(option))
        option = input("---> ")
        equip()
    else:
        print("You do not own this weapon.")

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
    os.system('cls')
    print("Welcome to the shop!")
    print("\nWhat would you like to buy?\n")
    print("1.) Great Sword")
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

    elif option == "Back":
        start1()

    else:
        os.system('cls')
        print("We don't have that item in stock at the moment!")
        option = input("---> ")
        store()

def Mp_Format(name, health):
    print("{0}      vs.      {1}".format(PlayerIG.name, name))
    print("{0}'s Health: {1}".format(PlayerIG.name, PlayerIG.health))
    print("{0}'s Health: {1}".format(name, health))
    print("1.) Attack")
    mpinput = input("---> ")
    if mpinput != "1":
        Mp_Format(name,health)
    else:
        return mpinput
def Mp_Main():
    host = '192.168.1.108'
    port = 7890

    s = socket.socket
    s.connect((host, port))
    print("Waiting for another player to connect..")
    PlayerObj = pickle.dumps(PlayerIG)
    s.send(PlayerObj)
    Enemy = s.recv(1024)
    Enemy = pickle.loads(Enemy)

    while True:
        mpinput = Mp_Format(Enemy.name, Enemy.health)
        s.send(mpinput.encode())
        print("Waiting for another player to respond..")
        Damage = s.recv(1024)
        Damage = pickle.loads(Damage)
        Damage_Dealt(PlayerIG.health - Damage[0], Enemy.health-Damage[2], Enemy.name)
        PlayerIG.health = Damage[0]
        Enemy.health = Damage[1]
        if Damage[2] != 0:
            if Damage[2] == 1:
                mpwin(Enemy.name, s)
            elif Damage[2] == 2:
                mplose(Enemy.name, s)


def Damage_Dealt(x, y, name):
    print("You took %i damage." % x)
    print("You deal %i damage to %s." % (y, name))
    option = input("---> ")

def mpwin(name, s):
    print("You have defeated %s !" % name)
    option = input("---> ")
    s.close()
    start1()

def mplose(name, s):
    print("You have been defeated by %s." % name)
    option = input("---> ")
    s.close()
    start1()

if __name__ == "__main__":
    main()
