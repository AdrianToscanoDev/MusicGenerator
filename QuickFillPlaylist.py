from UsefulFunctions import addNewLine, clearScreen


def confirmationScreen():
    addNewLine(40)
    clearScreen()
    print("--------------------------- Please confirm your selection --------------------------")
    print("|                                                                                   |\n"
          "|\tAre you sure you would like to fill the playlist?                           |\n"
          "|\t                                                                            |\n"
          "|\tYou will be unable to add songs,                                            |\n"
          "|\tand you will need to restart the app to add more                            |\n"
          "|\t                                                                            |\n"
          "|\ta) Yes, fill the playlist                                                   |\n"
          "|\tb) No, don't fill the playlist                                              |\n"
          "|                                                                                   |\n"
          "-----------------------------------------------------------------------------------\n")

def quickFillPlaylistScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- Quick Fill Playlist -------------------------------")
    print("|                                                                                   |\n"
          "|\tYour playlist has been filled! You will be unable to                        |\n"
          "|\tadd additional songs.                                                       |\n"
          "|\t                                                                            |\n"
          "|\tIf you would like to add more songs, select Quit                            |\n"
          "|\tand restart the app!:)                                                      |\n"
          "|\t                                                                            |\n"
          "|\ta) Home                                                                     |\n"
          "|\tb) Quit                                                                     |\n"
          "|                                                                                   |\n"
          "-----------------------------------------------------------------------------------\n")

def quickFill(totalSongsGenerated):
    # get the remainder of songs left to add
    leftTofill = 50 - totalSongsGenerated

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

        # add the entire song.txt file to the playlist
        with open("playlist.txt", "w") as playlistFile:
            # write the first 5 lines to the playlist
            for i in range(50):
                playlistFile.write(songs[i])
        playlistFile.close()

    # if it's not the first time adding to the playlist, append to it in 'a' mode
    else:
        # determine where in the songs.txt file you are going to start reading from
        startPosition = totalSongsGenerated

        # append them to the playlist
        with open("playlist.txt", "a") as playlistFile:
            # write the next 5 lines starting at the correct place
            for i in range(startPosition, startPosition + leftTofill):
                playlistFile.write(songs[i])
        playlistFile.close()
