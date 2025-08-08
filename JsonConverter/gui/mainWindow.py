from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget

from config.variables import ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Basic Layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Window title
        self.setWindowTitle('VIAVI Json Converter')

        # Window icon
        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

    def adjustFixedSize(self):
        # Last config to be done
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addToLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)
