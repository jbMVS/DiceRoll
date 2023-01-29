import random
from dicerollfunc import *

dice = ""
amount = ""

def yesdice():
    print("") # deadspace
    for x in range(0,int(amount)):
        result = random.randint(1, int(dice))
        if int(result) == int(dice) and int(dice) > 2: # last number is dice to exclude from crits, right now it's 2 and below
            critcheck = ("  (╯°□°)╯ - CRITICAL ROLL!!!")
        elif int(result) == 1 and int(dice) > 2:
            critcheck = ("  ('╥_╥)  - CRITICAL MISS...")
        elif int(result) != int(dice) or 1:
            critcheck = ""
        print(str(x + 1) + ": You rolled a " + str(result) + " on a d" + str(dice) + "." + critcheck)

def nodice():
    if (dice == "help") or (dice == "?") or (amount == "help") or (amount == "?"):
        help()
    elif dice == "joke" or amount == "joke":
        joke()
    elif dice == "info" or amount == "info":
        info()
    elif dice == "welcome" or amount == "welcome":
        welcome()
    elif dice == "exit" or amount == "exit":
        exitprogram()
    elif dice == "web" or amount == "web":
        webpage()
    elif (dice == "0") or (amount == "0") or (dice.isnumeric() == False) or (amount.isnumeric() == False):
        error()

welcome()

while True:
    dice = input("\n- How many sides? Example: type ""6"" and press Enter to roll a d6.\n> ")
    if dice.isnumeric() == True and dice != "0":
        amount = input("- How many dice? Enter the number of dice you wish to roll.\n> ")
        if amount.isnumeric() == True and amount != "0":
            yesdice()
        else:
            nodice()
    else:
        nodice()
