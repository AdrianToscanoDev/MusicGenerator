from UsefulFunctions import addNewLine

def viewPlaylistScreen():
    addNewLine(40)
    print("------------------------------- Your Playlist -------------------------------\n")

    # display playlist
    with open('playlist.txt', 'r') as file:
        contents = file.read()
        print(contents)
    file.close()

    # display options
    addNewLine(2)
    print("a) Home\n"
          "b) Add Songs\n"
          "c) Quit\n")
    print("------------------------------------------------------------------------------\n")