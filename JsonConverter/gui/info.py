from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel

from config.variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for i in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setContentsMargins(*margins)
