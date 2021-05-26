import os

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication, QAction, QPushButton)
from PyQt5.QtGui import QIcon
from qdesign import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # open_file = QAction('Найти файл', self)
        # open_file.setShortcut('Ctr + O')
        # open_file.setStatusTip('Найти файл')
        #
        # open_file.triggered.connect(self.show_dialog)
        #
        # menu_bar = self.menuBar()
        # file_menu = menu_bar.addMenu('&Файл')
        # file_menu.addAction(open_file)

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.label_2.setPixmap(QtGui.QPixmap(''))

        self.setWindowTitle('PDF Конвертер')

    def show_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File')[0]
        name = os.path.basename(fname).split('.')[1]
        if name == 'txt':
            return fname

    def click(self):
        with open(self.show_dialog(), 'r') as file:
            res = file.read()
            print(res)
            self.ui.label_2.setPixmap(QtGui.QPixmap('pdf_icon.png'))


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
