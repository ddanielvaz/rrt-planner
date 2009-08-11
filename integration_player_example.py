from configspace import ConfigSpace
from gui import Drawer
from modelcar import Car
from proxies import OdometerProxy, PlayerClient, GraphicsProxy
from rrt import RRT
from utils import INTEGRATION_TIME

MAX_TREE_NODES = 800

c = PlayerClient()
c.connect()
o = OdometerProxy(c)
g = GraphicsProxy(c)
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
tree = rrt.build_rrt()
g.setcolor((0,255,0))
g.clear()
if rrt.path:
    p = [g.png_to_map(n[0],n[1]) for n in rrt.path]
    g.draw_polyline(p, len(p))
    g.setcolor((0,0,0))
    g.draw_points(p, len(p))
    print rrt.path
    edges = [(rrt.path[i], rrt.path[i+1]) for i in range(len(rrt.path)-1)]
    print edges
    for edge in edges:
        v,w = tree.edge_attributes(*edge)[0][1]
        o.set_speed(v*0.032, -w, INTEGRATION_TIME)

#p = [g.png_to_map(n[0],n[1]) for n in tree.nodes()]
#g.draw_points(p, len(p))

