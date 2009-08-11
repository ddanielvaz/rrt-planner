# -*- coding: utf-8 -*-
from playerc import playerc_graphics2d, PLAYERC_OPEN_MODE, player_color_t

class GraphicsProxy(playerc_graphics2d):
    def __init__(self, client, pid=0):
        super(GraphicsProxy, self).__init__(client, pid)
        super(GraphicsProxy, self).subscribe(PLAYERC_OPEN_MODE)

    def setcolor(self, rgb):
        color = player_color_t()
        color.red, color.green, color.blue = rgb
        self.color = color

    def png_to_map(self, x, y):
        scale = 16.0/500.0
        xmap = x * scale - 8.0
        ymap = 8.0 - y * scale
        return xmap, ymap

if __name__ == "__main__":
    import numpy
    from player_client import PlayerClient
    c = PlayerClient()
    c.connect()
    g = GraphicsProxy(c)
    g.setcolor((0,0,0))
    p = []
    for i in range(50):
        p.append(tuple(numpy.random.uniform(3, 3.5, 2)))
    g.draw_points(p, len(p))
    g.clear()
    g.subscribe(PLAYERC_OPEN_MODE)
    g.setcolor((0,0,255))
    p = []
    for i in range(50):
        p.append(tuple(numpy.random.uniform(1, 1.5, 2)))
    g.draw_points(p, len(p))
