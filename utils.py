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

