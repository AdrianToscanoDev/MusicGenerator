import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addNewLine(amount):
    for i in range(amount):
        print()