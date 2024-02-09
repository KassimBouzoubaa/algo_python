import csv

actions = {
    1: {"cout": 20, "profit": 5},
    2: {"cout": 30, "profit": 10},
    3: {"cout": 50, "profit": 15},
    4: {"cout": 70, "profit": 20},
    5: {"cout": 60, "profit": 17},
    6: {"cout": 80, "profit": 25},
    7: {"cout": 22, "profit": 7},
    8: {"cout": 26, "profit": 11},
    9: {"cout": 48, "profit": 13},
    10: {"cout": 34, "profit": 27},
    11: {"cout": 42, "profit": 17},
    12: {"cout": 110, "profit": 9},
    13: {"cout": 38, "profit": 23},
    14: {"cout": 14, "profit": 1},
    15: {"cout": 18, "profit": 3},
    16: {"cout": 8, "profit": 8},
    17: {"cout": 4, "profit": 12},
    18: {"cout": 10, "profit": 14},
    19: {"cout": 24, "profit": 21},
    20: {"cout": 114, "profit": 18},
}


def charger_donnees_csv(nom_fichier):
    actions = {}

    try:
        with open(nom_fichier, mode="r") as fichier_csv:
            lecteur = csv.reader(fichier_csv)

            # Ignorer l'en-tête
            en_tete = next(lecteur, None)

            for ligne in lecteur:
                id, cout, benefice = ligne
                actions[id] = {
                    "Cout": float(cout),
                    "Benefice": float(benefice),
                }

        print(f"Données chargées depuis {nom_fichier}.")
        return actions

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None
