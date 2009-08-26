# -*- coding: utf-8 -*-
from playerc import playerc_client

# Create a client object
class PlayerClient(playerc_client):
    def __init__(self, host="localhost", port=6665):
        super(PlayerClient, self).__init__(None, host, port)

    def connect(self):
        super(PlayerClient, self).connect()

if __name__ == "__main__":
    c = PlayerClient()
    c.connect()
    print dir(c)
    c.disconnect()