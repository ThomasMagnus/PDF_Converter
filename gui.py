import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from converter import PDFConverter
from qdesign import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.show_file)
        self.ui.pushButton_3.clicked.connect(self.converter)
        self.ui.pushButton_2.clicked.connect(self.delete)

        self.reset()

        self.file = ''

        self.setWindowTitle('PDF Конвертер')

    def reset(self):
        self.ui.label_2.setPixmap(QtGui.QPixmap(''))
        self.ui.label_3.setText('')
        self.ui.pushButton_2.setEnabled(False)

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')[0]
        name = os.path.basename(fname).split('.')[1]

        if name == 'pdf':
            self.file = fname

    def show_file(self):
        self.show_dialog()
        self.ui.label_2.setPixmap(QtGui.QPixmap('images/pdf_icon.png'))
        self.ui.label_3.setText(os.path.basename(self.file).split('.')[0])
        self.ui.pushButton_2.setEnabled(True)

    def converter(self):
        name = os.path.basename(self.file).split('.')[0]
        pdf_converter = PDFConverter(self.file, name)
        pdf_converter.convert_to_word()
        self.file = ''
        self.reset()

    def delete(self):
        self.file = ''
        self.reset()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
