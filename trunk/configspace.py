# -*- coding: utf-8 -*-
import Image

class ConfigSpace(object):
    def __init__(self, map_file):
        self.im = Image.open(map_file)
        self.width, self.height = self.im.size
        self.data = self.im.load()
        self.bbox = [0, self.width, 0, self.height]
        self.scale = 500.0/16.0

    def is_configuration_in_colision(self, q):
        if q[0] >= self.width or q[1] >= self.height or q[0] < 0 or q[1] < 0:
            return True
        if self.data[q[:2]] == 255:
            return False
        else:
            return True
