# -*- coding: utf-8 -*-
import numpy

from configspace import ConfigSpace
from gui import Drawer
from modelcar import Car
from proxies import RobotPlayer, PlayerClient, Position2dProxy, LaserProxy, \
    Graphics2dProxy
from rrt import RRT
from utils import debug, INTEGRATION_TIME

MAX_TREE_NODES = 1200
N_ATTEMPT = 7
#Qinit = (46.875, 453.125, 0)
#Qgoal = (200, 400.125, 0)
my_car = Car(20, 30)
#Rand 1
Qinit = (100, 450, 0.0)
Qgoal = (400, 100, 0.0)
#Rand 2
#Qinit = (20, 480, 0.0)
#Qgoal = (480, 350, 0.0)
#Rand 3
#Qinit = (425, 195, 0.0)
#Qgoal = (125, 90, 0.0)
space = ConfigSpace("./cave.png", my_car, Qgoal)
rrt = RRT(space, Qinit, Qgoal, MAX_TREE_NODES)
for i in range(N_ATTEMPT):
    numpy.random.seed()
    debug("ATTEMPT %d." % (i+1))
    tree = rrt.build_rrt()
    if rrt.path:
        c = PlayerClient()
        c.connect()
        p2d = Position2dProxy(c)
        lp = LaserProxy(c)
        r = RobotPlayer(c, p2d, lp)
        g = Graphics2dProxy(c)
        g.setcolor((0,255,0))
        g.clear()
        p = [g.png_to_map(n[0],n[1]) for n in rrt.path]
        g.draw_polyline(p, len(p))
        g.setcolor((0,0,0))
        g.draw_points(p, len(p))
        edges = [(rrt.path[i], rrt.path[i+1]) for i in range(len(rrt.path)-1)]
        for edge in edges:
            c.read()
            v,w = tree.edge_attributes(*edge)[0][1]
            n = edge[0]
            r.locomotion(n, v*0.032/5.0, -w/5.0, INTEGRATION_TIME)
        break
