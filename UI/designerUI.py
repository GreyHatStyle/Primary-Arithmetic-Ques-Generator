# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1437, 825)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(parent=self.page)
        self.frame.setGeometry(QtCore.QRect(470, 30, 601, 121))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.welcome_label = QtWidgets.QLabel(parent=self.frame)
        self.welcome_label.setGeometry(QtCore.QRect(80, 30, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.frame_2 = QtWidgets.QFrame(parent=self.page)
        self.frame_2.setGeometry(QtCore.QRect(50, 220, 661, 531))
        self.frame_2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.welcome_label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.welcome_label_2.setGeometry(QtCore.QRect(210, 20, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label_2.setFont(font)
        self.welcome_label_2.setObjectName("welcome_label_2")
        self.pg1_addition_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.pg1_addition_btn.setGeometry(QtCore.QRect(210, 130, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg1_addition_btn.setFont(font)
        self.pg1_addition_btn.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(12, 44, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(0, 2, 147);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(75, 192, 255);\n"
"}\n"
"")
        self.pg1_addition_btn.setObjectName("pg1_addition_btn")
        self.pg1_subtraction_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.pg1_subtraction_btn.setGeometry(QtCore.QRect(210, 220, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg1_subtraction_btn.setFont(font)
        self.pg1_subtraction_btn.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(12, 44, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(0, 2, 147);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(75, 192, 255);\n"
"}\n"
"")
        self.pg1_subtraction_btn.setObjectName("pg1_subtraction_btn")
        self.pg1_multi_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.pg1_multi_btn.setGeometry(QtCore.QRect(210, 310, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg1_multi_btn.setFont(font)
        self.pg1_multi_btn.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(12, 44, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(0, 2, 147);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(75, 192, 255);\n"
"}\n"
"")
        self.pg1_multi_btn.setObjectName("pg1_multi_btn")
        self.pg1_division_btn = QtWidgets.QPushButton(parent=self.frame_2)
        self.pg1_division_btn.setGeometry(QtCore.QRect(210, 400, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg1_division_btn.setFont(font)
        self.pg1_division_btn.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(12, 44, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(0, 2, 147);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(75, 192, 255);\n"
"}\n"
"")
        self.pg1_division_btn.setObjectName("pg1_division_btn")
        self.frame_3 = QtWidgets.QFrame(parent=self.page)
        self.frame_3.setGeometry(QtCore.QRect(810, 220, 661, 531))
        self.frame_3.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(520, 0, 601, 121))
        self.frame_4.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pg2_head_label = QtWidgets.QLabel(parent=self.frame_4)
        self.pg2_head_label.setGeometry(QtCore.QRect(80, 30, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_head_label.setFont(font)
        self.pg2_head_label.setObjectName("pg2_head_label")
        self.pg2_frame1 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame1.setGeometry(QtCore.QRect(30, 140, 221, 301))
        self.pg2_frame1.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame1.setObjectName("pg2_frame1")
        self.pg2_q1_label = QtWidgets.QLabel(parent=self.pg2_frame1)
        self.pg2_q1_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q1_label.setFont(font)
        self.pg2_q1_label.setObjectName("pg2_q1_label")
        self.pg2_ans1_tf = QtWidgets.QLineEdit(parent=self.pg2_frame1)
        self.pg2_ans1_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans1_tf.setFont(font)
        self.pg2_ans1_tf.setObjectName("pg2_ans1_tf")
        self.pg2_corr1_label = QtWidgets.QLabel(parent=self.pg2_frame1)
        self.pg2_corr1_label.setGeometry(QtCore.QRect(30, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr1_label.setFont(font)
        self.pg2_corr1_label.setText("")
        self.pg2_corr1_label.setObjectName("pg2_corr1_label")
        self.pg2_frame6 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame6.setGeometry(QtCore.QRect(30, 470, 221, 301))
        self.pg2_frame6.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame6.setObjectName("pg2_frame6")
        self.pg2_q6_label = QtWidgets.QLabel(parent=self.pg2_frame6)
        self.pg2_q6_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q6_label.setFont(font)
        self.pg2_q6_label.setObjectName("pg2_q6_label")
        self.pg2_ans6_tf = QtWidgets.QLineEdit(parent=self.pg2_frame6)
        self.pg2_ans6_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans6_tf.setFont(font)
        self.pg2_ans6_tf.setObjectName("pg2_ans6_tf")
        self.pg2_corr6_label = QtWidgets.QLabel(parent=self.pg2_frame6)
        self.pg2_corr6_label.setGeometry(QtCore.QRect(20, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr6_label.setFont(font)
        self.pg2_corr6_label.setText("")
        self.pg2_corr6_label.setObjectName("pg2_corr6_label")
        self.pg2_frame9 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame9.setGeometry(QtCore.QRect(930, 470, 221, 301))
        self.pg2_frame9.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame9.setObjectName("pg2_frame9")
        self.pg2_q9_label = QtWidgets.QLabel(parent=self.pg2_frame9)
        self.pg2_q9_label.setGeometry(QtCore.QRect(20, 10, 171, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q9_label.setFont(font)
        self.pg2_q9_label.setObjectName("pg2_q9_label")
        self.pg2_ans9_tf = QtWidgets.QLineEdit(parent=self.pg2_frame9)
        self.pg2_ans9_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans9_tf.setFont(font)
        self.pg2_ans9_tf.setObjectName("pg2_ans9_tf")
        self.pg2_corr9_label = QtWidgets.QLabel(parent=self.pg2_frame9)
        self.pg2_corr9_label.setGeometry(QtCore.QRect(10, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr9_label.setFont(font)
        self.pg2_corr9_label.setText("")
        self.pg2_corr9_label.setObjectName("pg2_corr9_label")
        self.pg2_result_btn = QtWidgets.QPushButton(parent=self.page_2)
        self.pg2_result_btn.setGeometry(QtCore.QRect(1190, 490, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg2_result_btn.setFont(font)
        self.pg2_result_btn.setStyleSheet(" QPushButton {\n"
"    \n"
"    background-color: rgb(255, 230, 44);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    \n"
"    background-color: rgb(255, 183, 0);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(255, 240, 153);\n"
"}\n"
"")
        self.pg2_result_btn.setObjectName("pg2_result_btn")
        self.pg2_frame2 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame2.setGeometry(QtCore.QRect(330, 140, 221, 301))
        self.pg2_frame2.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame2.setObjectName("pg2_frame2")
        self.pg2_q2_label = QtWidgets.QLabel(parent=self.pg2_frame2)
        self.pg2_q2_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q2_label.setFont(font)
        self.pg2_q2_label.setObjectName("pg2_q2_label")
        self.pg2_ans2_tf = QtWidgets.QLineEdit(parent=self.pg2_frame2)
        self.pg2_ans2_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans2_tf.setFont(font)
        self.pg2_ans2_tf.setObjectName("pg2_ans2_tf")
        self.pg2_corr2_label = QtWidgets.QLabel(parent=self.pg2_frame2)
        self.pg2_corr2_label.setGeometry(QtCore.QRect(30, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr2_label.setFont(font)
        self.pg2_corr2_label.setText("")
        self.pg2_corr2_label.setObjectName("pg2_corr2_label")
        self.pg2_frame3 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame3.setGeometry(QtCore.QRect(630, 140, 221, 301))
        self.pg2_frame3.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame3.setObjectName("pg2_frame3")
        self.pg2_q3_label = QtWidgets.QLabel(parent=self.pg2_frame3)
        self.pg2_q3_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q3_label.setFont(font)
        self.pg2_q3_label.setObjectName("pg2_q3_label")
        self.pg2_ans3_tf = QtWidgets.QLineEdit(parent=self.pg2_frame3)
        self.pg2_ans3_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans3_tf.setFont(font)
        self.pg2_ans3_tf.setObjectName("pg2_ans3_tf")
        self.pg2_corr3_label = QtWidgets.QLabel(parent=self.pg2_frame3)
        self.pg2_corr3_label.setGeometry(QtCore.QRect(30, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr3_label.setFont(font)
        self.pg2_corr3_label.setText("")
        self.pg2_corr3_label.setObjectName("pg2_corr3_label")
        self.pg2_frame4 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame4.setGeometry(QtCore.QRect(930, 140, 221, 301))
        self.pg2_frame4.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame4.setObjectName("pg2_frame4")
        self.pg2_q4_label = QtWidgets.QLabel(parent=self.pg2_frame4)
        self.pg2_q4_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q4_label.setFont(font)
        self.pg2_q4_label.setObjectName("pg2_q4_label")
        self.pg2_ans4_tf = QtWidgets.QLineEdit(parent=self.pg2_frame4)
        self.pg2_ans4_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans4_tf.setFont(font)
        self.pg2_ans4_tf.setObjectName("pg2_ans4_tf")
        self.pg2_corr4_label = QtWidgets.QLabel(parent=self.pg2_frame4)
        self.pg2_corr4_label.setGeometry(QtCore.QRect(30, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr4_label.setFont(font)
        self.pg2_corr4_label.setText("")
        self.pg2_corr4_label.setObjectName("pg2_corr4_label")
        self.pg2_frame5 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame5.setGeometry(QtCore.QRect(1230, 140, 221, 301))
        self.pg2_frame5.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame5.setObjectName("pg2_frame5")
        self.pg2_q5_label = QtWidgets.QLabel(parent=self.pg2_frame5)
        self.pg2_q5_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q5_label.setFont(font)
        self.pg2_q5_label.setObjectName("pg2_q5_label")
        self.pg2_ans5_tf = QtWidgets.QLineEdit(parent=self.pg2_frame5)
        self.pg2_ans5_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans5_tf.setFont(font)
        self.pg2_ans5_tf.setObjectName("pg2_ans5_tf")
        self.pg2_corr5_label = QtWidgets.QLabel(parent=self.pg2_frame5)
        self.pg2_corr5_label.setGeometry(QtCore.QRect(30, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr5_label.setFont(font)
        self.pg2_corr5_label.setText("")
        self.pg2_corr5_label.setObjectName("pg2_corr5_label")
        self.pg2_frame7 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame7.setGeometry(QtCore.QRect(330, 470, 221, 301))
        self.pg2_frame7.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame7.setObjectName("pg2_frame7")
        self.pg2_q7_label = QtWidgets.QLabel(parent=self.pg2_frame7)
        self.pg2_q7_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q7_label.setFont(font)
        self.pg2_q7_label.setObjectName("pg2_q7_label")
        self.pg2_ans7_tf = QtWidgets.QLineEdit(parent=self.pg2_frame7)
        self.pg2_ans7_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans7_tf.setFont(font)
        self.pg2_ans7_tf.setObjectName("pg2_ans7_tf")
        self.pg2_corr7_label = QtWidgets.QLabel(parent=self.pg2_frame7)
        self.pg2_corr7_label.setGeometry(QtCore.QRect(20, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr7_label.setFont(font)
        self.pg2_corr7_label.setText("")
        self.pg2_corr7_label.setObjectName("pg2_corr7_label")
        self.pg2_frame8 = QtWidgets.QFrame(parent=self.page_2)
        self.pg2_frame8.setGeometry(QtCore.QRect(630, 470, 221, 301))
        self.pg2_frame8.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(209, 209, 209);\n"
"    border-radius: 10px;\n"
"}")
        self.pg2_frame8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.pg2_frame8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.pg2_frame8.setObjectName("pg2_frame8")
        self.pg2_q8_label = QtWidgets.QLabel(parent=self.pg2_frame8)
        self.pg2_q8_label.setGeometry(QtCore.QRect(40, 10, 151, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_q8_label.setFont(font)
        self.pg2_q8_label.setObjectName("pg2_q8_label")
        self.pg2_ans8_tf = QtWidgets.QLineEdit(parent=self.pg2_frame8)
        self.pg2_ans8_tf.setGeometry(QtCore.QRect(30, 160, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_ans8_tf.setFont(font)
        self.pg2_ans8_tf.setObjectName("pg2_ans8_tf")
        self.pg2_corr8_label = QtWidgets.QLabel(parent=self.pg2_frame8)
        self.pg2_corr8_label.setGeometry(QtCore.QRect(20, 240, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pg2_corr8_label.setFont(font)
        self.pg2_corr8_label.setText("")
        self.pg2_corr8_label.setObjectName("pg2_corr8_label")
        self.pg2_clear_btn = QtWidgets.QPushButton(parent=self.page_2)
        self.pg2_clear_btn.setGeometry(QtCore.QRect(1190, 590, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg2_clear_btn.setFont(font)
        self.pg2_clear_btn.setStyleSheet(" QPushButton {\n"
"    \n"
"    background-color: rgb(30, 203, 27);\n"
"    border: 2px  solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(10, 186, 1);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(0, 255, 128);\n"
"}")
        self.pg2_clear_btn.setObjectName("pg2_clear_btn")
        self.pg2_back_btn = QtWidgets.QPushButton(parent=self.page_2)
        self.pg2_back_btn.setGeometry(QtCore.QRect(1190, 690, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pg2_back_btn.setFont(font)
        self.pg2_back_btn.setStyleSheet(" QPushButton {\n"
"    background-color: rgb(12, 44, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(0, 2, 147);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(75, 192, 255);\n"
"}")
        self.pg2_back_btn.setObjectName("pg2_back_btn")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1437, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome Chinu Bisht"))
        self.welcome_label_2.setText(_translate("MainWindow", "Start Test"))
        self.pg1_addition_btn.setText(_translate("MainWindow", "Addition"))
        self.pg1_subtraction_btn.setText(_translate("MainWindow", "Subtraction"))
        self.pg1_multi_btn.setText(_translate("MainWindow", "Multiplication"))
        self.pg1_division_btn.setText(_translate("MainWindow", "Division"))
        self.pg2_head_label.setText(_translate("MainWindow", "Addition Test"))
        self.pg2_q1_label.setText(_translate("MainWindow", "   76\n"
"+ 34"))
        self.pg2_q6_label.setText(_translate("MainWindow", "   760\n"
"+ 314"))
        self.pg2_q9_label.setText(_translate("MainWindow", "   76111\n"
"+ 34534"))
        self.pg2_result_btn.setText(_translate("MainWindow", "Result"))
        self.pg2_q2_label.setText(_translate("MainWindow", "   76\n"
"+ 34"))
        self.pg2_q3_label.setText(_translate("MainWindow", "   76\n"
"+ 34"))
        self.pg2_q4_label.setText(_translate("MainWindow", "   76\n"
"+ 34"))
        self.pg2_q5_label.setText(_translate("MainWindow", "   76\n"
"+ 34"))
        self.pg2_q7_label.setText(_translate("MainWindow", "   760\n"
"+ 314"))
        self.pg2_q8_label.setText(_translate("MainWindow", "   760\n"
"+ 314"))
        self.pg2_clear_btn.setText(_translate("MainWindow", "Submit"))
        self.pg2_back_btn.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
