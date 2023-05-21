from Stat_Calculations import *

main_parent = Stats("Sigurd", "Parent", 40, 20, 5, 20, 20, 10, 20, 10)
main_lvl = 30
second_parent = Stats("Deirdre", "Parent", 15, 5, 30, 15, 15, 5, 5, 30)
second_lvl = 30

child = calc_Start_Stats(main_parent, 1, second_parent, 0, "Seliph", "Sigurd")

child.print_stats()