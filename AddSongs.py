from UsefulFunctions import addNewLine, clearScreen


def addSongsScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- ADD SONGS -------------------------------")
    print("|                                                                            |\n"
          "|\tHow many songs would you like to add to your playlist?               |\n"
          "|\t                                                                     |\n"
          "|\ta) Add 5 songs                                                       |\n"
          "|\tb) Add 10 songs                                                      |\n"
          "|\tc) Home                                                              |\n"
          "|\td) Quit                                                              |\n"
          "|                                                                            |\n"
          "-------------------------------------------------------------------------\n")


"""
reads 5 songs from the songs.txt file
"""
def add5(totalSongsGenerated):
    with open("songs.txt", "r") as songsFile:
        # save contents of the file as a list
        songs = songsFile.readlines()
    songsFile.close()

    # Read the first line of the playlist
    with open("playlist.txt", "r") as playlistFile:
        firstLine = playlistFile.readline().strip()

    # if it's the first time adding to the playlist, open in 'w' mode
    if firstLine == "Your playlist is currently empty!":

        # empty the contents of the file
        with open("playlist.txt", "w") as playlistFile:
            pass
        playlistFile.close()

        # add the first 5 songs
        with open("playlist.txt", "w") as playlistFile:
            # write the first 5 lines to the playlist
            for i in range(5):
                playlistFile.write(songs[i])
        playlistFile.close()

    # if it's not the first time adding to the playlist, append to it in 'a' mode
    else:
        # determine where in the songs.txt file you are going to start reading from
        startPosition = totalSongsGenerated

        # append them to the playlist
        with open("playlist.txt", "a") as playlistFile:
            # write the next 5 lines starting at the correct place
            for i in range(startPosition, startPosition + 5):
                playlistFile.write(songs[i])
        playlistFile.close()

def add10(totalSongsGenerated):
    with open("songs.txt", "r") as songsFile:
        # save contents of the file as a list
        songs = songsFile.readlines()
    songsFile.close()

    # Read the first line of the playlist
    with open("playlist.txt", "r") as playlistFile:
        firstLine = playlistFile.readline().strip()

    # if it's the first time adding to the playlist, open in 'w' mode
    if firstLine == "Your playlist is currently empty!":

        # empty the contents of the file
        with open("playlist.txt", "w") as playlistFile:
            pass
        playlistFile.close()

        # add the first 10 songs
        with open("playlist.txt", "w") as playlistFile:
            # write the first 10 lines to the playlist
            for i in range(10):
                playlistFile.write(songs[i])
        playlistFile.close()

    # if it's not the first time adding to the playlist, append to it in 'a' mode
    else:
        # determine where in the songs.txt file you are going to start reading from
        startPosition = totalSongsGenerated

        # append them to the playlist
        with open("playlist.txt", "a") as playlistFile:
            # write the next 10 lines starting at the correct place
            for i in range(startPosition, startPosition + 10):
                playlistFile.write(songs[i])
        playlistFile.close()

def addSongsSuccess():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tSongs were successfully added!                                   |\n"
          "|                                                                        |\n"
          "|\ta) Home                                                          |\n"
          "|\tb) View Playlist                                                 |\n"
          "|\tc) Quit                                                          |\n"
          "-------------------------------------------------------------------------\n")


def printFullMessage():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tYour playlist is already full!                                        |\n"
          "|                                                                        |\n"
          "|\ta) Home                                                               |\n"
          "|\tb) View Playlist                                                      |\n"
          "|\tc) Quit                                                               |\n"
          "-------------------------------------------------------------------------\n")
def printMaxedOutMessage():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tAdding these songs will overflow the playlist!                        |\n"
          "|                                                                        |\n"
          "|\tPlease try again!                                                     |\n"
          "|\ta) Home                                                               |\n"
          "|\tb) View Playlist                                                      |\n"
          "|\tc) Quit                                                               |\n"
          "-------------------------------------------------------------------------\n")