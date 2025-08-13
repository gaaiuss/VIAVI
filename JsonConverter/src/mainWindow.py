import json

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow

from src.converter import (flatten_json_list, format_serial_number,
                           merge_json_files, write_csv)
from src.variables import (CSV_CONFIG_FILE, ICON_PATH, JSON_OUTPUT_FILE,
                           LABEL_ICON_PATH)
from src.windowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, /, parent=None):
        # Setup Qt Designer window
        super().__init__(parent)
        self.setupUi(self)

        # Buttons functionalities
        self.selectedFiles = []
        self.selectButton.clicked.connect(self.selectFileDialog)
        self.convertButton.clicked.connect(self.convertSelectedFiles)

        # Icon
        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

        # Label Logo
        self.setLabelLogo()

    def getSelectedFiles(self):
        return self.selected_files

    def showSavedLocalPath(self):
        pass

    def setLabelLogo(self):
        self.labelLogo.setPixmap(QPixmap(str(LABEL_ICON_PATH)))

    def selectFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Files")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.selected_files = selected_files
            self.selectedFilesLabel.setText(
                f'{len(selected_files)} files selected')

    def convertSelectedFiles(self):
        merge_json_files(self.selected_files, JSON_OUTPUT_FILE)
        with open(JSON_OUTPUT_FILE, 'r') as f:
            json_list = json.load(f)
            fmt_json = format_serial_number(json_list)
            resource = flatten_json_list(fmt_json)
            csv_output_file = self.saveFile()
            write_csv(csv_output_file, CSV_CONFIG_FILE, resource)

    def saveFile(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "CSV Files (*.csv);;All Files (*)")
        self.savedReportPath.setText(f'Report saved in "{file_path}"')
        return file_path
