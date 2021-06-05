# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 403)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(20, 310, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_result.setFont(font)
        self.lbl_result.setStyleSheet("color: #2B244F;")
        self.lbl_result.setObjectName("lbl_result")
        self.lbl_bmi = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bmi.setGeometry(QtCore.QRect(20, 350, 380, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_bmi.setFont(font)
        self.lbl_bmi.setStyleSheet("QLabel{\n"
"border: 2px solid #FDC62D;\n"
"border-radius: 10px;\n"
"color: #2B244F;\n"
"}\n"
"QLabel::hover{\n"
"border: 3px solid rgb(230, 180, 40);\n"
"border-radius: 10px;\n"
"}")
        self.lbl_bmi.setObjectName("lbl_bmi")
        self.lbl_height = QtWidgets.QLabel(self.centralwidget)
        self.lbl_height.setGeometry(QtCore.QRect(20, 100, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_height.setFont(font)
        self.lbl_height.setStyleSheet("color: #2B244F;")
        self.lbl_height.setObjectName("lbl_height")
        self.btn_Metric = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Metric.setGeometry(QtCore.QRect(100, 30, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_Metric.setFont(font)
        self.btn_Metric.setStyleSheet("QPushButton{\n"
"background-color: #fff;\n"
"color: #2B244F;;\n"
"border: 2px solid #FDC62D;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"\n"
"QPushButton::focus{\n"
"background-color: #FDC62D;\n"
"color: #2B244F;;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(253, 211, 83);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.btn_Metric.setObjectName("btn_Metric")
        self.btn_standard = QtWidgets.QPushButton(self.centralwidget)
        self.btn_standard.setGeometry(QtCore.QRect(260, 30, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_standard.setFont(font)
        self.btn_standard.setStyleSheet("QPushButton{\n"
"background-color: #fff;\n"
"color: #2B244F;;\n"
"border: 2px solid #FDC62D;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::focus{\n"
"background-color: #FDC62D;\n"
"color: #2B244F;;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(253, 211, 83);\n"
"\n"
"}")
        self.btn_standard.setObjectName("btn_standard")
        self.txt_height = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_height.setGeometry(QtCore.QRect(100, 100, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_height.setFont(font)
        self.txt_height.setStyleSheet("QLineEdit{\n"
"border: 2px solid #FDC62D;\n"
"border-radius: 10px;\n"
"color: #2B244F;\n"
"}\n"
"QLineEdit::hover{\n"
"border: 3px solid rgb(230, 180, 40);\n"
"border-radius: 10px;\n"
"}")
        self.txt_height.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_height.setObjectName("txt_height")
        self.lbl_m_or_feet = QtWidgets.QLabel(self.centralwidget)
        self.lbl_m_or_feet.setGeometry(QtCore.QRect(334, 103, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_m_or_feet.setFont(font)
        self.lbl_m_or_feet.setStyleSheet("QLabel{\n"
"color: #2B244F;\n"
"background-color: none;\n"
"}")
        self.lbl_m_or_feet.setObjectName("lbl_m_or_feet")
        self.btn_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculate.setGeometry(QtCore.QRect(100, 240, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_calculate.setFont(font)
        self.btn_calculate.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #FDC62D;\n"
"color: #2B244F;;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(253, 211, 83);\n"
"\n"
"}")
        self.btn_calculate.setObjectName("btn_calculate")
        self.btn_tips = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tips.setGeometry(QtCore.QRect(340, 300, 55, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_tips.setFont(font)
        self.btn_tips.setStyleSheet("\n"
"QPushButton{\n"
"background-color: #FDC62D;\n"
"color: #2B244F;;\n"
"border-radius: 10px;\n"
"cursor: pointer;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(253, 211, 83);\n"
"\n"
"}")
        self.btn_tips.setObjectName("btn_tips")
        self.lbl_weight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_weight.setGeometry(QtCore.QRect(20, 170, 70, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_weight.setFont(font)
        self.lbl_weight.setStyleSheet("color: #2B244F;")
        self.lbl_weight.setObjectName("lbl_weight")
        self.txt_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_weight.setGeometry(QtCore.QRect(100, 170, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_weight.setFont(font)
        self.txt_weight.setStyleSheet("QLineEdit{\n"
"border: 2px solid #FDC62D;\n"
"border-radius: 10px;\n"
"color: #2B244F;\n"
"}\n"
"QLineEdit::hover{\n"
"border: 3px solid rgb(230, 180, 40);\n"
"border-radius: 10px;\n"
"}")
        self.txt_weight.setInputMethodHints(QtCore.Qt.ImhNone)
        self.txt_weight.setInputMask("")
        self.txt_weight.setText("")
        self.txt_weight.setObjectName("txt_weight")
        self.lbl_kg_or_lbs = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kg_or_lbs.setGeometry(QtCore.QRect(330, 173, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_kg_or_lbs.setFont(font)
        self.lbl_kg_or_lbs.setStyleSheet("QLabel{\n"
"color: #2B244F;\n"
"background-color: none;\n"
"}")
        self.lbl_kg_or_lbs.setObjectName("lbl_kg_or_lbs")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_result.setText(_translate("MainWindow", "Result: "))
        self.lbl_bmi.setText(_translate("MainWindow", "Your Result Will Be Shown Here"))
        self.lbl_height.setText(_translate("MainWindow", "Height: "))
        self.btn_Metric.setText(_translate("MainWindow", "Metric"))
        self.btn_standard.setText(_translate("MainWindow", "Standard"))
        self.txt_height.setToolTip(_translate("MainWindow", "Use . for decimal digit"))
        self.txt_height.setPlaceholderText(_translate("MainWindow", "1.70"))
        self.lbl_m_or_feet.setText(_translate("MainWindow", "Meters"))
        self.btn_calculate.setText(_translate("MainWindow", "Calculate"))
        self.btn_tips.setText(_translate("MainWindow", "?"))
        self.lbl_weight.setText(_translate("MainWindow", "Weight:"))
        self.txt_weight.setToolTip(_translate("MainWindow", "Use . for decimal digit"))
        self.txt_weight.setPlaceholderText(_translate("MainWindow", "59.5"))
        self.lbl_kg_or_lbs.setText(_translate("MainWindow", "Kg"))