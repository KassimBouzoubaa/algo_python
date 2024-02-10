from actions import charger_donnees_csv
from bruteforce import force_brute
from optimized import dynamic
import time


def run_algorithm(algorithm, data, max_spending):
    """
    Exécute un algorithme donné sur les données spécifiées.

    Args:
        algorithm (function): L'algorithme à exécuter.
        data (dict): Les données d'actions avec leurs coûts et bénéfices.
        max_spending (int): Le budget maximum pour l'algorithme.

    Returns:
        None
    """
    # Mesurer le temps d'exécution
    start_time = time.time()

    # Exécuter l'algorithme sur les données spécifiées
    action_ids, total_profit, total_costs = algorithm(data, max_spending)

    # Afficher les résultats
    print("Coût total:", total_costs)
    print("Meilleur profit:", total_profit)
    print("Meilleure combinaison d'actions:", action_ids)

    # Calculer le temps écoulé
    elapsed_time = round(time.time() - start_time, 2)
    print("Temps écoulé:", elapsed_time, "secondes")


# Définir le nom du fichier CSV contenant les données
csv_file_name = "data/actions.csv"

# Charger les données à partir du fichier CSV
data = charger_donnees_csv(csv_file_name)

# Définir le budget maximum
MAX_SPENDING = 500

# Choisir l'algorithme à exécuter (par exemple, force_brute ou dynamic)
selected_algorithm = dynamic

print(f"Début de l'exécution de l'algorithme {selected_algorithm.__name__}")
run_algorithm(selected_algorithm, data, MAX_SPENDING)
print(f"Fin de l'exécution de l'algorithme {selected_algorithm.__name__}")
