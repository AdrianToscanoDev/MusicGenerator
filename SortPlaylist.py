from UsefulFunctions import addNewLine, clearScreen


def sortPlaylistScreen_success():
    addNewLine(40)
    clearScreen()
    print("-----------------------------------------------------------------------------------")
    print("|                                                                                   |\n"
          "|\tPlaylist has been sorted!                                                   |\n"
          "|\t                                                                            |\n"
          "|\ta) Home                                                                     |\n"
          "|\tb) View Playlist                                                            |\n"
          "|\tc) Quit                                                                     |\n"
          "|                                                                                   |\n"
          "-----------------------------------------------------------------------------------\n")


def sortPlaylistScreen_failed_addMore():
    addNewLine(40)
    clearScreen()
    print("-----------------------------------------------------------------------------------")
    print("|                                                                                   |\n"
          "|\tThe playlist has less than 2 songs. Please add at least 2 songs to sort:)        |\n"
          "|\t                                                                            |\n"
          "|\ta) Home                                                                     |\n"
          "|\tb) Add songs                                                                |\n"
          "|\tc) Quit                                                                     |\n"
          "|                                                                                   |\n"
          "-----------------------------------------------------------------------------------\n")


def sortPlaylistScreen_failed_error():
    addNewLine(40)
    clearScreen()
    print("-----------------------------------------------------------------------------------")
    print("|                                                                                   |\n"
          "|\tSorry, there was an error sorting the playlist.                             |\n"
          "|\t                                                                            |\n"
          "|\ta) Home                                                                     |\n"
          "|\tb) View Playlist                                                            |\n"
          "|\tc) Quit                                                                     |\n"
          "|                                                                                   |\n"
          "-----------------------------------------------------------------------------------\n")


def sortPlaylist():
    # communicate with my teammates microservice (aka - setup my zeroMQ socket)
    pass
    # send a request to the microservice

    # wait for a response

    # return 1 if not successful
    # or return 0 if successful
