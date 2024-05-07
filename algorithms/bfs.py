from models.point import Point


def bfs_algorithms(matrix, start=0, end=8):
    visited = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    route = []
    open_point = Point(start)
    queue = [open_point]

    while len(queue) != 0:
        open_point = queue[0]
        visited[open_point.name] = 1
        queue.remove(open_point)
        route.append(open_point)
        if open_point.name == 8:
            return route[::-1]
        for i in range(0, 9):
            if visited[i] == 0 and matrix[open_point.name][i] > 0:
                p = Point(name=i, before=open_point)
                queue.append(p)
                visited[p.name] = 1
    return route[::-1]
