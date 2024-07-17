from UsefulFunctions import clearScreen, addNewLine


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
          "|\td) Go back to Home                                              |\n"
          "|\tq) Quit Program                                                 |\n"
          "|                                                                   |\n"
          "---------------------------------------------------------------------\n")

    # get choice
    user_choice = input("Enter choice here: ")
    go_to_screen = "none"

    if user_choice == 'a':
        go_to_screen = "View Playlist"
    elif user_choice == 'b':
        go_to_screen = "Add Songs"
    elif user_choice == 'c':
        go_to_screen = "Quick Fill Playlist"
    elif user_choice == 'd':
        go_to_screen = "Home"
    elif user_choice == 'q':
        go_to_screen = "Quit"

    return go_to_screen
