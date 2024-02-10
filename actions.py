import csv


def charger_donnees_csv(nom_fichier):
    """
    Charge les données à partir d'un fichier CSV contenant des informations sur les actions.

    Args:
        nom_fichier (str): Le chemin du fichier CSV à charger.

    Returns:
        dict: Un dictionnaire contenant les informations sur les actions avec leurs coûts et bénéfices.
              Les actions avec un coût inférieur ou égal à 0 sont ignorées.
              None est retourné si le fichier spécifié n'est pas trouvé.
    """
    actions = {}

    try:
        with open(nom_fichier, mode="r") as fichier_csv:
            lecteur = csv.reader(fichier_csv)

            # Ignorer l'en-tête
            en_tete = next(lecteur, None)

            for ligne in lecteur:
                id, cout, benefice = ligne

                # Ignorer les actions avec un coût inférieur ou égal à 0
                if float(cout) > 0:
                    actions[id] = {
                        "Cout": float(cout),
                        "Benefice": float(benefice),
                    }

        print(f"Données chargées depuis {nom_fichier}.")
        return actions

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return None
