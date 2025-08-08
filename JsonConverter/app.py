# import json
import sys

# from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from gui.buttons import ButtonsGrid
from gui.info import Info
from gui.mainWindow import MainWindow

if __name__ == "__main__":
    # Create app
    app = QApplication(sys.argv)
    window = MainWindow()

    # Info
    info = Info('Select json files to convert to csv')
    window.addToLayout(info)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Execute everything
    window.adjustFixedSize()
    window.show()
    app.exec()
