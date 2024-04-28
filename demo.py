import matplotlib.pyplot as plt

# Tọa độ của hai điểm
x1, y1 = 1, 2
x2, y2 = 4, 6

# Vẽ đoạn thẳng
plt.plot([x1, x2], [y1, y2], color='b', linestyle='-', linewidth=2)

# Đặt các nhãn và tiêu đề
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Vẽ đoạn thẳng bằng Pyplot')

# Hiển thị đồ thị
plt.grid(True)
plt.show()
