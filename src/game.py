#!/usr/bin/env python
'''
wait for connection from player
main loop:
    update display
    send game state to player AI
    wait for moves from player AI
    send game state to cat AI
    wait for moves from cat AI
'''
import server
import level
import cat_ai
from display import *

lvl = level.generateLevel(21, 63)
server = server.Server()
cat = cat_ai.CatAI()

D = level.createAdjList(lvl, TERRAIN_FLOOR)

print "Waiting for client to connect..."
server.start()
print "Client connected..."
print "Initializing display..."

S = initDisplay()


while server.running:
    # Print map
    printAdjList(S, D, Vertex(0,0), True)
    
    server.send_state(lvl)
    if server.get_player_moves():
        # Process server.moves
        pass
    else:
        # Client error???
        break

    cat.get_cat_moves(lvl)
    

endDisplay(S)
print "Closing display..."
if server.error_msg != "":
    print server.error_msg
print "Disconnecting from client..."
server.end()
print "Disconnected from client..."
print "Shutting down..."
