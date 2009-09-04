# -*- coding: utf-8 -*-
from math import pi, sqrt

from numpy.random import rand, uniform

from playerc import playerc_map, PLAYERC_OPEN_MODE

class MapProxy(playerc_map):
    def __init__(self, client, pid=0):
        super(MapProxy, self).__init__(client, pid)
        super(MapProxy, self).subscribe(PLAYERC_OPEN_MODE)
        self.get_map()
        lower_w = int(-self.width / 2.0 * self.resolution)
        upper_w = int(self.width / 2.0 * self.resolution)
        lower_h = int(-self.height / 2.0 * self.resolution)
        upper_h = int(self.height / 2.0 * self.resolution)
        self.bbox = (lower_w, upper_w, lower_h, upper_h)
        occ = []
        for cell in self.cells:
            occ.append(ord(cell))
        self.occ = occ
        self.scale = 1.0

    def map_to_png(self, pos):
        x, y, a = pos
        xpng = x / self.resolution + self.width / 2.0
        ypng = self.height / 2.0 + y / self.resolution
        return int(xpng), int(ypng), a

    def is_configuration_in_colision(self, q):
        px, py, a = self.map_to_png(q)
        cell_index = int(self.width * py + px)
        if px >= self.width or py >= self.height or px < 0 or py < 0:
            return True
        elif self.occ[cell_index] == 255:
            return False
        else:
            return True

if __name__ == "__main__":
    from player_client import PlayerClient
    c = PlayerClient()
    c.connect()
    m = MapProxy(c)
    print m.occ
    print m.resolution
    print m.scale
