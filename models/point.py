class Point:
    def __init__(self, name, h=0):
        self.name = name
        self.h = h
        self.before = None

    def set_before_point(self, point: 'Point'):
        self.before = point
