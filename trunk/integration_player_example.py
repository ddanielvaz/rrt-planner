# -*- coding: utf-8 -*-
import numpy

from configspace import ConfigSpace
from gui import Drawer
from modelcar import Car
from proxies import RobotPlayer, PlayerClient, Position2dProxy, LaserProxy, \
    Graphics2dProxy, MapProxy
from rrt import RRT
from utils import debug, INTEGRATION_TIME, DELTA_T

MAX_TREE_NODES = 1600
N_ATTEMPT = 7
QGOAL_BIAS = 0.2

c = PlayerClient()
c.connect()
space = MapProxy(c)
p2d = Position2dProxy(c)
lp = LaserProxy(c)
r = RobotPlayer(c, p2d, lp)
Qinit = r.odom.get_measurement()
Qgoal = (-5, 0, 3.14/8)
my_car = Car(2, 30)
rrt = RRT(space, my_car, Qinit, Qgoal, QGOAL_BIAS, MAX_TREE_NODES)
for i in range(N_ATTEMPT):
    numpy.random.seed()
    debug("ATTEMPT %d." % (i+1))
    tree = rrt.build_rrt()
    if rrt.path:
        g = Graphics2dProxy(c)
        g.setcolor((0,255,0))
        for edge in rrt.plot_points:
            p = [(n[0],n[1]) for n in edge]
            g.draw_polyline(p, len(p))
        p = [(n[0],n[1]) for n in rrt.path]
        g.setcolor((0,0,255))
        g.draw_points(p, len(p))
        edges = [(rrt.path[i], rrt.path[i+1]) for i in range(len(rrt.path)-1)]
        for edge in edges:
            v,w = tree.edge_attributes(*edge)[0][1]
            n = edge[0]
            r.locomotion(my_car, n, v/5.0, w/5.0, INTEGRATION_TIME, DELTA_T)
        break
c.disconnect()
