from itertools import combinations, chain


def force_brute(actions, depense):
    """
     Résout le problème de maximisation de bénéfice en utilisant une approche de force brute.

     Args:
         actions (dict): Dictionnaire d'actions avec leurs coûts et bénéfices.
         depense (int): La dépense maximale autorisée.

    Returns:
         list: Une combinaison d'actions optimale.
         float: La somme des bénéfices.
         float: La somme des coûts.
    """

    # Initialisation des variables pour stocker la meilleure combinaison et le meilleur profit
    meilleure_combinaison = None
    somme_benefices = 0

    # Générer toutes les combinaisons possibles d'actions
    toutes_combinaisons = chain.from_iterable(
        combinations(actions.items(), r) for r in range(1, len(actions) + 1)
    )

    # Parcourir toutes les combinaisons possibles
    for combinaison_actuelle in toutes_combinaisons:
        # Calculer le coût total et le profit total de la combinaison actuelle
        cout_total = sum(action["Cout"] for _, action in combinaison_actuelle)
        profit_total = sum(action["Profit"] for _, action in combinaison_actuelle)

        # Vérifier si le coût total est inférieur ou égal à la dépense maximale
        # et si le profit total est supérieur au meilleur profit trouvé jusqu'à présent
        if cout_total <= depense and profit_total > somme_benefices:
            # Mettre à jour la meilleure combinaison et le meilleur profit
            meilleure_combinaison, somme_benefices = combinaison_actuelle, profit_total

    # Récupération des ids de la meilleure combinaison
    ids_meilleure_combinaison = [id for id, _ in meilleure_combinaison]

    # Calcul du coût total de la meilleure combinaison
    somme_couts = sum(action[1]["Cout"] for action in meilleure_combinaison)

    return ids_meilleure_combinaison, somme_benefices, somme_couts
