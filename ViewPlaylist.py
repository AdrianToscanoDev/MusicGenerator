import json

from UsefulFunctions import addNewLine, clearScreen

import zmq


def viewPlaylistScreen():
    addNewLine(40)
    clearScreen()
    print("------------------------------- Your Playlist -------------------------------\n")

    print(request_playlist())

    # display options
    addNewLine(2)
    print("a) Home\n"
          "b) Add Songs\n"
          "c) Quit\n")
    print("------------------------------------------------------------------------------\n")


def request_playlist():
    # connect to server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4233")

    # send request
    request = "G"
    byte_request = request.encode('utf-8')
    socket.send(byte_request)

    # decode reply when received
    byte_response = socket.recv()
    playlist = byte_response.decode('utf-8')

    # return the playlist
    return playlist
