def dynamic(actions, budget_max):
    # Transformer les clés en entiers
    actions_dict = {i + 1: v for i, (k, v) in enumerate(actions.items())}
    # Convertir le dictionnaire en une liste de tuples pour faciliter le traitement
    actions_list = [(key, value['Cout'], value['Benefice']) for key, value in actions_dict.items()]
    print(actions_list[0])
    # Initialisation de la matrice de programmation dynamique pour stocker les résultats intermédiaires
    dp = [[0] * (budget_max + 1) for _ in range(len(actions_list) + 1)]


    # Remplissage de la matrice
    for i in range(1, len(actions_list) + 1):
        for budget in range(1, budget_max + 1):
            # Vérification si l'action peut être incluse avec le budget disponible
            if actions_list[i - 1][1] <= budget:
                # Choix entre inclure l'action ou non
                dp[i][budget] = max(dp[i - 1][budget],
                                    dp[i - 1][int(budget - actions_list[i - 1][1])] + actions_list[i - 1][2])

            else:
                dp[i][budget] = dp[i - 1][budget]

    # Récupération de la meilleure combinaison d'actions
    combinaison = []
    i = len(actions_list)
    budget = budget_max
    while i > 0 and budget > 0:
        if dp[i][int(budget)] != dp[i - 1][int(budget)]:
            combinaison.append(actions_list[i - 1])
            budget -= actions_list[i - 1][1]
        i -= 1
        # Calcul de la somme des bénéfices et des coûts
    somme_benefices = sum(action[2] for action in combinaison)
    somme_couts = sum(action[1] for action in combinaison)

    return combinaison, somme_benefices, somme_couts