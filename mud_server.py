"""
small_mud.py

A small beginning of a MUD, Multi User Dungeon, game.
"""

Current_room = 0

description = [
    "You see a typical class room with a white-board in front of you.",
    "You are in a corridor at University West.",
    "You see a restaurant where people eat lunch.",
    "you see a toilet you cannot run away"]

def parse_and_execute(command):
    global Current_room
    print command
    if command == "look" or command == "l":
        return description[Current_room]
    if command == "go west" or command == "w":
        if Current_room < 3:
            Current_room += 1
            return "You walk west!"
        if Current_room == 3:
            Current_room = 0
            return "Congratulations, you espaced the building! Game over!"
        else:
            return "You bump into the wall!"
    if command == "go east" or command == "e":
        if Current_room > 0:
            Current_room -= 1
            return "You walk east!"
        return "You bump into the wall!"
    return "I don't understand your command!"

# Echo server program

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name

server.register_function(parse_and_execute, 'data')

# Run the server's main loop
server.serve_forever()


