# -*- coding: utf-8 -*-

from datetime import datetime
from math import sin, cos, degrees
from time import sleep, strftime
from sys import path
path.append("./..")

from utils import debug, map_to_png

DELTA_T = 0.100 # 100 ms
Kx = 0.0025
Ky = -0.05
Ka = 0.05
class RobotPlayer(object):
    def __init__(self, client, odom, laser):
        self.client = client
        self.laser = laser
        self.odom = odom

    def read(self):
        return self.client.read()

    def locomotion(self, robot_model, pos, vr, wr, action_time):
        xr, yr, ar = pos
        t = 0
        self.read()
        while t <= action_time:
            self.read()
            xc, yc, ac = map_to_png(*self.odom.get_measurement())

            xe = cos(ar) * (xr - xc) + sin(ar) * (yr - yc)
            ye = -sin(ar) * (xr - xc) + cos(ar) * (yr - yc)
            ae = ar - ac
            
            #debug("xr: %.2f | yr: %.2f | ar: %.2f" % (xr, yr, degrees(ar)))
            #debug("xc: %.2f | yc: %.2f | ac: %.2f" % (xc, yc, degrees(ac)))
            debug("xe: %.6f | ye: %.6f | ae: %.6f" % (xe, ye, degrees(ae)))

            vd = vr * cos(ae) + Kx * xe
            wd = wr + vr * (Ky * ye + Ka * sin(ae))
            debug("vr: %.2f | wr: %.2f | vd: %.2f | wd: %.2f" % (vr, wr, vd, wd))
            self.odom.set_cmd_vel(vd, 0, wd, True)
            sleep(DELTA_T)
            state = (xr, yr, ar)
            u = (vr, wr)
            dx, dy, da = robot_model.state_estimator(state, u, DELTA_T)
            xr, yr, ar = (xr + dx, yr + dy, ar + da)
            t = t + DELTA_T
