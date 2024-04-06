from models.point import Point, print_route

matrix_example = [
    [0, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def dfs_algorithms(matrix, start=0, end=8):
    set_of_bound = []
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    route = []
    open_point = Point(start)
    while True:
        route.insert(0, open_point)
        visited[open_point.name] = 1

        for i in range(8, -1, -1):
            if visited[i] == 0 and matrix[open_point.name][i] > 0:
                p = Point(name=i, before=open_point)
                set_of_bound.insert(0, p)

        if len(set_of_bound) == 0:
            route = None
            break
        open_point = set_of_bound[0]
        set_of_bound.pop(0)
        if open_point.name == end:
            route.insert(0, open_point)
            break

    return route



print_route(dfs_algorithms(matrix_example))


