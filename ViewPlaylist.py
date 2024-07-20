from UsefulFunctions import addNewLine, clearScreen, getChoiceFrom


def viewPlaylistScreen():
    # check if playlist is empty
    showEmptyPlaylistScreen()

    # if playlist is empty, show empty screen

    # if playlist is not empty , display playlist

    # get choice


def showEmptyPlaylistScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- HOME -------------------------------")
    print("|                                                                   |\n"
          "|\t\t Your playlist is currently empty!                            |\n"
          "|\t                                                                |\n"
          "|\ta) Go to Home                                                |\n"
          "|\tb) Add Songs                                                    |\n"
          "|\tq) Quit Program                                                 |\n"
          "|                                                                   |\n"
          "---------------------------------------------------------------------\n")

    # get choice
    user_choice = input("Enter choice here: ")
    go_to_screen = getChoiceFrom(user_choice,
                                 "Home",
                                 "Add Songs",
                                 "Quit")

    return go_to_screen
