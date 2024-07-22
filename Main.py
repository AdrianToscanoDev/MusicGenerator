from UsefulFunctions import getInputFrom
from Home import homeScreen
from Welcome import welcomeScreen
from ViewPlaylist import viewPlaylistScreen
from AddSongs import addSongsScreen, addSongsSuccess
from QuickFillPlaylist import quickFillPlaylistScreen
from Quit import quitScreen, errorScreen

def main():

    # display a welcome screen
    welcomeScreen()

    # display home screen
    homeScreen()
    user_choice = getInputFrom("HomeScreen")

    # main program loop
    while user_choice != "Quit":

        if user_choice == "Home":
            homeScreen()
            user_choice = getInputFrom("HomeScreen")

        elif user_choice == "View Playlist":
            viewPlaylistScreen()
            user_choice = getInputFrom("ViewPlaylistScreen")

        elif user_choice == "Add Songs":
            addSongsScreen()
            user_choice = getInputFrom("AddSongsScreen")

        elif user_choice == "Add 5 songs" or user_choice == "Add 10 songs":
            addSongsSuccess()
            user_choice = getInputFrom("AddSongsSuccess")

        elif user_choice == "Quick Fill Playlist":
            quickFillPlaylistScreen()
            user_choice = getInputFrom("QuickFillPlaylistScreen")

        else:
            errorScreen()
            user_choice = "Quit"

    # end program
    quitScreen()

if __name__ == "__main__":
    main()
