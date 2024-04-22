# import matplotlib.pyplot as plt
from data.position_point import position_points


def draw_point(plt):
    for i in range(0, 9):
        plt.scatter(
            position_points[i]["x"],
            position_points[i]["y"],
            label=position_points[i]['label'],
            c=position_points[i]['color'],
            s=300,
            alpha=0.8,
        )

    plt.xlim([-1, 15])
    plt.ylim([-10, 10])
    plt.legend()
    plt.title("Graph")

# draw_point(plt)