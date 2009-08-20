# -*- coding: utf-8 -*-
from playerc import playerc_graphics2d, PLAYERC_OPEN_MODE, player_color_t

class Graphics2dProxy(playerc_graphics2d):
    def __init__(self, client, pid=0):
        super(Graphics2dProxy, self).__init__(client, pid)
        super(Graphics2dProxy, self).subscribe(PLAYERC_OPEN_MODE)

    def setcolor(self, rgb):
        color = player_color_t()
        color.red, color.green, color.blue = rgb
        self.color = color

if __name__ == "__main__":
    import numpy
    from player_client import PlayerClient
    from time import sleep
    c = PlayerClient()
    c.connect()
    g = Graphics2dProxy(c)
    g.setcolor((0,255,0))
    p = []
    for i in range(1000):
        p.append(tuple(numpy.random.uniform(-2, 2, 2)))
    g.draw_points(p, len(p))
    sleep(5)
    c.disconnect()
