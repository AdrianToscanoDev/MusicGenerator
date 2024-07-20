from UsefulFunctions import clearScreen, addNewLine, getChoiceFrom
from Home import homeScreen
from Welcome import welcomeScreen


def main():

    # display a welcome screen
    user_choice = welcomeScreen()

    # main program loop
    while user_choice != 'q':

        # default to home screen
        go_to_screen = homeScreen()

        # decide which screen to go to from the home screen
        if go_to_screen == "View Playlist":
            print("View Playlist")
        elif go_to_screen == "Add Songs":
            print("Add Songs")
        elif go_to_screen == "Quick Fill Playlist":
            print("Quick Fill Playlist")
        elif go_to_screen == "Home":
            print("Home")
        elif go_to_screen == "Quit":
            print("Quit")

    # end program
    addNewLine(40)
    print("Thanks for using the app!\n")


if __name__ == "__main__":
    main()
