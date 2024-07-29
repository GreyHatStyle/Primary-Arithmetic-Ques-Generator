from .designerUI import *
import sys
from PyQt6.QtWidgets import QFileDialog,QProgressBar


from tkinter import messagebox
from subprocess import run

# Local Imports
from Utils import Number_generator

class GUI_Front:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setWindowTitle("Primary Arithmetic Questions")
        
        
        self.setter()
        self.addition_page()
        MainWindow.show()
        app.exec()


    def setter(self):
        self.ui.pg2_back_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        self.ui.pg1_addition_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.pg1_addition_btn.clicked.connect(lambda: self.addition_page())
        pass

        
    def pg2_input(self):
        ans_lst = [
            self.ui.pg2_ans1_tf.text(),
            self.ui.pg2_ans2_tf.text(),
            self.ui.pg2_ans3_tf.text(),
            self.ui.pg2_ans4_tf.text(),
            self.ui.pg2_ans5_tf.text(),
            self.ui.pg2_ans6_tf.text(),
            self.ui.pg2_ans7_tf.text(),
            self.ui.pg2_ans8_tf.text(),
            self.ui.pg2_ans9_tf.text(),
        ]

        return ans_lst

    def addition_page(self):
        
        
        ques_lst = Number_generator("+").generate_number()

        self.ui.pg2_head_label.setText("Addition Test")
        self.ui.pg2_q1_label.setText(ques_lst[0])
        self.ui.pg2_q2_label.setText(ques_lst[1])
        self.ui.pg2_q3_label.setText(ques_lst[2])
        self.ui.pg2_q4_label.setText(ques_lst[3])
        self.ui.pg2_q5_label.setText(ques_lst[4])
        self.ui.pg2_q6_label.setText(ques_lst[5])
        self.ui.pg2_q7_label.setText(ques_lst[6])
        self.ui.pg2_q8_label.setText(ques_lst[7])
        self.ui.pg2_q9_label.setText(ques_lst[8])

        print(ques_lst)


        