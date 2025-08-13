import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from src.mainWindow import MainWindow
from src.variables import ICON_PATH

if __name__ == '__main__':
    # App creation
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    # Icon
    icon = icon = QIcon(str(ICON_PATH))
    app.setWindowIcon(icon)

    # App execution
    mainWindow.show()
    app.exec()
