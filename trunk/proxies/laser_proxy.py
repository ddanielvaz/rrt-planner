# -*- coding: utf-8 -*-
from math import radians

from playerc import playerc_laser, PLAYERC_OPEN_MODE

class LaserProxy(playerc_laser):
    def __init__(self, client, pid=0):
        super(LaserProxy, self).__init__(client, pid)
        super(LaserProxy, self).subscribe(PLAYERC_OPEN_MODE)
        self.get_geom()

    def get_measurement(self):
        #angles = [radians(i/2.0) for i in range(-180, 181)]
        #rays = [(self.ranges[i], angle) for i,angle in enumerate(angles)]
        angles = []
        for i in range(-180, 181):
            angles.append(radians(i/2.0))
        rays = []
        for i,angle in enumerate(angles):
            rays.append((self.ranges[i], angle))
        return rays

if __name__ == "__main__":
    from player_client import PlayerClient
    c = PlayerClient()
    c.connect()
    l = LaserProxy(c)
    a=[]
    for i in range(1):
        c.read()
        print l.get_measurement()
    c.disconnect()