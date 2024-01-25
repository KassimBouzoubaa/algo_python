actions = {
    1: {"cout": 20, "pourcentage": 5},
    2: {"cout": 30, "pourcentage": 10},
    3: {"cout": 50, "pourcentage": 15},
    4: {"cout": 70, "pourcentage": 20},
    5: {"cout": 60, "pourcentage": 17},
    6: {"cout": 80, "pourcentage": 25},
    7: {"cout": 22, "pourcentage": 7},
    8: {"cout": 26, "pourcentage": 11},
    9: {"cout": 48, "pourcentage": 13},
    10: {"cout": 34, "pourcentage": 27},
    11: {"cout": 42, "pourcentage": 17},
    12: {"cout": 110, "pourcentage": 9},
    13: {"cout": 38, "pourcentage": 23},
    14: {"cout": 14, "pourcentage": 1},
    15: {"cout": 18, "pourcentage": 3},
    16: {"cout": 8, "pourcentage": 8},
    17: {"cout": 4, "pourcentage": 12},
    18: {"cout": 10, "pourcentage": 14},
    19: {"cout": 24, "pourcentage": 21},
    20: {"cout": 114, "pourcentage": 18},
}


def force_brute(actions):
    DEPENSE_MAX = 500
    meilleure_combinaison = None
    meilleur_benefice = 0

    for i in range(1, 2 ** len(actions)):
        combinaison_actuelle = [
            actions[k] for k, v in actions.items() if (i >> (k - 1)) & 1
        ]

        cout_total = sum(action["cout"] for action in combinaison_actuelle)
        benefice_total = sum(
            action["cout"] * action["pourcentage"] / 100
            for action in combinaison_actuelle
        )

        if cout_total <= DEPENSE_MAX and benefice_total > meilleur_benefice:
            meilleure_combinaison, meilleur_benefice = (
                combinaison_actuelle,
                benefice_total,
            )

    print(f"2 meilleur combi", meilleure_combinaison)
    print(f"2 meilleur benefice", meilleur_benefice)


def force_brute2(actions):
    depense_max = 500
    meilleure_combinaison = []
    meilleur_benefice = 0

    for key, value in actions.items():
        value["benefice"] = (value["cout"] * value["pourcentage"]) / 100

    actions_triees = dict(
        sorted(actions.items(), key=lambda x: x[1]["benefice"], reverse=True)
    )

    for key, value in actions_triees.items():
        if depense_max - value["cout"] >= 0:
            depense_max -= value["cout"]
            meilleur_benefice += value["benefice"]
            meilleure_combinaison.append(actions_triees[key])

    print(f"meilleur combi", meilleure_combinaison)
    print(f"meilleur benefice", meilleur_benefice)


force_brute(actions)
print("SUITE -----")
force_brute2(actions)
