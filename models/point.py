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


def print_route(route):
    for point in route[:-1]:
        print(ref[point.name], end="<-")
    print(ref[route[-1].name])