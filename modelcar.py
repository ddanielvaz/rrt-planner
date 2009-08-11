# -*- coding: utf-8 -*-
from math import radians, tan, cos, sin, pi

from utils import INTEGRATION_TIME, DELTA_T

class Car(object):
    def __init__(self, l, phi):
        self.l = l
        self.turn_constraint = radians(phi)
        self.rmin = self.l / tan(self.turn_constraint)

    def new_state(self, u, state, delta_t):
        """Esta função descreve a posição do carro após delta_t segundos sobre a
        influência de uma ação de controle 'u'."""
        dx = u.speed * cos(state.teta) * delta_t
        dy = u.speed * sin(state.teta) * delta_t
        dteta = u.turn_rate * delta_t
        return dx,dy,dteta

    def integrate(self, state, u, cspace, qgoal):
        count = 0.0
        x0 = state[0]
        y0 = state[1]
        teta0 = state[2]
        x, y, teta = 0,0,0
        v = u[0]
        w = u[1]
        points = [(x0, cspace.height - y0)]
        while count <= INTEGRATION_TIME:
            x = x0 + v * cos(teta0) * DELTA_T
            y = y0 + v * sin(teta0) * DELTA_T
            teta = teta0 + w * DELTA_T
            if teta > pi:
                teta = teta - 2.0 * pi
            elif teta < -pi:
                teta = teta + 2.0 * pi
            if cspace.is_configuration_in_colision((x, y, teta)):
                return None
            points.append((x, cspace.height - y))
            x0 = x
            y0 = y
            teta0 = teta
            count = count + DELTA_T
        return x,y,teta,points

