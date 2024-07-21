import os

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addNewLine(amount):
    for i in range(amount):
        print()

"""
Gets input from the user. screen parameter is used to decide from which set of options to choose from 
"""
def getInputFrom(screen):

    global go_to_screen

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
