ref = {0: "S", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "H", 8: "G"}


class Point:
    def __init__(self, name, h=0, before=None):
        self.name = name
        self.h = h
        self.before = before

    def set_before_point(self, point: 'Point'):
        self.before = point

    def __repr__(self):
        if self.before is None:
            return f"{ref[self.name]}(Null)"
        return f"{ref[self.name]}({ref[self.before.name]})"

    def find_point(self, points):
        for i in range(0, len(points)):
            if self.name == points[i].name:
                return i
        return None


def print_route(route, start=0):
    if route is None:
        print("No results were found")
        return
    p = route[0]
    while p.name != start:
        print(ref[p.name], end="<-")
        pos = p.before.find_point(route)
        p = route[pos]
    print(ref[p.name])
