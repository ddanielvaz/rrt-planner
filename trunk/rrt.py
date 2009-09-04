# -*- coding: utf-8 -*-
import pygraph

from utils import biased_sampling, debug, is_near_qgoal, select_nearest_node, dist

#INPUTS = ([(1, 0.0), (1, 0.2886), (1, 0.1443), (1, -0.2886), (1, -0.1443)]
#          (-1, -0.0), (-1, -0.2886), (-1, -0.1443), (-1, 0.2886), (-1, 0.1443)])
INPUTS = [(1, 0.0), (1, 0.28867513459481287), (1, 0.14433756729740643), (1, -0.28867513459481287), (1, -0.14433756729740643), (0.5, 0.0), (0.5, 0.14433756729740643), (0.5, 0.072168783648703216), (0.5, -0.14433756729740643), (0.5, -0.072168783648703216)]
class RRT(object):
    def __init__(self, cspace, car, qinit, qgoal, qgoal_bias, n):
        self.qinit = qinit
        self.qgoal = qgoal
        self.cspace = cspace
        self.car = car
        self.bias = qgoal_bias
        self.n = n

    def build_rrt(self):
        self.path = None
        self.plot_points = []
        debug("build_rrt started")
        count = 0
        g = pygraph.graph()
        g.add_node(self.qinit)
        while count < self.n:
            qrand = biased_sampling(self.cspace.bbox, self.bias, self.qgoal)
            q = self.extend_RRT(g, qrand)
            if q:
                count = count + 1
                if is_near_qgoal(q, self.qgoal, self.cspace.scale):
                    debug("TOLERANCE REACHED")
                    self.nearest_qgoal_node = q
                    self.build_path(g)
                    break
            else:
                continue
        debug("build_rrt ended")
        return g

    def extend_RRT(self, t, qrand):
        qnear = select_nearest_node(t, qrand)
        qchoosed, control, points = self.select_best_input(qnear, qrand,t)
        #debug(qchoosed)
        if qchoosed:
        #if not t.has_node(qchoosed):
            self.plot_points.append(points)
            t.add_node(qchoosed)
            t.add_edge(qnear, qchoosed)
            t.add_edge_attribute(qnear, qchoosed, ('control', control))
        #else:
        #    return None
        return qchoosed

    def select_best_input(self, qnear, qrand,t):
        qchoosed = None
        best_control = None
        points = None
        dmin = float('inf')
        for control in INPUTS:
            temp = self.car.integrate(qnear, control, self.cspace, self.qgoal)
            if temp:
                qnew = temp[:-1]
                d = dist(qnew, qrand)
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

