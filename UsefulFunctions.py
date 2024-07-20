import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addNewLine(amount):
    for i in range(amount):
        print()

def getChoiceFrom(userChoice, optionA = "none", optionB = "none", optionC = "none", optionD = "none"):

    if userChoice == 'q':
        return "Quit"
    elif userChoice == 'a':
        return optionA
    elif userChoice == 'b':
        return optionB
    elif userChoice == 'c':
        return optionC
    elif userChoice == 'd':
        return optionD


"""
a) View Playlist
b) Add songs
c) Quick fill playlist
d) Go back to home
q) Quit program
"""