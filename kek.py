import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Boilerplate")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        header_layout = QHBoxLayout()

        self.label1 = QLabel("1")
        header_layout.addWidget(self.label1, alignment=Qt.AlignLeft)

        self.label2 = QLabel("2")
        header_layout.addWidget(self.label2, alignment=Qt.AlignCenter)

        self.label3 = QLabel("3")
        header_layout.addWidget(self.label3, alignment=Qt.AlignRight)

        footer_layout = QHBoxLayout()

        self.label4 = QLabel("4")
        footer_layout.addWidget(self.label4, alignment=Qt.AlignLeft)

        self.label5 = QLabel("5")
        footer_layout.addWidget(self.label5, alignment=Qt.AlignCenter)

        self.label6 = QLabel("6")
        footer_layout.addWidget(self.label6, alignment=Qt.AlignRight)

        layout.addLayout(header_layout)  # Add the header layout to the main layout
        layout.addLayout(footer_layout)  # Add the footer layout to the main layout

    def on_button_clicked(self):
        self.label.setText("Button Clicked!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
