from itertools import combinations, chain


def force_brute(actions, depense):
    meilleure_combinaison = None
    meilleur_profit = 0

    # Générer toutes les combinaisons possibles d'actions
    toutes_combinaisons = chain.from_iterable(
        combinations(actions.items(), r) for r in range(1, len(actions) + 1)
    )

    for combinaison_actuelle in toutes_combinaisons:
        cout_total = sum(action["cout"] for _, action in combinaison_actuelle)
        profit_total = sum(
            action["cout"] * (1 + action["benefice"] / 100)
            for _, action in combinaison_actuelle
        )

        if cout_total <= depense and profit_total > meilleur_profit:
            meilleure_combinaison, meilleur_profit = combinaison_actuelle, profit_total

        ids_meilleure_combinaison = [id for id, _ in meilleure_combinaison]

    return ids_meilleure_combinaison, meilleur_profit
