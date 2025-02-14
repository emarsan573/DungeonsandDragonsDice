# import random
# define a function to roll a die
# create a dictionary that will have the drawings of the die being rolled

import random

dice_drawing = {
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


def roll_dice():
    roll = input("Roll the dice? (y/n) : ")

    while roll.lower() == "y".lower():
        dice1 = random.randint(1, 4)

        print("die rolled {}".format(dice1))
        print("\n".join(dice_drawing[dice1]))

        roll = input("\nRoll again? (y/n): ")

        rollagain = input("roll this die again? (y/n) : ")           





roll_dice()
