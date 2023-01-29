import random
import time
import webbrowser

def joke():
    print("") #deadspace
    print(random.choice(open("jokes.txt").readlines()))
    print("     (⌐■_■)╯")

def webpage():
    print("Webpage will open in your default browser...")
    time.sleep(1)
    webbrowser.open_new("https://www.online-python.com/zXS3x7hk6l")

def info():
    print("\nDice Roll is a simple Python program written to showcase the functions of using loops, sleep,\nand random integers. It was written by Jared Barney on January 27th, 2022. V6 updated 2022-02-08.")

def error():
    print("""\nYou must enter a whole number for each value. Enter "help" for more information.""")

def exitprogram():
    print("This program will close in 5 seconds. Bye!")
    time.sleep(5)
    quit()

def help():
    with open('help.txt') as h:
        help = h.read()
        print(help)

def welcome():
    with open('welcome.txt') as w:
        welcome = w.read()
        print(welcome)
