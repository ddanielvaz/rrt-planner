# -*- coding: utf-8 -*-
from configspace import ConfigSpace
from gui import Drawer
from modelcar import Car
from proxies import Position2dProxy, PlayerClient, Graphics2dProxy
from rrt import RRT
from utils import debug, INTEGRATION_TIME

MAX_TREE_NODES = 600
N_ATTEMPT = 5
#c.read()
Qinit = (46.875, 453.125, 0)
Qgoal = (200, 400.125, 0)
my_car = Car(20, 30)
#Rand 1
#Qinit = (100, 450, 0.0)
#Qgoal = (400, 100, 0.0)
#Rand 2
#Qinit = (20, 480, 0.0)
#Qgoal = (480, 350, 0.0)
#Rand 3
#Qinit = (425, 195, 0.0)
#Qgoal = (125, 90, 0.0)
space = ConfigSpace("./cave.png", my_car, Qgoal)
rrt = RRT(space, Qinit, Qgoal, MAX_TREE_NODES)
for i in range(N_ATTEMPT):
    debug("ATTEMPT %d." % (i+1))
    tree = rrt.build_rrt()
    if rrt.path:
        c = PlayerClient()
        c.connect()
        p2d = Position2dProxy(c)
        g = Graphics2dProxy(c)
        g.setcolor((0,255,0))
        g.clear()
        p = [g.png_to_map(n[0],n[1]) for n in rrt.path]
        g.draw_polyline(p, len(p))
        g.setcolor((0,0,0))
        g.draw_points(p, len(p))
        edges = [(rrt.path[i], rrt.path[i+1]) for i in range(len(rrt.path)-1)]
        for edge in edges:
            v,w = tree.edge_attributes(*edge)[0][1]
            p2d.locomotion(v*0.032, -w*0.032, INTEGRATION_TIME)
        break
