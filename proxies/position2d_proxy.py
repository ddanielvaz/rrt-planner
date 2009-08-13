# -*- coding: utf-8 -*-
from math import sqrt
from time import sleep

from playerc import playerc_position2d, PLAYERC_OPEN_MODE

class Position2dProxy(playerc_position2d):
    def __init__(self, client, pid=0):
        super(Position2dProxy, self).__init__(client, pid)
        super(Position2dProxy, self).subscribe(PLAYERC_OPEN_MODE)
        self.enable(True)
        self.x = self.px
        self.y = self.py
        self.angle = self.pa

    def get_diff_measurement(self):
        x, y, a = self.px, self.py, self.pa
        dx = x - self.x
        dy = y - self.y
        da = a - self.angle
        d = sqrt(dx ** 2 + dy ** 2)
        self.x, self.y, self.angle = x, y, a
        return d, da

    def get_measurement(self):
        return self.px, self.py, self.pa

    def locomotion(self, v, w, action_time):
        self.set_cmd_vel(v, 0, w, True)
        sleep(action_time)


if __name__ == "__main__":
    from player_client import PlayerClient
    c = PlayerClient()
    o = Position2dProxy(c)
    print dir(o)
