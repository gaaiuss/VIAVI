from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow

from src.converter import mergeJsonFiles, openReport, saveToExcel, writeCsv
from src.variables import ICON_PATH, LABEL_ICON_PATH
from src.windowUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, /, parent=None):
        # Setup Qt Designer window
        super().__init__(parent)
        self.setupUi(self)

        # Buttons functionalities
        self.selectedFiles = []
        self.selectButton.clicked.connect(self.selectFileDialog)
        self.convertButton.clicked.connect(self.generateReport)

        # Icon
        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

        # Label Logo
        self.setLabelLogo()

    def setLabelLogo(self):
        self.labelLogo.setPixmap(QPixmap(str(LABEL_ICON_PATH)))

    def selectFileDialog(self):
        fileDialog = QFileDialog(self)
        fileDialog.setNameFilter("Json (*.json)")
        fileDialog.setWindowTitle("Select Files")
        fileDialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        fileDialog.setViewMode(QFileDialog.ViewMode.Detail)

        if fileDialog.exec():
            selectedFiles = fileDialog.selectedFiles()
            self.selectedFiles = selectedFiles
            self.selectedFilesLabel.setText(
                f'{len(selectedFiles)} files selected')

    def generateReport(self):
        # Merge selected files
        resource = mergeJsonFiles(self.selectedFiles)

        # Write CSV
        writeCsv(resource)

        # Report save location
        savePath = self.getSavePath()

        # Generate excel file
        excelPath = saveToExcel(savePath)
        self.savedReportPath.setText(f'Report saved in "{excelPath}"')

        # Oper saved report
        openReport(excelPath)

    def getSavePath(self):
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Excel (*.xlsx);;All Files (*)")
        return filePath
