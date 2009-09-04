# -*- coding: utf-8 -*-

from datetime import datetime
from math import sin, cos, degrees, sqrt
from time import sleep

Kx = 0.25
Ky = 1
Ka = sqrt(4 * Ky)

class RobotPlayer(object):
    def __init__(self, client, odom, laser):
        self.client = client
        self.laser = laser
        self.odom = odom
        self.read()

    def read(self):
        return self.client.read()

    def locomotion(self, robot_model, pos, vr, wr, action_time, dt):
        xr, yr, ar = pos
        t = 0
        while t <= action_time:
            self.read()
            t0 = datetime.now()
            xc, yc, ac = self.odom.get_measurement()
            xe = cos(ar) * (xr - xc) + sin(ar) * (yr - yc)
            ye = -sin(ar) * (xr - xc) + cos(ar) * (yr - yc)
            ae = ar - ac
            vd = vr * cos(ae) + Kx * xe
            wd = wr + vr * (Ky * ye + Ka * sin(ae))

            state = (xr, yr, ar)
            u = (vr, wr)
            dx, dy, da = robot_model.state_estimator(state, u, dt)
            xr, yr, ar = (xr + dx, yr + dy, ar + da)
            t = t + dt
            t1 = datetime.now()
            d = t1 - t0
            delay = d.seconds + d.microseconds / 1e6
            self.odom.set_cmd_vel(vd, 0, wd, True)
            sleep(dt - delay)
