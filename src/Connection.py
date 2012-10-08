import socket
import Message

BUFFER_SIZE = 1024
MSG_DELIM = chr(23)

class Connection():

    def __init__(self, conn):
        self.conn = conn
        self.buffer = ""

    '''
    Receives a single message, decodes the data and returns a new Message
    object. Discards any data trailing the message delimiter.
    '''
    def getMessage(self):
        data = ""
        # Wait until the whole message has arrived
        while True:
            data += self.conn.recv(BUFFER_SIZE)
            if MSG_DELIM in data:
                break
        # Discard anything after the delimiter
        data = data[0:data.find(MSG_DELIM)]
        msg = Message.Message()
        msg.decode(data)
        return msg

    '''
    Sends a Message object.
    '''
    def sendMessage(self, msg):
        self.conn.sendall(msg.encoded + MSG_DELIM)

    '''
    Closes the connection
    '''
    def close(self):
        self.conn.close()

