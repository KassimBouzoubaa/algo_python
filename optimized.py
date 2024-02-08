def dynamic(actions, depense):
    # Création de listes pour stocker les coûts et les profits
    couts = [action["cout"] for action in actions.values()]

    profits = [
        action["cout"] * (1 + action["benefice"] / 100) for action in actions.values()
    ]

    n = len(actions)
    W = depense

    # Initialisation de la table T avec des zéros
    portefeuilles = [[0] * (W + 1) for _ in range(n + 1)]
    # comprehension de liste
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Remplissage de la table avec la programmation dynamique
    for nombre_action in range(1, n + 1):
        for depense_max in range(W + 1):
            if couts[nombre_action - 1] <= depense_max:
                valeur_portefeuille_precedent = portefeuilles[nombre_action - 1][
                    depense_max
                ]
                valeur_portefeuille_cout_deduit = portefeuilles[nombre_action - 1][
                    depense_max - couts[nombre_action - 1]
                ]
                profit_derniere_action = profits[nombre_action - 1]
                portefeuilles[nombre_action][depense_max] = max(
                    valeur_portefeuille_precedent,
                    valeur_portefeuille_cout_deduit + profit_derniere_action,
                )
            else:
                portefeuilles[nombre_action][depense_max] = portefeuilles[
                    nombre_action - 1
                ][depense_max]

    # Reconstruction de la meilleure combinaison
    i, j = n, W
    action_ids = []
    while i > 0 and j > 0:
        if portefeuilles[i][j] != portefeuilles[i - 1][j]:
            action_ids.append(i)
            j -= couts[i - 1]
        i -= 1

    # Inversion de l'ordre de la combinaison
    action_ids.reverse()

    return action_ids, portefeuilles[n][W]
