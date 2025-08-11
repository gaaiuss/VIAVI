import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from windowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, /, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    # App creation
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    # App execution
    mainWindow.show()
    app.exec()
