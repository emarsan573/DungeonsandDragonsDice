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
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  1   \|",
        "/________\ ",
    ),
    2: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  2   \|",
        "/________\ ",
    ),
    3: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  3   \|",
        "/________\ ",
    ),
    4: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  4   \|",
        "/________\ ",
    ),
    5: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  5   \|",
        "/________\ ",
    ),
    6: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  6   \|",
        "/________\ ",
    ),
    7: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  7   \|",
        "/________\ ",
    ),
    8: (
        "  / /\ \   ",
        " / /  \ \ ",
        "| /    \ |",
        "|/  8   \|",
        "/________\ ",
    ),
}







    while roll.lower() == "y".lower():
        dice1 = random.randint(1, 8)
        dice2 = random.randint(1, 8)
=======
            print("die rolled {}".format(dice1))
            print("\n".join(dice_drawing2[dice1]))
            rollagain = input("roll this die again? (y/n) : ")           




roll_dice()
