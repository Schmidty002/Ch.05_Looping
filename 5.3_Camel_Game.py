"""
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

"""
import random

game = True
done = False

print("You are a pilot exploring space.")                                                               # intro
print("A group of marauders has begun to pursue you after you encroached on their territory.")
print("They managed to nick your hull, and several systems were damaged.")
print("The warp gate that leads to federation space is 300,000 km away.")
print("Reach the gate before running out of oxygen, blowing your engines, or being overtaken by the marauders.")
print("l to view additional commands.")
print("Fly well.  No barrel rolls.")
print()

while not done:

    udis = 0                            # variables for supplies and distance
    o2 = 7
    canisters = 2
    enginteg = 9
    mdis = -10000
    repairs = False
    mar = True
    charges = 10
    win = False
    battle = False
    uhp = 10
    ushield = 10
    mhp = 30
    ushieldbroke = False
    udefenseup = False

    while game:

        while game and not battle:
            print("Enter Command")              # available actions
            print("[1] Swap oxygen canister")
            print("[2] Moderate engine power")
            print("[3] Full engine power")
            print("[4] Cut engines")
            print("[5] Status check")
            print("[6] Fire turrets")
            print("[7] Warp to nearest stargate")
            print("[0] Exit Game")
            print("- - -")
            command = input("Enter a command: ")
            print()

            if command == "l":
                print("- - -")
                print("[r] Repair ship")

            elif command == "r":
                if not repairs:
                    repairs = True
                    print("Repairs complete\n")
                else:
                    print("No damage detected\n")

            elif command == "0":                                                                  # exits game
                print("Are you sure you want to quit?  All game data will be lost.")
                print("[Y] or [N]")
                command = input()
                if command.lower() == "y":
                    print("Exiting Game...")
                    game = False
                    win = 8
                    done = True
                    continue
                else:
                    continue

            elif command == "7":                                # warp commands
                if repairs:
                    if mar:
                        print("[Error] Cannot warp while being pursued.\n")
                    else:
                        print("Initiating warp...\n")
                        udis = 300000
                else:
                    print("[Error] Warp drive: " + "\u001b[31m" + "offline" + "\u001b[0m\n")

            elif command == "6":                                        # turret commands
                if repairs:
                    if mar:
                        if charges >= 1:
                            if mdis < 15000:
                                if random.randrange(0, 2) == 1:
                                    print("You destroyed your pursuers.\n")
                                    mar = False
                                    charges -= 1

                                else:
                                    print("You missed.\n")
                                    charges -= 1
                            else:
                                print("[Error] Pursuers out of range.\n")
                        else:
                            print("[Error] Out of charges.\n")
                    else:
                        print("[Error] No targets located\n")
                else:
                    print("[Error] Turrets: " + "\u001b[31m" + "offline" + "\u001b[0m\n")

            elif command == "5":                                            # checks supplies and distances
                print("Distance to warp gate:", 300000-mdis, "km")
                if mar:
                    print("Distance from pursuers:", udis-mdis, "km")
                else:
                    print("No pursuers detected\n")
                print("Engine integrity:", enginteg)
                print("Oxygen levels", o2)
                print("Oxygen canisters remaining:", canisters)
                if not repairs:
                    print("Turrets: " + "\u001b[31m" + "offline" + "\u001b[0m")
                    print("Warp drive: " + "\u001b[31m" + "offline" + "\u001b[0m\n")
                else:
                    print("Turrets: " + "\u001b[32m" + "online" + "\u001b[0m")
                    print("Warp drive: " + "\u001b[32m" + "online" + "\u001b[0m\n")
                continue

            elif command == "4":                            # cuts engines
                if not repairs:
                    enginteg = 9
                if repairs:
                    enginteg = 1000
                print("Your engines have cooled.")
                print()
                if mar:
                    mdis += random.randrange(7000, 12001)

            elif command == "3":                            # full engine power
                move = random.randrange(10000, 14001)
                udis += move
                print("You traveled", move, "km this turn")
                print()
                o2 -= 1
                enginteg -= random.randrange(1, 4)
                if mar:
                    mdis += random.randrange(7000, 12001)

            elif command == "2":                            # moderate engine power
                move = random.randrange(5000, 12001)
                udis += move
                print("You have traveled", move, "km")
                print()
                o2 -= 1
                enginteg -= 1
                if mar:
                    mdis += random.randrange(7000, 12001)

            elif command == "1":                            # replenishes oxygen
                if canisters > 0:
                    canisters -= 1
                    if not repairs:
                        o2 = 7
                    if repairs:
                        o2 = 1000
                else:
                    print("\033[31m" + "You are out of canisters." + "\033[0m")
                    print()

            else:                                                                   # handles non-number inputs
                print("[Command Invalid]\n")
                continue

            if o2 < 3 and o2 >= 1:                                                  # notifies on low oxygen
                print("\033[32m" + "[Warning] " + "\033[0m" + "Oxygen supply low")
                print()
            elif o2 < 1:
                print("You suffocated.")
                print()
                game = False
                continue

            if enginteg < 4 and enginteg >= 1:                                      # notifies on low engine integrity
                print("\033[32m" + "[Warning] " + "\033[0m" + "Your engines are beginning to overheat.")
                print()
            elif enginteg < 1:
                print("Your engines exploded.")
                print("You are deafened by the sound, and searing pain envelopes your body.")
                print("A flash of light, and then your world is dark and numb.")
                print("You are dead.")
                game = False
                continue

            if udis >= 300000:                                              # tests for finished voyage
                print("You have safely arrived in federation space.")
                print("Congratulations on a successful voyage!")
                game = False
                win = True
                continue

            if mar:
                if udis - mdis <= 0:      # tests for marauders catching up
                    if repairs:
                        battle = True
                    else:
                        print("The marauders caught up to your ship.")
                        print("Your vessel is obliterated by a hail of laserfire.")
                        print("The marauders dance before your charred remains.")
                        game = False
                        continue
                elif udis - mdis <= 15000:
                    print("\033[32m" + "[Warning] " + "\033[0m" + "The marauders are close behind.")
                    print()

            if random.randrange(1, 21) == 20:                                # odds of finding a starship
                print("You found the remnants of an ancient star ship.")
                print("Supplies have been replenished.")
                print("Engines have been cooled.")
                print()
                if not repairs:
                    o2 = 7
                    canisters = 2
                    enginteg = 9
                if repairs:
                    o2 = 1000
                    canisters = 2
                    enginteg = 1000

        if game and battle:                             # initiates space battle
            print("[Enemy ship engaged]\n")

        while game and battle:                          # action list
            print("[1] Fire cannons")
            print("[2] Divert power to shields")
            print("[3] Barrel roll")
            print("[4] Status check")
            print("[5] Attempt escape")
            print()
            command = input("Enter a command: ")

            if command == "1":                              # user cannon attack
                print("User used cannons!\n")
                if random.randint(0, 10) > 7:
                    print("Foe Marauders avoided the attack!\n")
                else:
                    damage = random.randint(2, 6)
                    critroll = random.randint(0, 20)
                    if critroll == 20:
                        print("A critical hit!\n")
                        damage *= 2
                        mhp -= damage
                        print("Foe Marauders took", damage, "damage!\n")
                    else:
                        mhp -= damage
                        print("Foe Marauders took", damage, "damage!\n")

            elif command == "2":                                # user shield boosts
                print("User used shield!\n")
                if ushieldbroke:
                    print("\033[32m" + "[Error]" + "\033[0m", "Shields offline\n")
                    continue
                else:
                    udefenseup = True

            elif command == "3":                            # disobedience will be punished
                print("You exploded in a fiery column of death.")
                print("I told you no barrel rolls.\n")
                game = False
                continue

            elif command == "4":                                    # status check
                print("HP: ", uhp, "/10", sep="")
                print("Shields: ", ushield, "/10", sep="")
                print("Enemy HP: ", mhp, "/30", sep="")
                print()
                continue

            elif command == "5":                                    # attempts escape from battle
                print("You tried to run away.")
                print()
                if random.randrange(0, 10) > 7:
                    print("Got away safely!")
                    print()
                    battle = False
                    udis += 1000
                    continue
                else:
                    print("Can't escape!")
                    print()

            else:                                                   # Jake-proofing
                print("[Command Invalid]")
                print()
                continue

            if mhp <= 0:                                            # tests for signs of life
                mar = False
                battle = False
                mdis = 0

            if mar:
                print("Foe Marauders used cannons!")                # enemy cannon attack
                print()
                if random.randint(0, 10) > 3:
                    damage = random.randint(2, 5)
                    if udefenseup:
                        damage //= 2
                        udefenseup = False
                    if not ushieldbroke:
                            if damage >= ushield and not ushieldbroke:
                                damage -= ushield
                                ushield = 0
                                uhp -= damage
                                print("Your shields were destroyed!")
                                print()
                                ushieldbroke = True
                                if damage > 0:
                                    print("You took", damage, "damage!")
                                    print()
                            else:
                                ushield -= damage
                                print("Your shields took", damage, "damage!")
                                print()
                    else:
                        uhp -= damage
                        print("You took", damage, "damage!")
                        print()
                else:
                    print("Foe Marauders' attack missed!")
                    print()
            else:
                print("Foe Marauders were defeated!")
                print()
                continue

            if uhp <= 0:                                        # death note
                print("Glancing at the side of your monitor, you see a picture of you sitting with you two children.")
                print("Tommy is 7, and last you saw him he was building a model spaceship,")
                print("so he could be just like [insert parental title affiliated with user's gender].")
                print()
                print("Emma is 12.  She wouldn't talk to you before you left, because she didn't want you to go.")
                print("These thoughts are the last things that go through your mind before your vision fades to")
                print("blinding white, your body engulfed in searing pain, and then there is cold, dark, nothing.")
                print()
                print("You have died.")
                game = False
                continue

    if not win:
        print("\033[31m" + "\nGAME OVER" + "\033[0m")
        print()

    print("Would you like to play again?")
    print("[Y] or [N]")
    command = input().lower()
    if command == "y":
        game = True
        continue

    elif command == "n":
        done = True
        continue

    else:
        print("[Command invalid]")
        continue
