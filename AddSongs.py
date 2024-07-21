from UsefulFunctions import addNewLine, clearScreen

def addSongsScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- ADD SONGS -------------------------------")
    print("|                                                                        |\n"
          "|\tHow many songs would you like to add to your playlist?               |\n"
          "|\t                                                                     |\n"
          "|\ta) Add 5 songs                                                       |\n"
          "|\tb) Add 10 songs                                                      |\n"
          "|\tc) Home                                                              |\n"
          "|\tq) Quit                                                              |\n"
          "|                                                                        |\n"
          "-------------------------------------------------------------------------\n")

def addSongsSuccess():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tSongs were successfully added!                                        |\n"
          "|                                                                        |\n"
          "|\ta) Home                                                               |\n"
          "|\tb) View Playlist                                                      |\n"
          "|\tc) Quit                                                               |\n"
          "-------------------------------------------------------------------------\n")