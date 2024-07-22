import os

"""
function is used to help format the terminal window
"""
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

"""
function is used to help format the terminal window.
adds new lines to the terminal, specified by the parameter "amount".
"""
def addNewLine(amount):
    for i in range(amount):
        print()

"""
ensures input is valid.

rangeMax is the high end of the range of options.
for example: passing 'c' for rangeMax means that 
input should not be higher in the alphabet than 'c' (aka not d or more)
"""
def validateInput(userInput, rangeMax):

    # make sure input is 1 single char
    userInputLength = len(userInput)
    if userInputLength != 1:
        print("Invalid input! Please enter from one of the options available.")

    # make sure input is within the range from [a, rangeMax]
    a_in_ascii = 61
    rangeMax_in_ascii = ord(rangeMax)
    userInput_in_ascii = ord(userInput)

    if userInput_in_ascii < a_in_ascii or userInput_in_ascii > rangeMax_in_ascii:
        print("Invalid input! Please choose an option from a to ", rangeMax, "\n")

"""
Gets input from the user. screen parameter is used to decide from which set of options to choose from 
"""
def getInputFrom(screen):

    go_to_screen = "error"

    user_input = input("Enter choice here: \n")

    if screen == "HomeScreen":
        go_to_screen = getChoiceFrom(user_input,
                                     "View Playlist",
                                     "Add Songs",
                                     "Quick Fill Playlist",
                                     "Quit")
    elif screen == "ViewPlaylistScreen":
        go_to_screen = getChoiceFrom(user_input,
                                     "Home",
                                     "Add Songs",
                                     "Quit")
    elif screen == "AddSongsScreen":
        go_to_screen = getChoiceFrom(user_input,
                                     "Add5",
                                     "Add10",
                                     "Home",
                                     "Quit")
    elif screen == "QuickFillPlaylistScreen":
        go_to_screen = getChoiceFrom(user_input,
                                     "Home",
                                     "Quit")

    elif screen == "AddSongsSuccess":
        go_to_screen = getChoiceFrom(user_input,
                                     "Home",
                                     "View Playlist",
                                     "Quit")

    return go_to_screen

"""
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
