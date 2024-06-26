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

    def __gt__(self, other: 'PointCost'):
        if self.f > other.f:
            return True
        elif self.f == other.f:
            if self.point.name > other.point.name:
                return True
        return False

    def __lt__(self, other: 'PointCost'):
        if self.f < other.f:
            return True
        elif self.f == other.f:
            if self.point.name <= other.point.name:
                return True
        return False

    def __repr__(self):
        return f"{self.point}[{self.f}]"


def find_min_point_cost(arr_point_cost):
    return min(arr_point_cost)


from models.draw_route import draw_route


def print_route(route, start=0, end=8, plt=None):
    text = ""
    if route == [] or route is None:
        return ""
    if route[0].name != end:
        print("No results were found")
        print(route)
        text += f"No results were found \n {route}"
        return text
    p = route[0]
    while p.name != start:
        print(ref[p.name], end="<-")
        text += f"{ref[p.name]}<-"
        pos = p.before.find_point(route)
        if plt is not None:
            draw_route(plt, p.name, p.before.name)
        p = route[pos]
    print(ref[p.name])
    text += f"{ref[p.name]}"
    return text

