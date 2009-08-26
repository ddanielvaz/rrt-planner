# -*- coding: utf-8 -*-
from rrt import RRT
from configspace import ConfigSpace
from modelcar import Car
from gui import Drawer
from utils import debug

MAX_TREE_NODES = 1600
N_ATTEMPT = 10
QGOAL_BIAS = 1

my_car = Car(20, 30)
#Rand 1
#Qinit = (100, 450, 0.0)
#Qgoal = (400, 100, 0.0)
#Rand 2
Qinit = (20, 480, 0.0)
Qgoal = (100, 480, 0.0)
#Qgoal = (480, 350, 0.0)
#Rand 3
#Qinit = (425, 195, 0.0)
#Qgoal = (125, 90, 0.0)
space = ConfigSpace("./examples/bitmaps/cave.png", Qgoal)
rrt = RRT(space, my_car, Qinit, Qgoal, QGOAL_BIAS, MAX_TREE_NODES)
for i in range(N_ATTEMPT):
    debug("ATTEMPT %d." % (i+1))
    tree = rrt.build_rrt()
    if rrt.path:
        drawer = Drawer(space)
        drawer.draw_vertices(tree.nodes(), marker="o", color="#000000", ls="", markersize=2)
        drawer.draw_points(rrt.plot_points, edgecolor="#ff0000", facecolor="none")
        #drawer.draw_edges(tree.edges(), edgecolor="#00FF00")
        drawer.draw_vertices(rrt.path, marker="o", color="#00FF00", ls="", markersize=3)
        drawer.draw_vertices([Qinit], marker="^", color="#0000ff", ls="", markersize=5)
        drawer.draw_vertices([Qgoal], marker="o", color="#00ff00", ls="", markersize=5)
        drawer.show()
        break
