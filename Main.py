from UsefulFunctions import getInputFrom
from Home import homeScreen
from Welcome import welcomeScreen
from ViewPlaylist import viewPlaylistScreen
from AddSongs import addSongsScreen, add5, add10, addSongsSuccess, printFullMessage, printMaxedOutMessage
from QuickFillPlaylist import quickFillPlaylistScreen, quickFill
from Quit import quitScreen, errorScreen

def main():

    # display a welcome screen
    welcomeScreen()

    # display home screen
    homeScreen()
    user_choice = getInputFrom("HomeScreen")

    # keeps track of how many songs have been added to the playlist
    totalSongsGenerated = 0

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

        elif user_choice == "Add 5 songs":
            if totalSongsGenerated + 5 <= 50:
                add5(totalSongsGenerated)
                addSongsSuccess()
                totalSongsGenerated = totalSongsGenerated + 5
                user_choice = getInputFrom("AddSongsSuccess")
            else:
                printFullMessage()
                user_choice = getInputFrom("PlaylistFullMessage")

        elif user_choice == "Add 10 songs":
            if totalSongsGenerated + 10 <= 50:
                add10(totalSongsGenerated)
                addSongsSuccess()
                totalSongsGenerated = totalSongsGenerated + 10
                user_choice = getInputFrom("AddSongsSuccess")
            elif totalSongsGenerated + 10 > 50:
                printMaxedOutMessage()
                user_choice = getInputFrom("PlaylistFullMessage")
            else:
                printFullMessage()
                user_choice = getInputFrom("PlaylistFullMessage")

        elif user_choice == "Quick Fill Playlist":
            quickFill(totalSongsGenerated)
            quickFillPlaylistScreen()
            totalSongsGenerated = 50
            user_choice = getInputFrom("QuickFillPlaylistScreen")

        else:
            errorScreen()
            user_choice = "Quit"

    # end program
    quitScreen()

if __name__ == "__main__":
    main()
