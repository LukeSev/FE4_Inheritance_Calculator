from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QMessageBox,
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
from PyQt6.QtGui import QPixmap
import sys
from Stat_Calculations import *

LIGHTBLUE = "#b8e0f5"
LIGHTTAN = "#faf2cd"

# For indexing into arrays
MOTHER  =   0
FATHER  =   1

LEVEL   =   0
PROMO   =   0
STATS   =   1

SON     =   0
DGHTR   =   1

PARENT_ERROR = "ERROR: Invalid Parent Combination"
STAT_ERROR = "ERROR: Invalid Stat Selection(s)"

class StatForm():
    def __init__(self, Name, Type):
        self.Name = Name
        self.Type = Type
        self.Lvl = QLineEdit()
        self.HP = QLineEdit()
        self.Str = QLineEdit()
        self.Mag = QLineEdit()
        self.Skl = QLineEdit()
        self.Spd = QLineEdit()
        self.Lck = QLineEdit()
        self.Def = QLineEdit()
        self.Mdf = QLineEdit()

class Results_Window(QWidget):
    def __init__(self, son, daughter):
        super().__init__()
        self.setWindowTitle('Results')
        self.setFixedSize(300, 400)
        if(daughter == None):
            self.setFixedSize(150, 400)
        layout = QHBoxLayout()
        son_results = create_stat_display(self, son)
        layout.addLayout(son_results)
        if(daughter != None):
            daughter_results = create_stat_display(self, daughter)
            layout.addLayout(daughter_results)
        self.setLayout(layout)

class FE4_Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.results = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('FE4 Inheritance Calculator')
        self.setFixedSize(800, 600)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        logo = QLabel(self)
        logo.setPixmap(QPixmap('FE4_Logo.png'))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.generalLayout.addWidget(logo)

        self.forms = [StatForm("Mother", "Parent"), StatForm("Father", "Parent")]
        self.create_forms()
        startBtn = QPushButton("start!")
        startBtn.setStyleSheet("background-color:{}".format(LIGHTBLUE))
        startBtn.clicked.connect(self.calculate_children_stats)
        self.generalLayout.addWidget(startBtn)
        
        self.center()
        self.show()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def display_error_msg(error_msg):
        msg_box = QMessageBox()
        msg_box.setText(error_msg)
        msg_box.exec()

    def create_stat_form(self, title):
        statForm = QVBoxLayout()
        if(title == "Mother"):
            self.motherDropdown = self.create_mother_dropdown()
            statForm.addWidget(self.motherDropdown)
            form = MOTHER
        else:
            self.fatherDropdown = self.create_father_dropdown()
            statForm.addWidget(self.fatherDropdown)
            form = FATHER
        label = QLabel(self)
        label.setText(title)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        statForm.addWidget(label)
        formLayout = QFormLayout()
        formLayout.addRow("Lvl:", self.forms[form].Lvl)
        formLayout.addRow("HP: ", self.forms[form].HP)
        formLayout.addRow("Str:", self.forms[form].Str)
        formLayout.addRow("Mag:", self.forms[form].Mag)
        formLayout.addRow("Skl:", self.forms[form].Skl)
        formLayout.addRow("Spd:", self.forms[form].Spd)
        formLayout.addRow("Lck:", self.forms[form].Lck)
        formLayout.addRow("Def:", self.forms[form].Def)
        formLayout.addRow("Mdf:", self.forms[form].Mdf)
        statForm.addLayout(formLayout)
        return statForm

    def create_mother_dropdown(self):
        motherDropdown = QComboBox()
        motherDropdown.addItem("<Select Mother>")
        motherDropdown.addItem("Aideen")
        motherDropdown.addItem("Ayra")
        motherDropdown.addItem("Briggid")
        motherDropdown.addItem("Deirdre")
        motherDropdown.addItem("Erinys")
        motherDropdown.addItem("Ethlin")
        motherDropdown.addItem("Lachesis")
        motherDropdown.addItem("Sylvia")
        motherDropdown.addItem("Tiltyu")
        return motherDropdown

    def create_father_dropdown(self):
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
        return fatherDropdown

    def create_forms(self):
        formsLayout = QHBoxLayout()
        self.motherForm = self.create_stat_form("Mother")
        self.fatherForm = self.create_stat_form("Father")
        formsLayout.addLayout(self.motherForm)
        formsLayout.addLayout(self.fatherForm)
        self.generalLayout.addLayout(formsLayout)

    def generate_stats(self, form):
        if(form.Name == "Mother"):
            name = self.motherDropdown.currentText()
        else:
            name = self.fatherDropdown.currentText()
        stats = Stats(
            name, 
            form.Type,
            int(form.HP.text()),
            int(form.Str.text()),
            int(form.Mag.text()),
            int(form.Skl.text()),
            int(form.Spd.text()),
            int(form.Lck.text()),
            int(form.Def.text()),
            int(form.Mdf.text())
        )
        return (int(form.Lvl.text()), stats)

    def display_results(self, son, daughter):
        return


    def calculate_children_stats(self):
        # Generate stats from forms
        mother_info = self.generate_stats(self.forms[MOTHER])
        mother_stats = mother_info[STATS]
        if(mother_info[LEVEL] >= 20):
            mother_promoted = 1
        else:
            mother_promoted = 0

        father_info = self.generate_stats(self.forms[FATHER])
        father_stats = father_info[STATS]
        if(father_info[LEVEL] >= 20):
            father_promoted = 1
        else:
            father_promoted = 0

        # Check for invalid pairings
        if(
            (mother_stats.Name == "Ethlin" and father_stats.Name != "Quan")     or
            (father_stats.Name == "Quan" and mother_stats.Name != "Ethlin")     or
            (mother_stats.Name == "Deirdre" and father_stats.Name != "Sigurd")  or
            (father_stats.Name == "Sigurd" and mother_stats.Name != "Deirdre")  ):  
                self.display_error_msg(PARENT_ERROR)
                return -1

        # Check for valid stat fields
        if(
            check_valid_stats(mother_stats, max_stats[unit_classes[mother_stats.Name][mother_promoted]]) == -1   or
            check_valid_stats(father_stats, max_stats[unit_classes[father_stats.Name][father_promoted]]) == -1   ):
                self.display_error_msg(STAT_ERROR)
                return -1

        # Account for the mothers that reverse inheritance role
        if mother_stats.Name in main_mothers:
            son_parent = [mother_promoted, mother_stats]
            daughter_parent = [father_promoted, father_stats]
        else:
            son_parent = [father_promoted, father_stats]
            daughter_parent = [mother_promoted, mother_stats]
        
        # Calculate stats for both children, excluding Sigurd
        son = calc_start_stats(son_parent[STATS], son_parent[PROMO], daughter_parent[STATS], daughter_parent[PROMO], children[mother_stats.Name][SON], father_stats.Name)
        if(father_stats.Name == "Sigurd"): 
            daughter = None
        else: 
            daughter = calc_start_stats(daughter_parent[STATS], daughter_parent[PROMO], son_parent[STATS], son_parent[PROMO], children[mother_stats.Name][DGHTR], father_stats.Name)

        # Display results
        if self.results is None:
            self.results = Results_Window(son, daughter)
        self.results.show()
        return 0

def create_stat_label(text):
        label = QLabel()
        label.setText(text)
        return label

def create_stat_display(self, stats):
        stat_display = QVBoxLayout()
        stat_display.addWidget(create_stat_label(str(stats.Name)))
        stat_display.addWidget(create_stat_label("HP:  {}".format(str(stats.HP))))
        stat_display.addWidget(create_stat_label("Str: {}".format(str(stats.Str))))
        stat_display.addWidget(create_stat_label("Mag: {}".format(str(stats.Mag))))
        stat_display.addWidget(create_stat_label("Skl: {}".format(str(stats.Skl))))
        stat_display.addWidget(create_stat_label("Spd: {}".format(str(stats.Spd))))
        stat_display.addWidget(create_stat_label("Lck: {}".format(str(stats.Lck))))
        stat_display.addWidget(create_stat_label("Def: {}".format(str(stats.Def))))
        stat_display.addWidget(create_stat_label("Mdf: {}".format(str(stats.Mdf))))
        return stat_display