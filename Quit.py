from UsefulFunctions import addNewLine, clearScreen
def quitScreen():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tThank you for using the app!                                          |\n"
          "-------------------------------------------------------------------------\n")

def errorScreen():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tSorry, there was a problem with the app!                              |\n"
          "|\tPlease try again. Exiting program...                                  |\n"
          "-------------------------------------------------------------------------\n")

# TODO: reset the contents of the playlist and add this to both quitScreen and errorScreen