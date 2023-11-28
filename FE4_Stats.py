# Note: Class Base Stats, as well as inheritance calculations were all obtained from the Serenes Forest page for FE4
class Stats:
    def __init__(self, Name, Type, HP, Str, Mag, Skl, Spd, Lck, Def, Mdf):
        self.Name = Name
        self.Type = Type
        self.HP = HP
        self.Str = Str
        self.Mag = Mag
        self.Skl = Skl
        self.Spd = Spd
        self.Lck = Lck
        self.Def = Def
        self.Mdf = Mdf
    
    def print_stats(self):
        print("\n{}\n\tHP: \t{}\n\tStr: \t{}\n\tMag: \t{}\n\tSkl: \t{}\n\tSpd: \t{}\n\tLck: \t{}\n\tDef: \t{}\n\tMdf: \t{}\n"
              .format(self.Name, self.HP, self.Str, self.Mag, self.Skl, self.Spd, self.Lck, self.Def, self.Mdf))

# Note: 'Cavalier' referse to Social, Lance, Arch, Axe, and Free Knight, which all have the same base stats
class_bases = {
    "Junior Lord":      Stats("", "Class", 30, 5, 0, 5, 5, 0, 5, 0),
    "Lord Knight":      Stats("", "Class", 34, 10, 0, 7, 7, 0, 7, 3),
    "Sword Armour":     Stats("", "Class", 34, 9, 0, 5, 3, 0, 10, 0),
    "General":          Stats("", "Class", 34, 10, 0, 6, 5, 0, 12, 3),
    "Troubadour":       Stats("", "Class", 32, 3, 3, 6, 6, 0, 3, 3),
    "Cavalier":         Stats("", "Class", 30, 7, 0, 6, 6, 0, 6, 0),
    "Paladin":          Stats("", "Class", 40, 9, 5, 9, 9, 0, 9, 5),
    "Duke Knight":      Stats("", "Class", 40, 12, 0, 7, 7, 0, 8, 3),
    "Bow Knight":       Stats("", "Class", 40, 10, 0, 8, 8, 0, 8, 3),
    "Great Knight":     Stats("", "Class", 40, 12, 0, 7, 7, 0, 10, 3),
    "Forrest Knight":   Stats("", "Class", 40, 8, 0, 15, 12, 0, 8, 3),
    "Mage":             Stats("", "Class", 26, 0, 7, 6, 6, 0, 1, 5),
    "Mage Knight":      Stats("", "Class", 40, 5, 10, 7, 7, 0, 5, 7),
    "Priest":           Stats("", "Class", 26, 0, 7, 6, 6, 0, 1, 7),
    "High Priest":      Stats("", "Class", 35, 0, 12, 9, 8, 0, 3, 8),
    "Thief":            Stats("", "Class", 26, 3, 0, 3, 7, 0, 1, 0),
    "Thief Fighter":     Stats("", "Class", 30, 7, 3, 7, 12, 0, 5, 3),
    "Swordfighter":     Stats("", "Class", 30, 7, 0, 10, 10, 0, 5, 0),
    "Swordmaster":      Stats("", "Class", 40, 12, 0, 15, 15, 0, 7, 3),
    "Forrest":          Stats("", "Class", 40, 12, 3, 12, 12, 0, 7, 3),
    "Shaman":           Stats("", "Class", 30, 0, 8, 7, 7, 0, 3, 10),
    "Bow Fighter":      Stats("", "Class", 30, 7, 0, 10, 10, 0, 5, 0),
    "Sniper":           Stats("", "Class", 40, 12, 0, 12, 12, 0, 7, 3),
    "Prince":           Stats("", "Class", 30, 8, 2, 7, 6, 0, 7, 3),
    "Princess":         Stats("", "Class", 26, 5, 7, 5, 8, 0, 5, 7),
    "Master Knight":    Stats("", "Class", 40, 12, 7, 12, 12, 0, 12, 7),
    "Bard":             Stats("", "Class", 30, 0, 7, 7, 10, 0, 3, 7),
    "Sage":             Stats("", "Class", 35, 0, 15, 12, 15, 0, 3, 12),
    "Dancer":           Stats("", "Class", 26, 3, 0, 1, 7, 0, 1, 3),
    "Pegasus Knight":   Stats("", "Class", 35, 7, 0, 7, 12, 0, 5, 7),
    "Falcon Knight":    Stats("", "Class", 40, 7, 7, 12, 15, 0, 6, 12),
    "Thunder Mage":     Stats("", "Class", 26, 0, 7, 9, 6, 0, 1, 5),
    "Mage Fighter (F)": Stats("", "Class", 26, 3, 12, 9, 12, 0, 5, 10),
    "Dragon Knight":    Stats("", "Class", 40, 10, 0, 7, 6, 0, 11, 0)
}

promo_bonuses = {
    ("Cavalier", "Paladin (M)"): Stats("", "Promo", 0, 2, 5, 3, 3, 0, 3, 5),
    ("Cavalier", "Duke Knight"): Stats("", "Promo", 0, 5, 0, 1, 1, 0, 2, 3),
    ("Cavalier", "Bow Knight"): Stats("", "Promo", 0, 3, 0, 2, 2, 0, 2, 3),
    ("Cavalier", "Great Knight"): Stats("", "Promo", 0, 5, 0, 1, 1, 0, 4, 3),
    ("Cavalier", "Forrest Knight"): Stats("", "Promo", 0, 1, 0, 9, 6, 0, 2, 3),
    ("Troubadour", "Paladin (F)"): Stats("", "Promo", 0, 6, 2, 3, 3, 0, 6, 2),
    ("Pegasus Knight","Falcon Knight"): Stats("", "Promo", 0, 0, 7, 3, 3, 0, 1, 5),
    ("Dragon Knight","Dragon Master"): Stats("", "Promo", 0, 2, 0, 2, 1, 0, 3, 0),
    ("Bow Fighter","Sniper"): Stats("", "Promo", 0, 5, 0, 2, 2, 0, 2, 3),
    ("Swordfighter","Forrest"): Stats("", "Promo", 0, 5, 3, 2, 2, 0, 2, 3),
    ("Swordfighter","Swordmaster"): Stats("", "Promo", 0, 5, 0, 5, 5, 0, 2, 3),
    ("Sword Armour","General"): Stats("", "Promo", 0, 1, 0, 1, 2, 0, 2, 3),
    ("Axe Fighter","Warrior"): Stats("", "Promo", 0, 3, 0, 2, 2, 0, 2, 3),
    ("Junior Lord","Lord Knight"): Stats("", "Promo", 0, 5, 0, 2, 2, 0, 2, 3),
    ("Prince","Master Knight"): Stats("", "Promo", 0, 4, 4, 5, 6, 0, 5, 4),
    ("Princess","Master Knight"): Stats("", "Promo", 0, 7, 0, 7, 4, 0, 7, 0),
    ("Priest","High Priest"): Stats("", "Promo", 0, 0, 5, 3, 2, 0, 2, 1),
    ("Mage","Mage Knight"): Stats("", "Promo", 0, 5, 3, 1, 1, 0, 4, 2),
    ("Mage","Mage Fighter (F)"): Stats("", "Promo", 0, 3, 5, 3, 6, 0, 4, 5),
    ("Thunder Mage","Mage Fighter (F)"): Stats("", "Promo", 0, 3, 5, 0, 6, 0, 4, 5),
    ("Wind Mage","Mage Fighter (F)"): Stats("", "Promo", 0, 5, 5, 4, 4, 0, 6, 3),
    ("Bard","Sage"): Stats("", "Promo", 0, 0, 8, 5, 5, 0, 0, 5),
    ("Shaman","Sage"): Stats("", "Promo", 0, 0, 7, 5, 8, 0, 0, 2),
    ("Thief","Thief Fighter"): Stats("", "Promo", 0, 4, 3, 4, 5, 0, 4, 3)
}

unit_bases = {
    "Sigurd":   Stats("Sigurd", "Bases", 35, 14, 0, 11, 12, 7, 9, 3),
    "Noish":    Stats("Noish", "Bases", 33, 11, 0, 7, 8, 5, 8, 0),
    "Alec":     Stats("Alec", "Bases", 32, 9, 0, 9, 10, 4, 7, 0),
    "Arden":    Stats("Arden", "Bases", 36, 13, 0, 5, 4, 3, 13, 0),
    "Quan":     Stats("Quan", "Bases", 34, 16, 0, 10, 10, 5, 10, 3),
    "Ethlin":   Stats("Ethlin", "Bases", 28, 5, 8, 11, 12, 8, 4, 6),
    "Finn":     Stats("Finn", "Bases", 32, 9, 0, 8, 10, 8, 7, 0),
    "Lex":      Stats("Lex", "Bases", 33, 10, 0, 10, 11, 8, 9, 0),
    "Azel":     Stats("Azel", "Bases", 30, 0, 10, 7, 9, 2, 2, 6),
    "Midir":    Stats("Midir", "Bases", 32, 9, 0, 7, 9, 3, 7, 0),
    "Adeen":    Stats("Adeen", "Bases", 28, 0, 13, 8, 9, 11, 1, 10),
    "Dew":      Stats("Dew", "Bases", 28, 3, 0, 6, 15, 12, 1, 0),
    "Ayra":     Stats("Ayra", "Bases", 32, 11, 0, 16, 17, 3, 7, 1),
    "Deirdre":  Stats("Deirdre", "Bases", 26, 0, 14, 9, 12, 6, 3, 16),
    "Jamke":    Stats("Jamke", "Bases", 36, 11, 0, 14, 14, 4, 9, 0),
    "Holyn":    Stats("Holyn", "Bases", 40, 14, 0, 17, 17, 1, 11, 1),
    "Lachesis": Stats("Lachesis", "Bases", 26, 6, 8, 9, 13, 5, 7, 9),
    "Lewyn":    Stats("Lewyn", "Bases", 34, 1, 12, 12, 16, 7, 5, 9),
    "Sylvia":   Stats("Sylvia", "Bases", 28, 3, 0, 4, 12, 6, 1, 5),
    "Erinys":   Stats("Erinys", "Bases", 32, 11, 1, 12, 18, 7, 9, 9),
    "Beowolf":  Stats("Beowolf", "Bases", 38, 14, 0, 11, 11, 3, 10, 0),
    "Briggid":  Stats("Briggid", "Bases", 40, 20, 0, 22, 21, 7, 14, 9),
    "Claude":   Stats("Claude", "Bases", 34, 0, 21, 14, 15, 9, 5, 20),
    "Tiltyu":   Stats("Tiltyu", "Bases", 28, 0, 10, 15, 10, 9, 1, 9)
}

max_stats = {
    "Junior Lord":      Stats("Max", "Class", 80, 20, 15, 20, 20, 30, 20, 15),
    "Lord Knight":      Stats("Max", "Class", 80, 25, 15, 22, 22, 30, 22, 18),
    "Sword Armour":     Stats("Max", "Class", 80, 24, 15, 20, 18, 30, 25, 15),
    "General":          Stats("Max", "Class", 80, 25, 15, 21, 20, 30, 27, 18),
    "Troubadour":       Stats("Max", "Class", 80, 18, 18, 21, 21, 30, 18, 18),
    "Cavalier":         Stats("Max", "Class", 80, 22, 15, 21, 21, 30, 21, 15),
    "Paladin":          Stats("Max", "Class", 80, 24, 20, 24, 24, 30, 24, 20),
    "Duke Knight":      Stats("Max", "Class", 80, 27, 15, 22, 22, 30, 23, 18),
    "Bow Knight":       Stats("Max", "Class", 80, 25, 15, 23, 23, 30, 23, 18),
    "Great Knight":     Stats("Max", "Class", 80, 27, 15, 22, 22, 30, 25, 18),
    "Forrest Knight":   Stats("Max", "Class", 80, 23, 15, 30, 27, 30, 23, 18),
    "Mage":             Stats("Max", "Class", 80, 15, 22, 21, 21, 30, 16, 20),
    "Mage Knight":      Stats("Max", "Class", 80, 20, 25, 22, 22, 30, 20, 22),
    "Priest":           Stats("Max", "Class", 80, 15, 22, 21, 21, 30, 16, 22),
    "High Priest":      Stats("Max", "Class", 80, 15, 27, 24, 23, 30, 18, 23),
    "Thief":            Stats("Max", "Class", 80, 18, 15, 18, 22, 30, 16, 15),
    "Thief Fighter":    Stats("Max", "Class", 80, 22, 18, 22, 27, 30, 20, 18),
    "Swordfighter":     Stats("Max", "Class", 80, 22, 15, 25, 25, 30, 20, 15),
    "Swordmaster":      Stats("Max", "Class", 80, 27, 15, 30, 30, 30, 22, 18),
    "Forrest":          Stats("Max", "Class", 80, 27, 18, 27, 27, 30, 22, 18),
    "Shaman":           Stats("Max", "Class", 80, 15, 23, 22, 22, 30, 18, 25),
    "Bow Fighter":      Stats("Max", "Class", 80, 22, 15, 25, 25, 30, 20, 15),
    "Sniper":           Stats("Max", "Class", 80, 27, 15, 27, 27, 30, 22, 18),
    "Prince":           Stats("Max", "Class", 80, 23, 18, 22, 21, 30, 22, 18),
    "Princess":         Stats("Max", "Class", 80, 20, 22, 20, 23, 30, 20, 22),
    "Master Knight":    Stats("Max", "Class", 80, 27, 22, 27, 27, 30, 27, 22),
    "Bard":             Stats("Max", "Class", 80, 15, 22, 22, 25, 30, 18, 22),
    "Sage":             Stats("Max", "Class", 80, 15, 30, 27, 30, 30, 18, 27),
    "Dancer":           Stats("Max", "Class", 80, 18, 15, 16, 22, 30, 16, 18),
    "Pegasus Knight":   Stats("Max", "Class", 80, 22, 15, 22, 27, 30, 20, 22),
    "Falcon Knight":    Stats("Max", "Class", 80, 22, 22, 25, 30, 30, 21, 27),
    "Thunder Mage":     Stats("Max", "Class", 80, 15, 22, 24, 21, 30, 16, 20),
    "Mage Fighter (F)": Stats("Max", "Class", 80, 18, 27, 24, 27, 30, 20, 25),
    "Dragon Knight":    Stats("Max", "Class", 80, 25, 15, 22, 21, 30, 26, 15)
}

# Note: Character classes stored in as tuple (unpromoted, promoted)
#       If promotion unavailable, or unit comes pre-promoted, both will be the same for simplicity
unit_classes = {
    "Sigurd":   ("Lord Knight", "Lord Knight"),
    "Noish":    ("Cavalier", "Paladin"),
    "Alec":     ("Cavalier", "Paladin"),
    "Arden":    ("Sword Armour", "General"),
    "Quan":     ("Duke Knight", "Duke Knight"),
    "Ethlin":   ("Troubadour", "Paladin"),
    "Finn":     ("Cavalier", "Duke Knight"),
    "Lex":      ("Cavalier", "Great Knight"),
    "Azel":     ("Mage", "Mage Knight"),
    "Midir":    ("Cavalier", "Bow Knight"),
    "Adeen":    ("Priest", "High Priest"),
    "Dew":      ("Thief", "Thief Fighter"),
    "Ayra":     ("Swordfighter", "Swordmaster"),
    "Deirdre":  ("Shaman", "Shaman"),
    "Jamke":    ("Bow Fighter", "Sniper"),
    "Holyn":    ("Swordfighter", "Forrest"),
    "Lachesis": ("Princess", "Master Knight"),
    "Lewyn":    ("Bard", "Sage"),
    "Sylvia":   ("Dancer", "Dancer"),
    "Erinys":  ("Pegasus Knight", "Falcon Knight"),
    "Beowolf":  ("Cavalier", "Forrest Knight"),
    "Briggid":  ("Sniper", "Sniper"),
    "Claude":   ("High Priest", "High Priest"),
    "Tiltyu":   ("Thunder Mage", "Mage Fighter (F)"),

    "Seliph":   ("Junior Lord", "Lord Knight"),
    "Lana":     ("Priest", "High Priest"),
    "Lester":   ("Cavalier", "Bow Knight"),
    "Ulster":   ("Swordfighter", "Forrest"),
    "Larcei":   ("Swordfighter", "Swordmaster"),
    "Dermott":  ("Cavalier", "Forrest Knight"),
    "Nanna":    ("Troubadour", "Paladin (F)"),
    "Ced":      ("Sage", "Sage"),
    "Fee":      ("Pegasus Knight", "Falcon Knight"),
    "Leif":     ("Prince", "Master Knight"),
    "Altenna":  ("Dragon Knight", "Dragon Knight"),
    "Patty":    ("Thief", "Thief Fighter"),
    "Faval":    ("Bow Fighter", "Sniper"),
    "Corpul":   ("Priest", "High Priest"),
    "Leen":     ("Dancer", "Dancer"),
    "Arthur":   ("Mage", "Mage Knight"),
    "Tinny":    ("Mage", "Mage Fighter (F)")
}

# Mothers who reverse the main parent/secondary parent roles in calculations
main_mothers = [
    "Ethlin",
    "Briggid"
]

# Units who come promoted, usually below promo level
pre_promotes = [
    "Sigurd",
    "Quan",
    "Deirdre",          # Technically not a pre-promote, but can't promote
    "Briggid",
    "Claude",
    "Oifey",
    "Shanan",
    "Hawk",
    "Hannibal",
    "Ced"
]

children = {
    "Deirdre":  ["Seliph", ""],
    "Ethlin":   ["Leif", "Altenna"],
    "Adeen":    ["Lester", "Lana"],
    "Ayra":     ["Ulster", "Larcei"],
    "Lachesis": ["Dermott", "Nanna"],
    "Sylvia":   ["Corpul", "Leen"],
    "Erinys":   ["Ced", "Fee"],
    "Briggid":  ["Faval", "Patty"],
    "Tiltyu":   ["Arthur", "Tinny"]
}

starting_levels = {
    # Gen 1
    "Sigurd":   5,
    "Noish":    3,
    "Alec":     2,
    "Arden":    3,
    "Quan":     4,
    "Ethlyn":   1,
    "Finn":     1,
    "Lex":      4,
    "Azel":     1,
    "Midir":    2,
    "Adeen":    3,
    "Dew":      1,
    "Ayra":     4,
    "Deirdre":  3,
    "Jamke":    6,
    "Holyn":    12,
    "Lachesis": 2,
    "Lewyn":    6,
    "Sylvia":   1,
    "Erinys":   6,
    "Beowolf":  9,
    "Briggid":  12,
    "Claude":   20,
    "Tiltyu":   3,
    # Gen 2
    "Seliph":   1,
    "Lana":     1,
    "Lester":   1,
    "Ulster":   1,
    "Larcei":   1,
    "Dermott":  3,
    "Nanna":    3,
    "Ced":      14,
    "Fee":      2,
    "Leif":     1,
    "Altenna":  17,
    "Patty":    1,
    "Faval":    9,
    "Corpul":   1,
    "Leen":     3,
    "Arthur":   2,
    "Tinny":    3
}

parent_growths = {
    "Sigurd": Stats("", "Growths",1.1,0.5,0.05,0.3,0.3,0.4,0.4,0.05),
    "Noish": Stats("", "Growths",0.8,0.4,0.05,0.3,0.2,0.2,0.4,0.05),
    "Alec": Stats("", "Growths",0.7,0.3,0.05,0.4,0.3,0.3,0.3, 0.05),
    "Arden": Stats("", "Growths",0.9,0.5,0.05,0.1,0.2,0.1,0.4,0.05),
    "Quan": Stats("", "Growths",1.1,0.5,0.05,0.3,0.4,0.1,0.5,0.05),
    "Ethlin": Stats("", "Growths",0.6,0.3,0.05,0.3,0.3,0.2,0.2,0.1),
    "Finn": Stats("", "Growths",0.7,0.3,0.05,0.4,0.3,0.5,0.3,0.05),
    "Lex": Stats("", "Growths",0.9,0.4,0.05,0.2,0.2,0.2,0.5,0.05),
    "Azel": Stats("", "Growths",0.7,0.1,0.4,0.2,0.5,0.2,0.2,0.1),
    "Midir": Stats("", "Growths",0.6,0.3,0.05,0.3,0.4,0.1,0.3,0.05),
    "Adeen": Stats("", "Growths",0.7,0.2,0.3,0.2,0.3,0.6,0.2,0.05),
    "Dew": Stats("", "Growths",0.5,0.4,0.1,0.4,0.4,0.4,0.4,0.1),
    "Ayra": Stats("", "Growths",0.7,0.3,0.05,0.6,0.3,0.2,0.2,0.05),
    "Deirdre": Stats("", "Growths",0.7,0.1,0.7,0.2,0.1,0.1,0.1,0.7),
    "Jamke": Stats("", "Growths",0.9,0.5,0,0.1,0.3,0.4,0.3,0.05),
    "Holyn": Stats("", "Growths",1.1,0.3,0.05,0.8,0.3,0.2,0.3,0.05),
    "Lachesis": Stats("", "Growths",0.6,0.5,0.05,0.1,0.2,0.4,0.2,0.1),
    "Lewyn": Stats("", "Growths",0.9,0.1,0.3,0.4,0.9,0.2,0.2,0.1),
    "Sylvia": Stats("", "Growths",0.5,0.1,0.3,0.1,0.1,0.3,0.1,0.4),
    "Erinys": Stats("", "Growths",0.5,0.2,0.1,0.2,0.3,0.2,0.3,0.1),
    "Beowolf": Stats("", "Growths",0.8,0.4,0,0.4,0.3,0.2,0.3,0.05),
    "Briggid": Stats("", "Growths",0.9,0.3,0.2,0.3,0.2,0.7,0.2,0.05),
    "Claude": Stats("", "Growths",0.7,0.1,0.4,0.2,0.3,0.5,0.2,0.5),
    "Tiltyu": Stats("", "Growths",0.6,0.1,0.2,0.6,0.4,0.5,0.1,0.1),
}

# Note: Growth Rates for each Father
child_growths = {
    "Seliph":   {
        "Sigurd": Stats("", "Growths", 1.40, 0.55, 0.3, 0.6, 0.35, 0.45, 0.45, 0.30)
        },
    "Lana":     {
        "Arden": Stats("", "Growths", 1.15, 0.45, 0.32, 0.25, 0.40, 0.65, 0.40, 0.07),
        "Azel": Stats("", "Growths", 1.15, 0.25, 0.65, 0.30, 0.55, 0.70, 0.30, 0.10),
        "Alec": Stats("", "Growths", 1.05, 0.35, 0.32, 0.40, 0.45, 0.75, 0.35, 0.07),
        "Claude": Stats("", "Growths", 1.05, 0.25, 0.50, 0.30, 0.45, 0.85, 0.30, 0.30),
        "Jamke": Stats("", "Growths", 1.15, 0.45, 0.30, 0.25, 0.45, 0.80, 0.35, 0.07),
        "Dew": Stats("", "Growths", 0.95, 0.40, 0.35, 0.40, 0.50, 0.80, 0.40, 0.10),
        "Noish": Stats("", "Growths", 1.10, 0.40, 0.32, 0.35, 0.40, 0.70, 0.40, 0.07),
        "Finn": Stats("", "Growths", 105, 0.35, 0.32, 0.40, 0.45, 0.85, 0.35, 0.07),
        "Beowolf": Stats("", "Growths", 1.10, 0.40, 0.30, 0.40, 0.45, 0.70, 0.35, 0.07),
        "Holyn": Stats("", "Growths", 1.35, 0.35, 0.32, 0.75, 0.45, 0.70, 0.35, 0.07),
        "Midir": Stats("", "Growths", 1.00, 0.35, 0.32, 0.35, 0.50, 0.65, 0.35, 0.07),
        "Lewyn": Stats("", "Growths", 1.15, 0.25, 0.45, 0.40, 0.75, 0.70, 0.30, 0.10),
        "Lex": Stats("", "Growths", 1.25, 0.40, 0.32, 0.30, 0.40, 0.70, 0.60, 0.07)
        },
    "Lester":   {
        "Arden": Stats("", "Growths", 1.35, 0.60, 0.20, 0.20, 0.35, 0.55, 0.50, 0.07),
        "Azel": Stats("", "Growths", 1.15, 0.20, 0.55, 0.30, 0.65, 0.65, 0.30, 0.12),
        "Alec": Stats("", "Growths", 1.15, 0.40, 0.20, 0.50, 0.45, 0.75, 0.40, 0.07),
        "Claude": Stats("", "Growths", 1.15, 0.20, 0.55, 0.30, 0.45, 0.95, 0.30, 0.52),
        "Jamke": Stats("", "Growths", 1.35, 0.60, 0.15, 0.20, 0.45, 0.85, 0.40, 0.07),
        "Dew": Stats("", "Growths", 0.95, 0.50, 0.25, 0.50, 0.55, 0.85, 0.50, 0.12),
        "Noish": Stats("", "Growths", 1.25, 0.50, 0.20, 0.40, 0.35, 0.65, 0.50, 0.07),
        "Finn": Stats("", "Growths", 1.15, 0.40, 0.20, 0.50, 0.45, 0.95, 0.40, 0.07),
        "Beowolf": Stats("", "Growths", 1.25, 0.50, 0.15, 0.50, 0.45, 0.65, 0.40, 0.07),
        "Holyn": Stats("", "Growths", 1.55, 0.40, 0.20, 0.90, 0.45, 0.65, 0.40, 0.07),
        "Midir": Stats("", "Growths", 1.05, 0.40, 0.20, 0.40, 0.55, 0.55, 0.40, 0.07),
        "Lewyn": Stats("", "Growths", 1.35, 0.20, 0.45, 0.50, 1.05,0.65, 0.30, 0.12),
        "Lex": Stats("", "Growths", 1.35, 0.50, 0.20, 0.30, 0.35, 0.65, 0.60, 0.07)
        },
    "Ulster":   {
        "Arden": Stats("", "Growths", 1.35, 0.65, 0.07, 0.55, 0.35, 0.20, 0.50, 0.7),
        "Azel": Stats("", "Growths", 1.15, 0.25, 0.42, 0.65, 0.65, 0.30, 0.30, 0.12),
        "Alec": Stats("", "Growths", 1.15, 0.45, 0.07, 0.85, 0.45, 0.40, 0.40, 0.7),
        "Claude": Stats("", "Growths", 1.15, 0.25, 0.42, 0.65, 0.45, 0.60, 0.30, 0.52),
        "Jamke": Stats("", "Growths", 1.35, 0.65, 0.02, 0.55, 0.45, 0.50, 0.40, 0.07),
        "Dew": Stats("", "Growths", 0.95, 0.55, 0.12, 0.85, 0.55, 0.50, 0.50, 0.01),
        "Noish": Stats("", "Growths", 1.25, 0.55, 0.07, 0.75, 0.35, 0.30, 0.50, 0.07),
        "Finn": Stats("", "Growths", 1.15, 0.45, 0.07, 0.85, 0.45, 0.60, 0.40, 0.7),
        "Beowolf": Stats("", "Growths", 1.25, 0.55, 0.02, 0.85, 0.45, 0.30, 0.40, 0.07),
        "Holyn": Stats("", "Growths", 1.55, 0.45, 0.07, 1.25, 0.45, 0.30, 0.40, 0.07),
        "Midir": Stats("", "Growths", 1.05, 0.45, 0.07, 0.75, 0.55, 0.20, 0.40, 0.07),
        "Lewyn": Stats("", "Growths", 1.35, 0.25, 0.32, 0.85, 1.05, 0.30, 0.30, 0.12),
        "Lex": Stats("", "Growths", 1.35, 0.55, 0.07, 0.65, 0.35, 0.30, 0.60, 0.07)
        },
    "Larcei":   {
        "Arden": Stats("", "Growths", 1.15, 0.55, 0.07, 0.65, 0.40, 0.25, 0.40, 0.07),
        "Azel": Stats("", "Growths", 1.15, 0.35, 0.40, 0.70, 0.55, 0.30, 0.30, 0.10),
        "Alec": Stats("", "Growths", 1.05, 0.45, 0.07, 0.80, 0.45, 0.35, 0.35, 0.07),
        "Claude": Stats("", "Growths", 1.05, 0.35, 0.25, 0.70, 0.45, 0.45, 0.30, 0.30),
        "Jamke": Stats("", "Growths", 1.15, 0.55, 0.05, 0.65, 0.45, 0.40, 0.35, 0.07),
        "Dew": Stats("", "Growths", 0.95, 0.50, 0.10, 0.80, 0.50, 0.40, 0.40, 0.10),
        "Noish": Stats("", "Growths", 1.10, 0.50, 0.07, 0.75, 0.40, 0.30, 0.40, 0.07),
        "Finn": Stats("", "Growths", 1.05, 0.45, 0.07, 0.80, 0.45, 0.45, 0.35, 0.07),
        "Beowolf": Stats("", "Growths", 1.10, 0.50, 0.05, 0.80, 0.45, 0.30, 0.35, 0.07),
        "Holyn": Stats("", "Growths", 1.35, 0.45, 0.07, 1.15, 0.45, 0.30, 0.35, 0.07),
        "Midir": Stats("", "Growths", 1.00, 0.45, 0.07, 0.75, 0.50, 0.25, 0.35, 0.07),
        "Lewyn": Stats("", "Growths", 1.15, 0.35, 0.20, 0.80, 0.75, 0.30, 0.30, 0.010),
        "Lex": Stats("", "Growths", 1.25, 0.50, 0.07, 0.70, 0.40, 0.30, 0.60, 0.07)
        },
    "Dermott":  {
        "Arden": Stats("", "Growths", 1.30, 0.90, 0.07, 0.15, 0.30, 0.30, 0.50, 0.10),
        "Azel": Stats("", "Growths", 1.10, 0.50, 0.42, 0.25, 0.60, 0.40, 0.30, 0.15),
        "Alec": Stats("", "Growths", 1.10, 0.70, 0.07, 0.45, 0.40, 0.50, 0.40, 0.10),
        "Claude": Stats("", "Growths", 1.10, 0.50, 0.42, 0.25, 0.40, 0.70, 0.30, 0.55),
        "Jamke": Stats("", "Growths", 1.30, 0.90, 0.02, 0.15, 0.40, 0.60, 0.40, 0.10),
        "Dew": Stats("", "Growths", 0.90, 0.80, 0.12, 0.45, 0.50, 0.60, 0.50, 0.15),
        "Noish": Stats("", "Growths", 1.20, 0.80, 0.07, 0.35, 0.30, 0.40, 0.50, 0.10),
        "Finn": Stats("", "Growths", 1.10, 0.70, 0.07, 0.45, 0.40, 0.70, 0.40, 0.10),
        "Beowolf": Stats("", "Growths", 1.20, 0.80, 0.02, 0.45, 0.40, 0.40, 0.40, 0.10),
        "Holyn": Stats("", "Growths", 1.50, 0.70, 0.07, 0.85, 0.40, 0.40, 0.40, 0.10),
        "Midir": Stats("", "Growths", 1.00, 0.70, 0.07, 0.35, 0.50, 0.30, 0.40, 0.10),
        "Lewyn": Stats("", "Growths", 1.30, 0.50, 0.32, 0.45, 1.00, 0.40, 0.30, 0.10),
        "Lex": Stats("", "Growths", 1.30, 0.80, 0.07, 0.25, 0.30, 0.40, 0.60, 0.10)
        },
    "Nanna":    {
        "Arden": Stats("", "Growths", 1.05, 0.75, 0.07, 0.15, 0.30, 0.45, 0.40, 0.12),
        "Azel": Stats("", "Growths", 1.05, 0.55, 0.40, 0.20, 0.45, 0.50, 0.30, 0.15),
        "Alec": Stats("", "Growths", 0.95, 0.65, 0.07, 0.30, 0.35, 0.55, 0.35, 0.12),
        "Claude": Stats("", "Growths", 0.95, 0.55, 0.25, 0.20, 0.35, 0.65, 0.30, 0.35),
        "Jamke": Stats("", "Growths", 1.05, 0.75, 0.05, 0.15, 0.35, 0.60, 0.35, 0.12),
        "Dew": Stats("", "Growths", 0.85, 0.70, 0.10, 0.30, 0.40, 0.60, 0.40, 0.15),
        "Noish": Stats("", "Growths", 1.00, 0.70, 0.07, 0.25, 0.30, 0.50, 0.40, 0.12),
        "Finn": Stats("", "Growths", 0.95, 0.65, 0.07, 0.30, 0.35, 0.65, 0.35, 0.12),
        "Beowolf": Stats("", "Growths", 1.00, 0.70, 0.05, 0.30, 0.35, 0.50, 0.35, 0.12),
        "Holyn": Stats("", "Growths", 1.25, 0.65, 0.07, 0.65, 0.35, 0.50, 0.35, 0.12),
        "Midir": Stats("", "Growths", 0.90, 0.65, 0.07, 0.25, 0.40, 0.45, 0.35, 0.12),
        "Lewyn": Stats("", "Growths", 1.05, 0.55, 0.20, 0.30, 0.65, 0.50, 0.30, 0.15),
        "Lex": Stats("", "Growths", 1.15, 0.70, 0.07, 0.20, 0.30, 0.50, 0.60, 0.12)
        },
    "Ced":      {
        "Arden": Stats("", "Growths", 1.15, 0.60, 0.10, 0.20, 0.35, 0.20, 0.55, 0.10),
        "Azel": Stats("", "Growths", 0.95, 0.20, 0.45, 0.30, 0.65, 0.30, 0.35, 0.15),
        "Alec": Stats("", "Growths", 0.95, 0.40, 0.10, 0.50, 0.45, 0.40, 0.45, 0.10),
        "Claude": Stats("", "Growths", 0.95, 0.20, 0.45, 0.30, 0.45, 0.60, 0.35, 0.55),
        "Jamke": Stats("", "Growths", 1.15, 0.60, 0.05, 0.20, 0.45, 0.50, 0.45, 0.10),
        "Dew": Stats("", "Growths", 0.75, 0.50, 0.15, 0.50, 0.55, 0.50, 0.55, 0.15),
        "Noish": Stats("", "Growths", 1.05, 0.50, 0.10, 0.40, 0.35, 0.30, 0.55, 0.10),
        "Finn": Stats("", "Growths", 0.95, 0.40, 0.10, 0.50, 0.45, 0.60, 0.45, 0.10),
        "Beowolf": Stats("", "Growths", 1.05, 0.50, 0.05, 0.50, 0.45, 0.30, 0.45, 0.10),
        "Holyn": Stats("", "Growths", 1.35, 0.40, 0.10, 0.90, 0.45, 0.30, 0.45, 0.10),
        "Midir": Stats("", "Growths", 0.85, 0.40, 0.10, 0.40, 0.55, 0.20, 0.45, 0.10),
        "Lewyn": Stats("", "Growths", 1.15, 0.20, 0.35, 0.50, 1.05, 0.30, 0.35, 0.15),
        "Lex": Stats("", "Growths", 1.15, 0.50, 0.10, 0.30, 0.35, 0.30, 0.65, 0.10)
        },
    "Fee":      {
        "Arden": Stats("", "Growths", 0.95, 0.45, 0.12, 0.25, 0.40, 0.25, 0.50, 0.12),
        "Azel": Stats("", "Growths", 0.95, 0.25, 0.45, 0.30, 0.55, 0.30, 0.40, 0.15),
        "Alec": Stats("", "Growths", 0.85, 0.35, 0.12, 0.40, 0.45, 0.35, 0.45, 0.12),
        "Claude": Stats("", "Growths", 0.85, 0.25, 0.30, 0.30, 0.45, 0.45, 0.40, 0.35),
        "Jamke": Stats("", "Growths", 0.95, 0.45, 0.10, 0.25, 0.45, 0.40, 0.45, 0.12),
        "Dew": Stats("", "Growths", 0.75, 0.40, 0.15, 0.40, 0.50, 0.40, 0.50, 0.15),
        "Noish": Stats("", "Growths", 0.90, 0.40, 0.12, 0.35, 0.40, 0.30, 0.50, 0.12),
        "Finn": Stats("", "Growths", 0.85, 0.35, 0.12, 0.40, 0.45, 0.45, 0.45, 0.12),
        "Beowolf": Stats("", "Growths", 0.90, 0.40, 0.10, 0.40, 0.45, 0.30, 0.45, 0.12),
        "Holyn": Stats("", "Growths", 1.15, 0.35, 0.12, 0.75, 0.45, 0.30, 0.45, 0.12),
        "Midir": Stats("", "Growths", 0.80, 0.35, 0.12, 0.35, 0.50, 0.25, 0.45, 0.12),
        "Lewyn": Stats("", "Growths", 0.95, 0.25, 0.25, 0.40, 0.75, 0.30, 0.40, 0.15),
        "Lex": Stats("", "Growths", 1.05, 0.40, 0.12, 0.30, 0.40, 0.30, 0.70, 0.12)
        },
    "Leif":     {
        "Quan": Stats("", "Growths", 1.30, 0.60, 0.07, 0.50, 0.45, 0.25, 0.50, 0.10)
        },
    "Altenna":  {
        "Quan": Stats("", "Growths", 1.35, 0.65, 0.07, 0.45, 0.60, 0.25, 0.55, 0.12)
        },
    "Patty":    {
        "Arden": Stats("", "Growths", 1.15, 0.55, 0.22, 0.35, 0.30, 0.45, 0.40, 0.07),
        "Azel": Stats("", "Growths", 1.15, 0.35, 0.55, 0.40, 0.45, 0.50, 0.30, 0.10),
        "Alec": Stats("", "Growths", 1.05, 0.45, 0.22, 0.50, 0.35, 0.55, 0.35, 0.07),
        "Claude": Stats("", "Growths", 1.15, 0.35, 0.50, 0.40, 0.35, 0.75, 0.30, 0.50),
        "Jamke": Stats("", "Growths", 1.15, 0.55, 0.20, 0.35, 0.35, 0.60, 0.35, 0.07),
        "Dew": Stats("", "Growths", 0.95, 0.50, 0.25, 0.50, 0.40, 0.60, 0.40, 0.10),
        "Noish": Stats("", "Growths", 1.10, 0.50, 0.22, 0.45, 0.30, 0.50, 0.40, 0.07),
        "Finn": Stats("", "Growths", 1.05, 0.45, 0.22, 0.50, 0.35, 0.65, 0.35, 0.07),
        "Beowolf": Stats("", "Growths", 1.10, 0.50, 0.20, 0.50, 0.35, 0.50, 0.35, 0.07),
        "Holyn": Stats("", "Growths", 1.35, 0.45, 0.22, 0.85, 0.35, 0.50, 0.35, 0.07),
        "Midir": Stats("", "Growths", 1.00, 0.45, 0.22, 0.45, 0.40, 0.45, 0.35, 0.07),
        "Lewyn": Stats("", "Growths", 1.35, 0.35, 0.35, 0.50, 0.95, 0.50, 0.30, 0.10),
        "Lex": Stats("", "Growths", 1.25, 0.50, 0.22, 0.40, 0.30, 0.50, 0.60, 0.07)
        },
    "Faval":    {
        "Arden": Stats("", "Growths", 1.55, 0.65, 0.15, 0.25, 0.30, 0.75, 0.50, 0.07),
        "Azel": Stats("", "Growths", 1.35, 0.25, 0.50, 0.35, 0.60, 0.85, 0.30, 0.12),
        "Alec": Stats("", "Growths", 1.35, 0.45, 0.15, 0.55, 0.40, 0.95, 0.40, 0.07),
        "Claude": Stats("", "Growths", 1.25, 0.25, 0.40, 0.35, 0.40, 1.05, 0.30, 0.32),
        "Jamke": Stats("", "Growths", 1.55, 0.65, 0.10, 0.25, 0.40, 0.105, 0.40, 0.07),
        "Dew": Stats("", "Growths", 1.15, 0.55, 0.20, 0.55, 0.50, 1.05, 0.50, 0.12),
        "Noish": Stats("", "Growths", 1.45, 0.55, 0.15, 0.45, 0.30, 0.85, 0.50, 0.07),
        "Finn": Stats("", "Growths", 1.35, 0.45, 0.15, 0.55, 0.40, 1.15, 0.40, 0.07),
        "Beowolf": Stats("", "Growths", 1.45, 0.55, 0.10, 0.55, 0.40, 0.85, 0.40, 0.07),
        "Holyn": Stats("", "Growths", 1.75, 0.45, 0.15, 0.95, 0.40, 0.85, 0.40, 0.07),
        "Midir": Stats("", "Growths", 1.25, 0.45, 0.15, 0.45, 0.50, 0.75, 0.40, 0.07),
        "Lewyn": Stats("", "Growths", 1.35, 0.25, 0.40, 0.55, 0.70, 0.85, 0.30, 0.12),
        "Lex": Stats("", "Growths", 1.55, 0.55, 0.15, 0.35, 0.30, 0.85, 0.60, 0.07)
        },
    "Corpul":   {
        "Arden": Stats("", "Growths", 1.20, 0.55, 0.25, 0.15, 0.25, 0.30, 0.45, 0.35),
        "Azel": Stats("", "Growths", 1.00, 0.15, 0.60, 0.25, 0.55, 0.40, 0.25, 0.40),
        "Alec": Stats("", "Growths", 1.00, 0.35, 0.25, 0.45, 0.35, 0.50, 0.35, 0.35),
        "Claude": Stats("", "Growths", 0.90, 0.15, 0.50, 0.25, 0.35, 0.60, 0.25, 0.60),
        "Jamke": Stats("", "Growths", 1.20, 0.55, 0.20, 0.15, 0.35, 0.60, 0.35, 0.35),
        "Dew": Stats("", "Growths", 0.80, 0.45, 0.30, 0.45, 0.45, 0.60, 0.45, 0.40),
        "Noish": Stats("", "Growths", 1.10, 0.45, 0.25, 0.35, 0.25, 0.40, 0.45, 0.35),
        "Finn": Stats("", "Growths", 1.00, 0.35, 0.25, 0.45, 0.35, 0.70, 0.35, 0.35),
        "Beowolf": Stats("", "Growths", 1.10, 0.45, 0.20, 0.45, 0.35, 0.40, 0.35, 0.35),
        "Holyn": Stats("", "Growths", 1.40, 0.35, 0.25, 0.85, 0.35, 0.40, 0.35, 0.35),
        "Midir": Stats("", "Growths", 0.90, 0.35, 0.25, 0.35, 0.45, 0.30, 0.35, 0.35),
        "Lewyn": Stats("", "Growths", 1.20, 0.15, 0.50, 0.45, 0.95, 0.40, 0.25, 0.40),
        "Lex": Stats("", "Growths", 1.20, 0.45, 0.25, 0.25, 0.25, 0.40, 0.55, 0.35)
        },
    "Leen":     {
        "Arden": Stats("", "Growths", 0.95, 0.35, 0.32, 0.15, 0.20, 0.35, 0.30, 0.42),
        "Azel": Stats("", "Growths", 0.95, 0.15, 0.65, 0.20, 0.35, 0.40, 0.20, 0.45),
        "Alec": Stats("", "Growths", 0.85, 0.25, 0.32, 0.30, 0.25, 0.45, 0.25, 0.42),
        "Claude": Stats("", "Growths", 0.85, 0.15, 0.50, 0.20, 0.25, 0.55, 0.20, 0.65),
        "Jamke": Stats("", "Growths", 0.95, 0.35, 0.30, 0.15, 0.25, 0.50, 0.25, 0.42),
        "Dew": Stats("", "Growths", 0.75, 0.30, 0.35, 0.30, 0.30, 0.50, 0.30, 0.45),
        "Noish": Stats("", "Growths", 0.90, 0.30, 0.32, 0.25, 0.20, 0.40, 0.30, 0.42),
        "Finn": Stats("", "Growths", 0.85, 0.25, 0.32, 0.30, 0.25, 0.55, 0.25, 0.42),
        "Beowolf": Stats("", "Growths", 0.90, 0.30, 0.30, 0.30, 0.25, 0.40, 0.25, 0.42),
        "Holyn": Stats("", "Growths", 1.15, 0.25, 0.32, 0.65, 0.25, 0.40, 0.25, 0.42),
        "Midir": Stats("", "Growths", 0.80, 0.25, 0.32, 0.25, 0.30, 0.35, 0.25, 0.42),
        "Lewyn": Stats("", "Growths", 0.95, 0.15, 0.45, 0.30, 0.55, 0.40, 0.20, 0.45),
        "Lex": Stats("", "Growths", 1.05, 0.30, 0.32, 0.20, 0.20, 0.40, 0.50, 0.42)
        },
    "Arthur":   {
        "Arden": Stats("", "Growths", 1.30, 0.55, 0.15, 0.55, 0.40, 0.35, 0.45, 0.10),
        "Azel": Stats("", "Growths", 1.10, 0.15, 0.50, 0.65, 0.70, 0.45, 0.25, 0.15),
        "Alec": Stats("", "Growths", 1.10, 0.35, 0.15, 0.85, 0.50, 0.55, 0.35, 0.10),
        "Claude": Stats("", "Growths", 1.10, 0.15, 0.50, 0.65, 0.50, 0.75, 0.25, 0.55),
        "Jamke": Stats("", "Growths", 1.30, 0.55, 0.10, 0.55, 0.50, 0.65, 0.35, 0.10),
        "Dew": Stats("", "Growths", 0.90, 0.45, 0.20, 0.85, 0.60, 0.65, 0.45, 0.15),
        "Noish": Stats("", "Growths", 1.20, 0.45, 0.15, 0.75, 0.40, 0.45, 0.45, 0.10),
        "Finn": Stats("", "Growths", 1.10, 0.35, 0.15, 0.85, 0.50, 0.75, 0.35, 0.10),
        "Beowolf": Stats("", "Growths", 1.20, 0.45, 0.10, 0.85, 0.50, 0.45, 0.35, 0.10),
        "Holyn": Stats("", "Growths", 1.50, 0.35, 0.15, 1.25, 0.50, 0.45, 0.35, 0.10),
        "Midir": Stats("", "Growths", 1.00, 0.35, 0.15, 0.75, 0.60, 0.35, 0.35, 0.10),
        "Lewyn": Stats("", "Growths", 1.30, 0.15, 0.40, 0.85, 1.10, 0.45, 0.25, 0.15),
        "Lex": Stats("", "Growths", 1.30, 0.45, 0.15, 0.65, 0.40, 0.45, 0.55, 0.10)
        },
    "Tinny":    {
        "Arden": Stats("", "Growths", 1.05, 0.35, 0.22, 0.65, 0.50, 0.55, 0.30, 0.12),
        "Azel": Stats("", "Growths", 1.05, 0.15, 0.55, 0.70, 0.65, 0.60, 0.20, 0.15),
        "Alec": Stats("", "Growths", 0.95, 0.25, 0.22, 0.80, 0.55, 0.65, 0.25, 0.12),
        "Claude": Stats("", "Growths", 0.95, 0.15, 0.40, 0.70, 0.55, 0.75, 0.20, 0.35),
        "Jamke": Stats("", "Growths", 1.05, 0.35, 0.20, 0.65, 0.55, 0.70, 0.25, 0.12),
        "Dew": Stats("", "Growths", 0.85, 0.30, 0.25, 0.80, 0.60, 0.70, 0.30, 0.15),
        "Noish": Stats("", "Growths", 1.00, 0.30, 0.22, 0.75, 0.50, 0.60, 0.30, 0.12),
        "Finn": Stats("", "Growths", 0.95, 0.25, 0.22, 0.80, 0.55, 0.75, 0.25, 0.12),
        "Beowolf": Stats("", "Growths", 1.00, 0.30, 0.20, 0.80, 0.55, 0.60, 0.25, 0.12),
        "Holyn": Stats("", "Growths", 1.25, 0.25, 0.22, 1.15, 0.55, 0.60, 0.25, 0.12),
        "Midir": Stats("", "Growths", 0.90, 0.25, 0.22, 0.75, 0.60, 0.55, 0.25, 0.12),
        "Lewyn": Stats("", "Growths", 1.05, 0.15, 0.35, 0.80, 0.85, 0.60, 0.20, 0.15),
        "Lex": Stats("", "Growths", 1.15, 0.30, 0.22, 0.70, 0.50, 0.60, 0.50, 0.12)
        },
}