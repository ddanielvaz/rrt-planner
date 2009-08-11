# -*- coding: utf-8 -*-
import pygraph

from utils import debug

INPUTS = ([(10, 0.0), (10, 0.2886), (10, 0.1443), (10, -0.2886), (10, -0.1443),
          (-10, -0.0), (-10, -0.2886), (-10, -0.1443), (-10, 0.2886), (-10, 0.1443)])

class RRT(object):
    def __init__(self, cspace, qinit, qgoal, n):
        self.qinit = qinit
        self.qgoal = qgoal
        self.cspace = cspace
        self.n = n
        self.path = None
        self.plot_points = []

    def build_rrt(self):
        debug("build_rrt started")
        count = 0
        g = pygraph.graph()
        g.add_node(self.qinit)
        while count < self.n:
            qrand = self.cspace.get_bias_random_configuration()
            q = self.extend_RRT(g, qrand)
            if q:
                count = count + 1
                if self.cspace.is_near_qgoal(q, self.qgoal):
                    debug("TOLERANCE REACHED")
                    self.nearest_qgoal_node = q
                    self.build_path(g)
                    break
            else:
                continue
        debug("build_rrt ended")
        return g

    def extend_RRT(self, t, qrand):
        qnear = self.cspace.select_nearest_node(t, qrand)
        qchoosed, control, points = self.select_best_input(qnear, qrand,t)
        self.plot_points.append(points)
        if not t.has_node(qchoosed):
            t.add_node(qchoosed)
            t.add_edge(qnear, qchoosed)
            t.add_edge_attribute(qnear, qchoosed, ('control', control))
        else:
            return None
        return qchoosed

    def select_best_input(self, qnear, qrand,t):
        qchoosed = None
        best_control = None
        points = None
        dmin = float('inf')
        for control in INPUTS:
            temp = self.cspace.car.integrate(qnear, control, self.cspace, self.qgoal)
            if temp:
                qnew = temp[:-1]
                d = self.cspace.dist(qnew, qrand)
                if d < dmin:
                    dmin = d
                    best_control = control
                    qchoosed = qnew
                    points = temp[-1]
        return qchoosed, best_control, points

    def build_path(self, g):
        h = pygraph.algorithms.heuristics.chow(self.qinit, self.nearest_qgoal_node)
        h.optimize(g)
        h_search = pygraph.algorithms.minmax.heuristic_search
        self.path = h_search(g, self.qinit, self.nearest_qgoal_node, h)

