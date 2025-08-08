from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

from config.variables import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(150, 150)


class ButtonsGrid(QGridLayout):
    def __init__(self, * args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [['Select Json File(s)', 'Save to CSV']]
        self._makeGrid()

    def _makeGrid(self):
        for rowNumber, row in enumerate(self._gridMask):
            for columnNumber, buttonText in enumerate(row):
                button = Button(buttonText)
                self.addWidget(button, rowNumber, columnNumber)

    def _connectButtonClicked(self, button: Button, slot: Slot):
        button.clicked.connect(slot)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    # def _showError(self, msg: str):
    #     msgBox = self.window.makeMsgBox()
    #     msgBox.setText(msg)
    #     msgBox.setIcon(msgBox.Icon.Critical)
    #     msgBox.setStandardButtons(
    #         msgBox.StandardButton.Ok |
    #         msgBox.StandardButton.Cancel
    #     )

    #     msgBox.exec()
