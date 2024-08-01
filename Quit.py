from UsefulFunctions import addNewLine, clearScreen
def quitScreen():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tThank you for using the app!                                     |\n"
          "-------------------------------------------------------------------------\n")

def errorScreen():
    addNewLine(40)
    clearScreen()
    print("-------------------------------------------------------------------------")
    print("|\tSorry, there was a problem with the app!                              |\n"
          "|\tPlease try again...                                  |\n"
          "-------------------------------------------------------------------------\n")