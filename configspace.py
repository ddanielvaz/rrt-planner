# -*- coding: utf-8 -*-
from math import pi, degrees, sqrt

import Image
from numpy.random import rand, uniform

LINEAR_TOLERANCE = 10.0
ANGULAR_TOLERANCE = 0.26
QGOAL_BIAS = 1

class ConfigSpace(object):
    def __init__(self, map_file, car, qgoal):
        self.im = Image.open(map_file)
        self.width, self.height = self.im.size
        self.data = self.im.load()
        self.car = car
        self.qgoal = qgoal

    def dist(self, p, q):
        """Retorna a distância euclidiana entre dois pontos mais a diferença
        absoluta angular, em graus."""
        dx = p[0] - q[0]
        dy = p[1] - q[1]
        da = p[2] - q[2]
        if da > pi:
            da = da - 2 * pi
        elif da < -pi:
            da = da + 2 * pi
        return sqrt(dx ** 2 + dy ** 2 + da**2 * 5)

    def is_near_qgoal(self, p, q):
        dx2 = (p[0] - q[0]) ** 2
        dy2 = (p[1] - q[1]) ** 2
        da = p[2] - q[2]
        if da > pi:
            da = da - 2 * pi
        elif da < -pi:
            da = da + 2 * pi
        d = sqrt(dx2 + dy2)
        if d < LINEAR_TOLERANCE and abs(da) < ANGULAR_TOLERANCE:
            return True
        else:
            return False

    def get_random_config(self):
        x = rand() * self.width  #randint(0, self.width)
        y = rand() * self.height #randint(0, self.height)
        teta = uniform(-pi, pi)
        return x, y, teta

    def get_bias_random_configuration(self):
        if rand() < QGOAL_BIAS:
            return self.qgoal
        q = self.get_random_config()
        #while self.is_configuration_in_colision(q):
        #    q = self.get_random_config()
        return q

    def is_configuration_in_colision(self, q):
        if q[0] >= self.width or q[1] >= self.height or q[0] < 0 or q[1] < 0:
            return True
        if self.data[q[:2]] == 255:
            return False
        else:
            return True

    def select_nearest_node(self, g, q):
        """Returns the nearest node according to function dist."""
        dmin = float('inf')
        vertices = g.nodes()
        for configuration in vertices:
            d = self.dist(configuration, q)
            if d < dmin:
                dmin = d
                nearest = configuration
        return nearest

