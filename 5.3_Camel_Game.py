'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

game = True
print("You are a pilot exploring space.")                                                               #intro
print("A group of marauders has begun to pursue you after you encroached on their territory.")
print("They managed to nick your hull, and you are leaking oxygen.")
print("The warp gate that leads to federation space is 200,000 km away.")
print("Reach the gate before running out of oxygen, blowing your engines, or being overtaken by the marauders.")
print("Fly well.  No barrel rolls.")
print()

udis = 0                            #variables for supplies and distance
o2 = 7
canisters = 2
enginteg = 9
mdis = -10000

while game:
    print("Enter Command")                      #available actions
    print("[1] Swap oxygen canister")
    print("[2] Moderate engine power")
    print("[3] Full engine power")
    print("[4] Cut engines")
    print("[5] Status check")
    print("[0] Exit Game")
    command = input("Command: ")
    print()

    if command == "0":                                                                  #exits game
        print("Are you sure you want to quit?  All game data will be lost.")
        print("[Y] or [N]")
        command = input()
        if command.lower() == "y":
            print("Exiting Game...")
            game = False
            continue
        else:
            continue

    elif command == "5":                                            #checks supplies and distances
        print("Distance to warp gate:",300000-mdis,"km")
        print("Engine integrity:",enginteg)
        print("Oxygen levels",o2)
        print("Oxygen canisters remaining:",canisters)
        print("Distance from pursuers:",udis-mdis,"km")
        continue

    elif command == "4":                            #cuts engines
        enginteg = 9
        print("Your engines have cooled.")
        print()
        mdis += random.randrange(7000,12001)

    elif command == "3":                            #full engine power
        move = random.randrange(10000,14001)
        udis += move
        print("You traveled",move,"km")
        print()
        o2 -= 1
        enginteg -= random.randrange(1,4)
        mdis += random.randrange(7000,12001)

    elif command == "2":                            #moderate engine power
        move = random.randrange(5000,12001)
        udis += move
        print("You have traveled",move,"km")
        print()
        o2 -= 1
        enginteg -= 1
        mdis += random.randrange(7000,12001)

    elif command == "1":                            #replenishes oxygen
        if canisters > 0:
            canisters -= 1
            o2 = 7
        else:
            print("\033[0;31;48m" + "You are out of canisters." + "\033[0;38;48m")
            print()

    if o2 < 3 and o2 >= 1:                                                  #notifies on low oxygen
        print("\033[0;31;48m" + "Oxygen supply low" + "\033[0;38;48m")
        print()
    elif o2 < 1:
        print("You suffocated.")
        print()
        game = False
        continue

    if enginteg < 4 and enginteg >= 1:                                      #notifies on low engine integrity
        print("\033[0;32;48m" + "Your engines are beginning to overheat." + "\033[0;38;48m")
        print()
    elif enginteg < 1:
        print("Your engines exploded.")
        print("You are deafened by the sound, and searing pain envelopes your body.")
        print("A flash of light, and then your world is dark and numb.")
        print("You are dead.")
        game = False
        continue

    if udis >= 300000:                                              #tests for finished voyage
        print("You have safely arrived in federation space.")
        print("Congratulations on a successful voyage!")
        game = False
        continue

    if udis - mdis <= 0:                                            #tests for marauders catching up
        print("The marauders caught up to your ship.")
        print("Your vessel is obliterated by a hail of laserfire.")
        print("The marauders dance before your charred remains.")
        game = False
        continue
    elif udis - mdis <= 15000:
        print("The marauders are close behind.")
        print()

    if random.randrange(1,21) == 20:                                #odds of finding a starship
        print("You found the remnants of an ancient star ship.")
        print("Supplies have been replenished.")
        print("Engines have been cooled.")
        print()
        o2 = 7
        canisters = 2
        enginteg = 9