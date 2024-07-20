from UsefulFunctions import clearScreen, addNewLine, getChoiceFrom


def homeScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- HOME -------------------------------")
    print("|                                                                   |\n"
          "|\tWhat would you like to do?                                      |\n"
          "|\t                                                                |\n"
          "|\ta) View Playlist                                                |\n"
          "|\tb) Add Songs                                                    |\n"
          "|\tc) Quick Fill Playlist                                          |\n"
          "|\tq) Quit Program                                                 |\n"
          "|                                                                   |\n"
          "---------------------------------------------------------------------\n")

    # get choice
    #TODO: validate input
    user_choice = input("Enter choice here: ")
    go_to_screen = getChoiceFrom(user_choice,
                                 "View Playlist",
                                 "Add Songs",
                                 "Quick Fill Playlist",
                                 "Quit")

    return go_to_screen
