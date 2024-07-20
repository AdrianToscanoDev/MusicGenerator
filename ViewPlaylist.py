from UsefulFunctions import addNewLine, clearScreen, getChoiceFrom


def viewPlaylistScreen():
    # TODO: check if playlist is empty
    isEmptyPlaylist()

    # if playlist is empty, show empty screen
    showEmptyPlaylistScreen()

    # if playlist is not empty , display playlist


    # get choice


def showEmptyPlaylistScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- Your Playlist -------------------------------")
    print("|                                                                   |\n"
          "|\t\t Your playlist is currently empty!                            |\n"
          "|\t                                                                |\n"
          "|\ta) Go to Home                                                |\n"
          "|\tb) Add Songs                                                    |\n"
          "|\tq) Quit Program                                                 |\n"
          "|                                                                   |\n"
          "---------------------------------------------------------------------\n")

    # get choice
    # TODO: validate input
    user_choice = input("Enter choice here: ")
    go_to_screen = getChoiceFrom(user_choice,
                                 "Home",
                                 "Add Songs",
                                 "Quit")

    return go_to_screen

def isEmptyPlaylist():
    return True