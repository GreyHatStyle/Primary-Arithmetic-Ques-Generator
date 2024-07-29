from .designerUI import *
import sys
from PyQt6.QtWidgets import QFileDialog,QProgressBar

from tkinter import messagebox
from subprocess import run



class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle("Primary Arithmetic Questions")
        
        
        self.setter()
        MainWindow.show()
        app.exec()


    def setter(self):
        self.ui.pg1_addition_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        pass