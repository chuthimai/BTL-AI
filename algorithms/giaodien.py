import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit
#Sử dụng thư viện PyQt5 
class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout chính
        layout = QVBoxLayout()

        # Bảng Điền Ma Trận
        grid_layout = QGridLayout()
        matrix_label = QLabel("Bảng Điền Ma Trận:")
        grid_layout.addWidget(matrix_label, 0, 0)
        # Tạo ma trận ô vuông 5x5
        for i in range(5):
            for j in range(5):
                btn = QPushButton()
                grid_layout.addWidget(btn, i+1, j)

        layout.addLayout(grid_layout)

        # Bảng Điền Heuristic
        heuristic_layout = QVBoxLayout()
        heuristic_label = QLabel("Bảng Điền Heuristic:")
        heuristic_layout.addWidget(heuristic_label)
        # Tạo các ô nhập giá trị heuristic, ví dụ 5x5
        for i in range(5):
            row_layout = QHBoxLayout()
            for j in range(5):
                heuristic_edit = QLineEdit()
                row_layout.addWidget(heuristic_edit)
            heuristic_layout.addLayout(row_layout)

        layout.addLayout(heuristic_layout)

        # Nút Chức Năng
        button_layout = QHBoxLayout()
        algorithm_label = QLabel("Thuật Toán:")
        button_layout.addWidget(algorithm_label)
        # Tạo các nút chọn thuật toán
        dfs_button = QPushButton("DFS")
        ida_button = QPushButton("IDA*")
        knn_button = QPushButton("KNN")
        bayes_button = QPushButton("Bayes")
        button_layout.addWidget(dfs_button)
        button_layout.addWidget(ida_button)
        button_layout.addWidget(knn_button)
        button_layout.addWidget(bayes_button)

        layout.addLayout(button_layout)

        # Kết quả
        result_label = QLabel("Kết Quả:")
        layout.addWidget(result_label)
        result_text = QTextEdit()
        layout.addWidget(result_text)

        self.setLayout(layout)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Giao Diện Thuật Toán')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())



