from matplotlib import pyplot as plt

from models.draw_point import draw_point
from models.point import Point, print_route, PointCost, find_min_point_cost


def a_star_algorithm(matrix, heu, start=0, end=8):
    set_of_bound = []
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    route = []
    open_point = PointCost(Point(start, h=heu[start]), c=0)
    set_of_bound.append(open_point)

    if sum([r[8] for r in matrix]) == 0:
        return "Not found result"

    while len(set_of_bound) != 0:
        open_point = find_min_point_cost(set_of_bound)
        set_of_bound.remove(open_point)
        route.append(open_point)
        visited[open_point.point.name] = 1

        for j in range(8, -1, -1):
            if visited[j] == 0 and matrix[open_point.point.name][j] > 0:
                g = open_point.c + matrix[open_point.point.name][j]
                p = PointCost(Point(name=j, before=open_point.point, h=heu[j]), c=g)
                set_of_bound.append(p)

        if open_point.point.name == end:
            draw_point(plt)
            route.insert(0, open_point)
            r = print_route(list(map(lambda point_cost: point_cost.point, route)), plt=plt)
            plt.savefig("./static/images/a_star.png")
            return f"Route: {r} ➦ cost = {route[0].f}"

    return "Not found result"
