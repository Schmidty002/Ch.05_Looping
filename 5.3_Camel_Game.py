'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

game = True

print("You are a pilot exploring space.")
print("A group of marauders has begun to pursue you after you encroached on their territory.")
print("The warp gate that leads to federation space is 200,000 km away.")
print("Reach the gate before running out of O2, blowing your engines, or being overtaken by the marauders.")
print("Fly well.  No barrel rolls.")
print()

udis = 0
o2 = 0
cannisters = 6
enginteg = 0
mdis = -10000

while game:
    print("Enter Command")
    print("[1] Swap O2 cannister")
    print("[2] Moderate engine power")
    print("[3] Full engine power")
    print("[4] Cut engines")
    print("[5] Status check")
    print("[0] Exit Game")
    command = input("Command: ")
    print()

    if command == "0":
        print("Are you sure you want to quit?  All game data will be lost.")
        print("[Y] or [N]")
        command = input()
        if command.lower() == "y":
            print("Exiting Game...")
            game = False
            continue
        else:
            continue

    elif command == "5":
        print("Distance to warp gate:",200000-mdis)
        print("O2 cannisters remaining:",cannisters)
        print("Distance from pursuers:",udis-mdis)
        continue

    elif command == "4":
        enginteg = 0
        print("Your engines have cooled.")
        print()
        mdis += random.randrange(7000,14001)

    elif command == "3":
        move = random.randrange(10000,14001)
        udis += move
        print("You traveled",move,"km")
        print()
        o2 += 1
        enginteg += random.randrange(1,4)
        mdis += random.randrange(7000,14001)

    elif command == "2":
        move = random.randrange(5000,12001)
        udis += move
        print("You have traveled",move,"km")
        print()
        o2 += 1
        enginteg += 1
        mdis += random.randrange(7000,14001)

    elif command == "1":
        if cannisters > 0:
            cannisters -= 1
            o2 = 0
        else:
            print("You are out of cannisters.")
            print()

    if o2 > 4 and o2 <= 6:
        print("O2 supply low")
        print()
    elif o2 > 6:
        print("You suffocated.")
        print()
        game = False
        continue

    if enginteg > 5 and enginteg <= 8:
        print("Your engines are beginning to overheat.")
        print()
    elif enginteg > 8:
        print("Your engines exploded.")
        print("You are deafened by the sound, and searing pain envelopes your body.")
        print("A flash of light, and then your world is dark and numb.")
        print("You are dead.")
        game = False
        continue

    if udis >= 200000:
        print("You have safely arrived in federation space.")
        print("Congratulations on a successful voyage!")
        game = False
        continue

    if udis - mdis <= 0:
        print("The marauders caught up to your ship.")
        print("Your vessel is obliterated by a hail of laserfire.")
        print("The marauders dance before your charred remains.")
        game = False
        continue
    elif udis - mdis <= 15000:
        print("The marauders are close behind.")
        print()

    if random.randrange(1,21) == 20:
        print("You found the remnants of a star ship.")
        print("Supplies have been replenished.")
        print("Engines have been cooled.")
        print()
        o2 = 0
        cannisters = 6
        enginteg = 0