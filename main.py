from data.actions import charger_donnees_csv
from bruteforce import force_brute
from optimized import dynamic
import time

nom_fichier_csv = "data/actions.csv"

donnees = charger_donnees_csv(nom_fichier_csv)

DEPENSE_MAX = 500


def run(algo):
    time_before = time.time()
    actions_ids, somme_benefice, somme_couts = algo(donnees, DEPENSE_MAX)
    # Affichage des résultats
    print("Coût:", somme_couts)
    print("Meilleur profit:", somme_benefice)
    print("Meilleure combinaison:", actions_ids)
    time_after = time.time()
    print(f"Temps écoulé:", round(time_after - time_before, 2), "secondes")


parametre = dynamic

print(f"Début du programme de {parametre.__name__}")
run(parametre)
print(f"Fin du programme de {parametre.__name__}")
