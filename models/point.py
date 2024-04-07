ref = {0: "S", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "H", 8: "G"}


class Point:
    def __init__(self, name, h=0, before=None):
        self.name = name
        self.h = h
        self.before = before

    def set_before_point(self, point: 'Point'):
        self.before = point

    def find_point(self, points):
        for i in range(0, len(points)):
            if self.name == points[i].name:
                return i
        return None

    def __repr__(self):
        if self.before is None:
            return f"{ref[self.name]}(Null)"
        return f"{ref[self.name]}({ref[self.before.name]})"


class PointCost:
    def __init__(self, point: Point, c=0):
        self.point = point
        self.c = c
        self.f = self.point.h + self.c

    def find_point(self, arr_points):
        try:
            return arr_points.index(self)
        except ValueError:
            return None

    def __ge__(self, other: 'PointCost'):
        if self.f > other.f:
            return True
        elif self.f == other.f:
            if self.point.name > other.point.name:
                return True
        return False

    def __le__(self, other: 'PointCost'):
        if self.f < other.f:
            return True
        elif self.f == other.f:
            if self.point.name < other.point.name:
                return True
        return False

    def __repr__(self):
        return f"{self.point}[{self.f}]"


def find_min_point_cost(arr_point_cost):
    return min(arr_point_cost)


def print_route(route, start=0, end=8):
    if route[0].name != end:
        print("No results were found")
        print(route)
        return
    p = route[0]
    while p.name != start:
        print(ref[p.name], end="<-")
        pos = p.before.find_point(route)
        p = route[pos]
    print(ref[p.name])
