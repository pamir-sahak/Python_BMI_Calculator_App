from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from bmi import Ui_MainWindow
from PyQt5 import QtGui
import sys


class Window(QtWidgets.QMainWindow):

    # height = Ui_MainWindow.setupUi.txt_height.text()
    # weight = Ui_MainWindow.setupUi.txt_weight.text()

    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("BMI Calculator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.ui.btn_calculate.clicked.connect(self.calculate)
        self.ui.btn_Metric.clicked.connect(self.bmi_in_metric)
        self.ui.btn_standard.clicked.connect(self.bmi_in_standard)
        self.ui.btn_tips.clicked.connect(self.info)

    def info(self):  # write here bmi categories in Message box
        msg = QMessageBox()
        msg.setWindowTitle("Body Mass Index Categories")
        msg.setText("1: BMI Below 18.5  is Underweight\n"
                    "2: BMI Between 18.5 and 24.9 is Normal\n"
                    "3: BMI Between 25.0 and 29.9 is Overweight\n"
                    "4: BMI Over 30.0  is Obese")

        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowIcon(QtGui.QIcon("icon.png"))

        x = msg.exec_()

    def bmi_in_metric(self):
        self.ui.lbl_m_or_feet.setText("Meters")
        self.ui.lbl_kg_or_lbs.setText("Kg")
        self.ui.txt_height.setPlaceholderText("1.70")
        self.ui.txt_weight.setPlaceholderText("59.5")
        self.ui.txt_weight.clear()
        self.ui.txt_height.clear()

    def bmi_in_standard(self):
        self.ui.lbl_m_or_feet.setText("Inch")
        self.ui.lbl_kg_or_lbs.setText("Pounds")
        self.ui.txt_height.setPlaceholderText("66.5")
        self.ui.txt_weight.setPlaceholderText("132.3")
        self.ui.txt_weight.clear()
        self.ui.txt_height.clear()

    def calculate_metric(self):

        try:
            height = float(self.ui.txt_height.text())
            weight = float(self.ui.txt_weight.text())

            bmi = weight / (height * height)
            bmi = float("{:.3f}".format(bmi))

            if bmi >= 30.0:
                category = "Obese"
            elif (bmi >= 25.0) and (bmi <= 29.9):
                category = "Overweight"
            elif (bmi >= 18.5) and (bmi <= 24.9):
                category = "Normal"
            else:
                category = "Underweight"

            self.ui.lbl_result.setText("Result: ")

            self.ui.lbl_bmi.setText("BMI = " + str(bmi) + ", Category = " + category)

        except Exception:
            alert = "Please Enter Only Numbers"
            self.ui.lbl_bmi.setText(alert)
            self.ui.lbl_result.setText("Alert!")

    def calculate_standard(self):
        try:
            height = float(self.ui.txt_height.text())
            weight = float(self.ui.txt_weight.text())

            bmi = 703 * weight / (height * height)
            bmi = float("{:.3f}".format(bmi))

            if bmi >= 30.0:
                category = "Obese"
            elif (bmi >= 25.0) and (bmi <= 29.9):
                category = "Overweight"
            elif (bmi >= 18.5) and (bmi <= 24.9):
                category = "Normal"
            else:
                category = "Underweight"

            self.ui.lbl_result.setText("Result: ")

            self.ui.lbl_bmi.setText("BMI = " + str(bmi) + ", Category = " + category)

        except Exception:
            alert = "Please Enter Only Numbers"
            self.ui.lbl_bmi.setText(alert)
            self.ui.lbl_result.setText("Alert!")

    def calculate(self):
        label_height = self.ui.lbl_m_or_feet.text()
        label_weight = self.ui.lbl_kg_or_lbs.text()
        #  there is bug here need to be solved
        height = self.ui.txt_height.text()
        weight = self.ui.txt_weight.text()

        if ((height == "") or (weight == "")):
            alert = "Please Enter Height & Weight"
            self.ui.lbl_bmi.setText(alert)
            self.ui.lbl_result.setText("Alert!")
        elif (label_weight == "Kg") and (label_height == "Meters"):
            self.calculate_metric()
        elif (label_weight == "Pounds") and (label_height == "Inch"):
            self.calculate_standard()

        # if type(height) is str or type(weight) is str:
        #     alert = "Please Enter Only Numbers"
        #     self.ui.lbl_bmi.setText(alert)
        #     self.ui.lbl_result.setText("Alert!")


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()
