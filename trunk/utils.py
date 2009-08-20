# -*- coding: utf-8 -*-
from time import strftime

INTEGRATION_TIME = 1.0
DELTA_T = 0.03125
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
