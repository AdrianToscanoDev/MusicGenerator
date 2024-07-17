from UsefulFunctions import clearScreen, addNewLine
from Home import homeScreen
from Welcome import welcomeScreen


def main():

    # display awelcome screen
    user_choice = welcomeScreen()

    # main program loop
    while user_choice != 'q':

        go_to_screen = homeScreen()

        # decide which screen to go to
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
