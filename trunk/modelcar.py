# -*- coding: utf-8 -*-
from math import radians, tan, cos, sin, pi

from utils import INTEGRATION_TIME, DELTA_T

class Car(object):
    def __init__(self, l, phi):
        self.l = l
        self.turn_constraint = radians(phi)
        self.rmin = self.l / tan(self.turn_constraint)

    def state_estimator(self, state, u, dt):
        """Esta função descreve a posição do carro após delta_t segundos sobre a
        influência de uma ação de controle 'u'."""
        v, w = u
        dx = v * cos(state[2]) * dt
        dy = v * sin(state[2]) * dt
        dteta = w * dt
        return dx, dy, dteta

    def integrate(self, state, u, cspace, qgoal):
        count = 0.0
        x0 = state[0]
        y0 = state[1]
        teta0 = state[2]
        x, y, teta = 0,0,0
        v = u[0]
        w = u[1]
        points = [(x0, y0)]
        while count <= INTEGRATION_TIME * cspace.scale:
            x = x0 + v * cos(teta0) * DELTA_T
            y = y0 + v * sin(teta0) * DELTA_T
            teta = teta0 + w * DELTA_T / cspace.scale
            if teta > pi:
                teta = teta - 2.0 * pi
            elif teta < -pi:
                teta = teta + 2.0 * pi
            if cspace.is_configuration_in_colision((x, y, teta)):
                return None
            points.append((x, y))
            x0 = x
            y0 = y
            teta0 = teta
            count = count + DELTA_T
        return x,y,teta,points

