def dynamic(actions, budget_max):
    """
    Résout le problème de maximisation de bénéfice en utilisant la programmation dynamique.

    Args:
        actions (dict): Dictionnaire d'actions avec leurs coûts et bénéfices.
        budget_max (int): Le budget maximum pour le sac à dos.

     Returns:
        list: Une combinaison d'actions optimale.
        float: La somme des bénéfices.
        float: La somme des coûts.
    """

    # Transformer les clés en entiers pour faciliter le traitement
    actions_dict = {i + 1: v for i, (k, v) in enumerate(actions.items())}

    # Convertir le dictionnaire en une liste de tuples
    actions_list = [
        (key, value["Cout"], value["Profit"]) for key, value in actions_dict.items()
    ]

    # Initialisation de la matrice de programmation dynamique
    dp = [[0] * (budget_max + 1) for _ in range(len(actions_list) + 1)]

    # Remplissage de la matrice
    for i in range(1, len(actions_list) + 1):
        for budget in range(1, budget_max + 1):
            # Vérification si l'action peut être incluse avec le budget disponible
            if actions_list[i - 1][1] <= budget:
                # Choix entre inclure l'action ou non
                dp[i][budget] = max(
                    dp[i - 1][budget],
                    dp[i - 1][int(budget - actions_list[i - 1][1])]
                    + actions_list[i - 1][2],
                )
            else:
                dp[i][budget] = dp[i - 1][budget]

    # Récupération de la meilleure combinaison d'actions
    combinaison = []
    i = len(actions_list)
    budget = budget_max
    while i > 0 and budget > 0:
        if dp[i][int(budget)] != dp[i - 1][int(budget)]:
            # Ajouter le nom de l'action à partir des clés du dictionnaire d'entrée
            combinaison.append(list(actions.keys())[i - 1])
            budget -= actions_list[i - 1][1]
        i -= 1

    # Calcul de la somme des bénéfices et des coûts
    somme_benefices = sum(actions[action]["Profit"] for action in combinaison)
    somme_couts = sum(actions[action]["Cout"] for action in combinaison)

    return combinaison, somme_benefices, somme_couts
