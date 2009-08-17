# -*- coding: utf-8 -*-
from time import sleep, strftime
DELTA_T = 0.100 #100 ms

class RobotPlayer(object):
    def __init__(self, client, odom, laser):
        self.client = client
        self.laser = laser
        self.odom = odom

    def read(self):
        return self.client.read()

    def locomotion(self, pos, v, w, action_time):
        x, y, theta = pos
        t = 0
        self.odom.set_cmd_vel(v, 0, w, True)
        while t <= action_time:
            self.read()
            t = t + DELTA_T
            sleep(DELTA_T)
            print strftime("%H:%M:%S")
