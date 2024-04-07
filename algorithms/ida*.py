from models.point import Point, print_route, PointCost

matrix_example = [
    [0, 2, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

h = [6, 4, 4, 3, 4, 1, 1, 0, 0]


def ida_star_step(matrix, start=0, end=8, i=8):
    set_of_bound = []
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    route = []
    open_point = PointCost(Point(start, h=h[start]), c=0)

    loop = True
    if open_point.f > i:
        loop = False

    while loop:
        route.insert(0, open_point)
        visited[open_point.point.name] = 1

        for j in range(8, -1, -1):
            if visited[j] == 0 and matrix[open_point.point.name][j] > 0:
                g = open_point.c + matrix[open_point.point.name][j]
                p = PointCost(Point(name=j, before=open_point.point, h=h[j]), c=g)
                if p.f <= i:
                    set_of_bound.insert(0, p)

        if len(set_of_bound) == 0:
            # route = None
            break
        open_point = set_of_bound[0]
        set_of_bound.pop(0)

        if open_point.point.name == end:
            route.insert(0, open_point)
            print(f"i = {i}; route = ", end='')
            print_route(list(map(lambda point_cost: point_cost.point, route)))
            print(f"cost = {route[0].f}")
            return True

    print(f"i = {i}; route = {route}")
    return False


def ida_star_algorithms(matrix, start=0, end=8, beta=2):
    i = beta
    while True:
        if ida_star_step(matrix, start=start, end=end, i=i):
            break
        i += beta


ida_star_algorithms(matrix_example)