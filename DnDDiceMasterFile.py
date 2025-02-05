# import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice

import random

dice_drawing = {
    1: (
        "   / /\ \ ",
        "  /_/ 1\_\  ",
        "  \__\/__/  ",
    ),
    2: (
        "   / /\ \ ",
        "  /_/ 2\_\  ",
        "  \__\/__/  ",
    ),
    3: (
        "   / /\ \ ",
        "  /_/ 3\_\  ",
        "  \__\/__/  ",
    ),
    4: (
        "   / /\ \ ",
        "  /_/ 4\_\  ",
        "  \__\/__/  ",
    ),   
    5: (
        "   / /\ \ ",
        "  /_/ 5\_\  ",
        "  \__\/__/  ",
    ),
    6: (
        "   / /\ \ ",
        "  /_/ 6\_\  ",
        "  \__\/__/  ",
    ),
    7: (
        "   / /\ \ ",
        "  /_/ 7\_\  ",
        "  \__\/__/  ",
    ),
    8: (
        "   / /\ \ ",
        "  /_/ 8\_\  ",
        "  \__\/__/  ",
    ),
    9: (
        "   / /\ \ ",
        "  /_/ 9\_\  ",
        "  \__\/__/  ",
    ),
    10: (
        "   / /\ \ ",
        "  /_/10\_\  ",
        "  \__\/__/  ",
    ),
}

def roll_dice():
    roll = input("Roll the dice? (y/n) : ")

    while roll.lower() == "y".lower():
        dice1 = random.randint(1, 10)
        dice2 = random.randint(1, 10)

        print("dice rolled {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("\nRoll again? (y/n): ")


roll_dice()
