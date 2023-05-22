from Stat_Calculations import *
from Inheritance_GUI import *

def main():
    app = QApplication([])

    window = FE4_Calc()
    sys.exit(app.exec())

def test():
    main_parent = Stats("Sigurd", "Parent", 40, 20, 5, 20, 20, 10, 20, 10)
    main_lvl = 30
    second_parent = Stats("Deirdre", "Parent", 15, 5, 30, 15, 15, 5, 5, 30)
    second_lvl = 30

    child = calc_Start_Stats(main_parent, 1, second_parent, 0, "Seliph", "Sigurd")

    child.print_stats()

if __name__ == "__main__":
    main()