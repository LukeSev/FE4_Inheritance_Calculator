from FE4_Stats import *
from math import floor
from random import randint

def PAR_HP_add(parent):
    return max(parent.HP - 20, 0)

def PAR_Lck_add(parent):
    return parent.Lck

# Non-HP/Lck Stat Additions
def PAR_Stat_add(parent_stat, base_stat):
    return max(parent_stat - base_stat, 0)

def CHLD_HP_add(level, growth):
    return floor(level * growth)

def CHLD_Stat_add(level, growth):
    return floor((level - 1) * growth)

def CHLD_Start_Gold(main_parent_gold, scnd_parent_gold):
    return floor((main_parent_gold + scnd_parent_gold) / 10) + 2000

def CHLD_Start_HP(main_parent_add, scnd_parent_add, child_add):
    return floor(((main_parent_add.HP * 2) + (scnd_parent_add.HP)) / 10) + child_add.HP + 20

# Note: Random number is involved with calculation, so this only provides an approximation
def CHLD_Start_Lck(main_parent_add_Lck, scnd_parent_add_Lck, child_add_Lck):
    return floor(((main_parent_add_Lck * 2) + (scnd_parent_add_Lck) + randint(1, 100)) / 10) + child_add_Lck + 1

# Non-HP/Lck Starting Stats
def CHLD_Start_Stat(main_parent_stat_add, scnd_parent_stat_add, child_parent_stat_add, child_base_stat):
    return ((floor(((main_parent_stat_add * 2) + scnd_parent_stat_add) / 10) + child_parent_stat_add) % 15) + child_base_stat

# Calculates all parent additions and returns them in stat struct
def calc_PAR_adds(parent, base_class):
    HP = PAR_HP_add(parent)
    Str = PAR_Stat_add(parent.Str, base_class.Str)
    Mag = PAR_Stat_add(parent.Mag, base_class.Mag)
    Skl = PAR_Stat_add(parent.Skl, base_class.Skl)
    Spd = PAR_Stat_add(parent.Spd, base_class.Spd)
    Lck = PAR_Lck_add(parent)
    Def = PAR_Stat_add(parent.Def, base_class.Def)
    Mdf = PAR_Stat_add(parent.Mdf, base_class.Mdf)
    return Stats(parent.Name, "additions", HP, Str, Mag, Skl, Spd, Lck, Def, Mdf)

# Calculates all child additions and returns them in stat struct
def calc_CHLD_adds(child, father):
    level = starting_levels[child]
    growths = unit_growths[child][father]
    HP = CHLD_HP_add(starting_levels[child], growths.HP)
    Str = CHLD_Stat_add(level, growths.Str)
    Mag = CHLD_Stat_add(level, growths.Mag)
    Skl = CHLD_Stat_add(level, growths.Skl)
    Spd = CHLD_Stat_add(level, growths.Spd)
    Lck = CHLD_Stat_add(level, growths.Lck)
    Def = CHLD_Stat_add(level, growths.Def)
    Mdf = CHLD_Stat_add(level, growths.Str)
    return Stats(child, "additions", HP, Str, Mag, Skl, Spd, Lck, Def, Mdf)

# Puts all the calcs together to get starting stats
# main parent and second parent are Stats objects with current parent stats
# promoted is 0 for base class, 1 for promoted class 
# child is name of child as string
def calc_Start_Stats(main_parent, main_promoted, scnd_parent, scnd_promoted, child_name, father_name):
    # Calculate additions for child and main/second parents
    child_adds = calc_CHLD_adds(child_name, father_name)
    main_class = unit_classes[main_parent.Name][main_promoted]
    main_parent_adds = calc_PAR_adds(main_parent, class_bases[main_class])
    scnd_class = unit_classes[scnd_parent.Name][scnd_promoted]
    scnd_parent_adds = calc_PAR_adds(scnd_parent, class_bases[scnd_class])

    # Calculate each stat
    child_bases = class_bases[unit_classes[child_name][0]]
    HP = CHLD_Start_HP(main_parent_adds, scnd_parent_adds, child_adds)
    Str = CHLD_Start_Stat(main_parent_adds.Str, scnd_parent_adds.Str, child_adds.Str, child_bases.Str)
    Mag = CHLD_Start_Stat(main_parent_adds.Mag, scnd_parent_adds.Mag, child_adds.Mag, child_bases.Mag)
    Skl = CHLD_Start_Stat(main_parent_adds.Skl, scnd_parent_adds.Skl, child_adds.Skl, child_bases.Skl)
    Spd = CHLD_Start_Stat(main_parent_adds.Spd, scnd_parent_adds.Spd, child_adds.Spd, child_bases.Spd)
    Lck = CHLD_Start_Lck(main_parent_adds.Lck, scnd_parent_adds.Lck, child_adds.Lck)
    Def = CHLD_Start_Stat(main_parent_adds.Def, scnd_parent_adds.Def, child_adds.Def, child_bases.Def)
    Mdf = CHLD_Start_Stat(main_parent_adds.Mdf, scnd_parent_adds.Mdf, child_adds.Mdf, child_bases.Mdf)
    return Stats(child_name, "child", HP, Str, Mag, Skl, Spd, Lck, Def, Mdf)