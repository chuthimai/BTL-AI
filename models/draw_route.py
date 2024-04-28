from data.position_point import position_points


def draw_route(plt, point1: int, point2: int):
    plt.plot(
        [position_points[point1]['x'],position_points[point2]['x']],
        [position_points[point1]['y'],position_points[point2]['y']],
        color='black',
        linestyle='-',
        linewidth=2
    )