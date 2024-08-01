from UsefulFunctions import clearScreen, clearPlaylist


def welcomeScreen():
    clearScreen()
    clearPlaylist()  # clear playlist everytime app is run
    print("-------------------- WELCOME TO MUSIC GENERATOR --------------------")
    print("|                                                                   |\n"
          "|\tThis app helps you discover new music in an easy way!       |\n"
          "|\t                                                            |\n"
          "|\tWe create a playlist for you (it will be empty at first),   |\n"
          "|\tand you can view it or add songs to it!                     |\n"
          "|                                                                   |\n"
          "|\tThat way, you don't need to write anything down and you get |\n"
          "|\tnew music to explore in a couple clicks!                    |\n"
          "|\t                                                            |\n"
          "|\t(Please note that the playlist can only hold a maximum      |\n"
          "|\tof 50 songs. Songs can only be added 5 or 10                |\n"
          "|\tat a time)                                                  |\n"
          "|                                                                   |\n"
          "|\tPress the enter key to continue                             |\n"
          "|                                                                   |\n"
          "---------------------------------------------------------------------\n")
    input()
