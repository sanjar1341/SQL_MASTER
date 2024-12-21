from PyQt5.QtWidgets import QApplication, QFrame, QSplitter, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dinamik Separator Misoli")
        self.setGeometry(100, 100, 400, 300)

        # Frame 1
        frame1 = QFrame()
        frame1.setStyleSheet("background-color: lightblue;")

        # Frame 2
        frame2 = QFrame()
        frame2.setStyleSheet("background-color: lightgreen;")

        # Separator (Splitter)
        splitter = QSplitter()
        splitter.addWidget(frame1)
        splitter.addWidget(frame2)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(splitter)

        self.setLayout(layout)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
