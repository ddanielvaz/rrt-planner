# -*- coding: utf-8 -*-
from math import pi, sqrt
from time import strftime

from numpy.random import rand, uniform

INTEGRATION_TIME = 1.0
DELTA_T = 0.100
LINEAR_TOLERANCE = 0.3
ANGULAR_TOLERANCE = 3.14
is_debug_active = True

def debug(debug_str):
    if is_debug_active:
        print "%s - DEBUG: %s" % (strftime("%H:%M:%S"), debug_str)
        #dbg_str = "%s" % (debug_str)
        #dbg_str = dbg_str.replace(".",",")
        #print dbg_str

def png_to_map(x, y):
    scale = 16.0/500.0
    xmap = x * scale - 8.0
    ymap = 8.0 - y * scale
    return xmap, ymap

def map_to_png(x, y, a):
    scale = 500.0/16.0
    xpng = x * scale + 250
    ypng = 250 - y * scale
    return xpng, ypng, -a

def runge_kutta_integrator(pos, v, w):
    pass

def dist(p, q):
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    da = p[2] - q[2]
    if da > pi:
        da = da - 2 * pi
    elif da < -pi:
        da = da + 2 * pi
    return sqrt(dx ** 2 + dy ** 2 + da**2 * 5)

def biased_sampling(bounds, bias, qgoal):
    if rand() < bias:
        return qgoal
    q = get_random_config(*bounds)
    return q

def get_random_config(lower_w, upper_w, lower_h, upper_h):
    x = uniform(lower_w, upper_w)
    y = uniform(lower_h, upper_h)
    teta = uniform(-pi, pi)
    return x, y, teta

def is_near_qgoal(p, q, scale):
    dx2 = (p[0] - q[0]) ** 2
    dy2 = (p[1] - q[1]) ** 2
    da = p[2] - q[2]
    if da > 2 * pi:
        da = da - 2 * pi
    d = sqrt(dx2 + dy2)
    if d < LINEAR_TOLERANCE * scale and abs(da) < ANGULAR_TOLERANCE:
        return True
    else:
        return False

def select_nearest_node(g, q):
    """Returns the nearest node according to function dist."""
    dmin = float('inf')
    vertices = g.nodes()
    for configuration in vertices:
        d = dist(configuration, q)
        if d < dmin:
            dmin = d
            nearest = configuration
    return nearest
