from models.point import Point, print_route
import matplotlib.pyplot as plt
from models.draw_point import draw_point

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


def bfs_algorithms(matrix, start=0, end=8):
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    route = []
    queue = []

    # Khởi tạo queue với các điểm lân cận của điểm bắt đầu
    for i in range(8, -1, -1):
        if visited[i] == 0 and matrix[start][i] > 0:
            p = Point(name=i, before=None)
            queue.append(p)

    while queue:
        open_point = queue.pop(0)
        route.insert(0, open_point)
        visited[open_point.name] = 1

        for i in range(8, -1, -1):
            if visited[i] == 0 and matrix[open_point.name][i] > 0:
                p = Point(name=i, before=open_point)
                queue.append(p)

        if open_point.name == end:
            route.insert(0, open_point)
            break

    return route

draw_point(plt=plt)

txt = print_route(dfs_algorithms(matrix_example), plt=plt)
plt.savefig("../static/images/bfs.png")
print(txt)
