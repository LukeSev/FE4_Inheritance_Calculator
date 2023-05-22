from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QWidget,
    QMainWindow, 
    QGridLayout, 
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox
)
from PyQt6 import (
    QtGui, 
    QtWidgets
)
from PyQt6.QtCore import Qt
import sys
from Stat_Calculations import *

LIGHTBLUE = "#b8e0f5"
LIGHTTAN = "#faf2cd"

class FE4_Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FE4 Inheritance Calculator')
        self.setFixedSize(800, 600)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self.createDisplay()
        self.createForms()
        startBtn = QPushButton("start!")
        startBtn.setStyleSheet("background-color:{}".format(LIGHTBLUE))
        self.generalLayout.addWidget(startBtn)

        self.center()
        self.show()


    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(600)
        self.display.setFixedWidth(800)
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.generalLayout.addWidget(self.display)


    def createStatForm(self, title):
        statForm = QVBoxLayout()
        if(title == "Mother"):
            self.motherDropdown = self.createMotherDropdown()
            statForm.addWidget(self.motherDropdown)
        else:
            self.fatherDropdown = self.createFatherDropdown()
            statForm.addWidget(self.fatherDropdown)
        label = QLabel(self)
        label.setText(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        statForm.addWidget(label)
        formLayout = QFormLayout()
        formLayout.addRow("HP: ", QLineEdit())
        formLayout.addRow("Str:", QLineEdit())
        formLayout.addRow("Mag:", QLineEdit())
        formLayout.addRow("Skl:", QLineEdit())
        formLayout.addRow("Spd:", QLineEdit())
        formLayout.addRow("Lck:", QLineEdit())
        formLayout.addRow("Def:", QLineEdit())
        formLayout.addRow("Mdf:", QLineEdit())
        statForm.addLayout(formLayout)
        return statForm

    def createMotherDropdown(self):
        motherDropdown = QComboBox()
        motherDropdown.addItem("<Select Mother>")
        motherDropdown.addItem("Aideen")
        motherDropdown.addItem("Altena")
        motherDropdown.addItem("Ayra")
        motherDropdown.addItem("Briggid")
        motherDropdown.addItem("Deirdre")
        motherDropdown.addItem("Erinys")
        motherDropdown.addItem("Lachesis")
        motherDropdown.addItem("Sylvia")
        motherDropdown.addItem("Tiltyu")
        line_edit = QLineEdit()
        line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        motherDropdown.setLineEdit(line_edit)
        return motherDropdown

    def createFatherDropdown(self):
        fatherDropdown = QComboBox()
        fatherDropdown.addItem("<Select Father>")
        fatherDropdown.addItem("Alec")
        fatherDropdown.addItem("Arden")
        fatherDropdown.addItem("Azel")
        fatherDropdown.addItem("Beowolf")
        fatherDropdown.addItem("Claude")
        fatherDropdown.addItem("Dew")
        fatherDropdown.addItem("Finn")
        fatherDropdown.addItem("Holyn")
        fatherDropdown.addItem("Jamke")
        fatherDropdown.addItem("Lewyn")
        fatherDropdown.addItem("Lex")
        fatherDropdown.addItem("Midir")
        fatherDropdown.addItem("Noish")
        fatherDropdown.addItem("Quan")
        fatherDropdown.addItem("Sigurd")
        line_edit = QLineEdit()
        line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fatherDropdown.setLineEdit(line_edit)
        return fatherDropdown

    def createForms(self):
        formsLayout = QHBoxLayout()
        self.motherForm = self.createStatForm("Mother")
        self.fatherForm = self.createStatForm("Father")
        formsLayout.addLayout(self.motherForm)
        formsLayout.addLayout(self.fatherForm)
        self.generalLayout.addLayout(formsLayout)
        

    def startStatCalculation(self):
        return
