import client

client = client.Client()
client.start()

print client.get_game_state()
while client.running:
    s = raw_input('q<RET> to quit, any other key for next loop')
    if s == 'q' or s == 'Q':
        client.give_up("Client is quitting.")
    else:
        client.send_moves({'moves':{1:([0,3], [0,4]), 2:([7,6],[6,5])}})

    print client.get_game_state()
