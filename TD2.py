dico_notes = {"math": 14, "programmation": 12, "anglais": 16, "biologie": 10, "sport": 19}

# MÉTHODE 1 : Utiliser la fonction sum() et len() ---
moyenne1 = sum(dico_notes.values()) / len(dico_notes)
print("Moyenne méthode 1 :", moyenne1)

# MÉTHODE 2 : Calculer la moyenne avec une boucle ---
total = 0
for note in dico_notes.values():
    total += note
moyenne2 = total / len(dico_notes)
print("Moyenne méthode 2 :", moyenne2)

# Moyenne sans la note de biologie ---
dico_sans_bio = dico_notes.copy()
dico_sans_bio.pop("biologie")

moyenne_sans_bio = sum(dico_sans_bio.values()) / len(dico_sans_bio)
print("Moyenne sans la biologie :", moyenne_sans_bio)


# Exercice 2  

animaux = [("chien", 3), ("chat", 4), ("souris", 16)]

for animal, nombre in animaux:
    print(f"{animal} : {nombre}")

# Exercice 3  

etudiants = {"Alice": {"math": (15, 4), "info": (18, 4), "anglais": (12, 2)},"Bob": {"math": (10, 4), "info": (14, 4), "anglais": (11, 2)},"Chloé": {"math": (17, 4), "info": (19, 4), "anglais": (15, 2)},"David": {"math": (8, 4), "info": (9, 4), "anglais": (10, 2)}}

moyennes = {}
for nom, matieres in etudiants.items():
    total_points = 0
    total_coeffs = 0
    for note, coeff in matieres.values():
        total_points += note * coeff
        total_coeffs += coeff
    moyennes[nom] = total_points / total_coeffs

print("Moyenne pondérée de chaque étudiant :")
for nom, moy in moyennes.items():
    print(f"   {nom} : {moy:.2f}")


meilleur_etudiant = max(moyennes, key=moyennes.get)
print(f"Meilleur étudiant : {meilleur_etudiant} avec {moyennes[meilleur_etudiant]} de moyenne")

moyenne_globale = sum(moyennes.values()) / len(moyennes)
print(f"Moyenne globale du groupe : {moyenne_globale:}")

etudiants_bons = {nom: moy for nom, moy in moyennes.items() if moy >= 12}
print("Étudiants avec une moyenne ≥ 12 :")
for nom, moy in etudiants_bons.items():
    print(f"   {nom} : {moy:}")


etudiants_tries = dict(sorted(etudiants_bons.items(), key=lambda x: x[1], reverse=True))
print("Étudiants triés par ordre décroissant de moyenne :")
for nom, moy in etudiants_tries.items():
    print(f"   {nom} : {moy:}")

# Exercice 4

import random

dico_points_sans_atouts = {
    "7": 0,
    "8": 0,
    "9": 0,
    "V": 2,
    "D": 3,
    "R": 4,
    "d": 10,
    "A": 11
}

jeu_cartes = ["7", "8", "9", "d", "V", "D", "R", "A"] * 4
main = random.sample(jeu_cartes, k=8)
total_points = 0
for carte in main:
    points = dico_points_sans_atouts[carte]
    print(carte, "vaux", points, "points")
    total_points = total_points + points

print(f"Le nombre total de points de la main est {total_points}.")


