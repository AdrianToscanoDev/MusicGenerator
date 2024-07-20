import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addNewLine(amount):
    for i in range(amount):
        print()

"""
name: getChoiceFrom

This function accepts the users choice, and then the options of the current screen, in order. 
It returns the name of the option that the user chose.
*note* if the function returns none, this implies an error
(none means this option was not an available option to the user)
"""
def getChoiceFrom(userChoice, optionA = "none", optionB = "none", optionC = "none", optionD = "none", optionE = "none"):

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