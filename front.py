import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class FileDropWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("파일 드래그 앤 드롭 예제")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 380, 280)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("파일을 이곳으로 드래그 앤 드롭하세요.")
        self.label.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        pixmap = QPixmap(file_path)
        self.label.setPixmap(pixmap.scaled(380, 280))
        self.label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDropWindow()
    window.show()
    sys.exit(app.exec_())
