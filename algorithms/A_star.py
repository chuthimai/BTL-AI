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


def a_star_algorithm(matrix, start=0, end=8):
    open_set = []  # Priority queue (heap) for open points
    closed_set = set()  # Set of closed (visited) points

    start_point = PointCost(Point(start, h=h[start]), c=0)
    open_set.heappush(start_point)

    while open_set:
        current_point = open_set.heappop()

        if current_point.point.name == end:
            print_route(list(map(lambda point_cost: point_cost.point, open_set)))
            print(f"cost = {current_point.f}")
            return True

        closed_set.add(current_point.point.name)

        for neighbor in range(8, -1, -1):
            if neighbor not in closed_set and matrix[current_point.point.name][neighbor] > 0:
                g = current_point.c + matrix[current_point.point.name][neighbor]
                f = g + h[neighbor]
                new_point = PointCost(Point(name=neighbor, before=current_point.point, h=h[neighbor]), c=g, f=f)

                if new_point not in open_set or new_point.f < open_set[open_set.index(new_point)].f:
                    open_set.heappush(new_point)

    return False


print_route(a_star_algorithm(matrix_example))