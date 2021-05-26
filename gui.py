import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QAction, QPushButton)
from main import PDFConverter
from qdesign import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_3.clicked.connect(self.converter)
        self.ui.label_2.setPixmap(QtGui.QPixmap(''))
        self.ui.label_3.setText('')
        self.file = ''

        self.setWindowTitle('PDF Конвертер')

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')[0]
        name = os.path.basename(fname).split('.')[1]
        if name == 'pdf':
            self.file = fname

    def click(self):
        self.show_dialog()
        self.ui.label_2.setPixmap(QtGui.QPixmap('pdf_icon.png'))
        self.ui.label_3.setText(os.path.basename(self.file).split('.')[0])

    def converter(self):
        pdf_converter = PDFConverter(self.file)
        pdf_converter.convert_to_word()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
