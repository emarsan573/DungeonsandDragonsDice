# import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice

import random

####d4#####

dice_drawing1 = {
    1: (
        "    /\     ",
        "   /  \    ",
        "  /    \   ",
        " /  1   \  ",
        "/________\ ",
    ),
    2: (
        "    /\     ",
        "   /  \    ",
        "  /    \   ",
        " /  2   \  ",
        "/________\ ",
    ),
    3: (
        "    /\     ",
        "   /  \    ",
        "  /    \   ",
        " /  3   \  ",
        "/________\ ",
    ),
        4: (
        "    /\     ",
        "   /  \    ",
        "  /    \   ",
        " /  4   \  ",
        "/________\ ",
    ),
}

####d6####

dice_drawing2 = {
    1: (
        " __________",
        "|          |",
        "|    1     |",
        "|     ●    |",
        "|          |",
        "|__________|",
    ),
    2: (
        " __________",
        "|          |",
        "|       ●  |",
        "|    2     |",
        "|  ●       |",
        "|__________|",
    ),
    3: (
        " __________",
        "|          |",
        "|   3  ●   |",
        "|    ●     |",
        "|  ●       |",
        "|__________|",
    ),
    4: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|    4     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    5: (
        " __________",
        "|          |",
        "|  ● 5  ●  |",
        "|    ●     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    6: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|  ●  6 ●  |",
        "|  ●    ●  |",
        "|__________|",
    ),
}






def roll_dice():
    roll = input("Which die would you like to roll (d4 d6) : ")

    if roll.lower() == "d4".lower() or "d6".lower():
        if roll.lower() == "d4".lower*():
            dice1 = random.randint(1, 4)

            print("die rolled {}".format(dice1))
            print("\n".join(dice_drawing1[dice1]))
            #rollagain1 = input("roll this die again? (y/n) : ")

        if roll.lower() == "d6".lower*():
            dice1 = random.randint(1, 6)

            print("die rolled {}".format(dice1))
            print("\n".join(dice_drawing2[dice1]))
    #if roll.lower() == "d6".lower():
        #dice2 = random.randint(1, 6)

        #print("die rolled {}".format(dice2))
        #print("\n".join(dice_drawing2[dice2]))
        #print("\n".join(dice_drawing[dice2]))

        #roll = input("\nRoll again? (y/n): ")


roll_dice()
