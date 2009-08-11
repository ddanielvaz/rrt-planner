# -*- coding: utf-8 -*-
from math import radians

class RobotPlayer(object):
    def __init__(self, client, odom, laser):
        self.client = client
        self.laser = laser
        self.odom = odom

    def read(self):
        return self.client.read()

    def walk(self):
        lright = self.laser.ranges[0:180]
        lleft = self.laser.ranges[180:360]
        minR = min(lright)
        minL = min(lleft)
        #print "minR:", minR, "minL:", minL
        left = (1e5*minR)/500-100
        right = (1e5*minL)/500-100
        if left > 100:
            left = 100
        if right > 100:
            right = 100
        newspeed = (right+left)/1e3
        newturnrate = radians(limit((right-left), -40.0, 40.0))
        self.odom.set_cmd_vel(newspeed, newspeed, newturnrate, 1)

def limit(val, bottom, top):
    if val > top:
        return top
    elif val < bottom:
        return bottom
    return val
