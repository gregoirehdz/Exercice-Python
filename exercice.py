# Exo 1
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
for jour in semaine:
    if jour in ["Lundi", "Mardi", "Mercredi", "Jeudi"]:
        print(f"{jour} : Au travail !")
    elif jour == "Vendredi":
        print(f"{jour} : Chouette c'est vendredi !")
    else:
        print(f"{jour} : Repos ce week-end.")

# Exo 2
liste = [8, 4, 6, 1, 5]

plus_petit = liste[0]
for nb in liste:
    if nb < plus_petit:
        plus_petit = nb

print("Le plus petit élément est :", plus_petit)

# Exo 3

notes = [14, 9, 13, 15, 12]

note_max = notes[0]
note_min = notes[0]
somme = 0

for note in notes:
    if note > note_max:
        note_max = note
    if note < note_min:
        note_min = note
    somme += note

moyenne = somme / len(notes)

print("Note maximum :", note_max)
print("Note minimum :", note_min)
print("Moyenne :", round(moyenne, 2))

if 10 <= moyenne < 12:
    print("Mention : passable")
elif 12 <= moyenne < 14:
    print("Mention : assez bien")
elif moyenne >= 14:
    print("Mention : bien")
else:
    print("Mention : insuffisant")

# Exo 4 

for i in range(21):
    if i % 2 == 0 and i <= 10:
        print(i, "est pair et <= 10")
    elif i % 2 != 0 and i > 10:
        print(i, "est impair et > 10")

# Exo 5 

n = 2
for i in range(n):
    for j in range(n):
        print(f"Ligne {i}, Colonne {j}")

# Exo 6 

for i in range(11):
    print("*" * i)

# Exo 7

import random 

position = 0   
arrivee = 5   
sauts = 0     


while position != arrivee:
    
    deplacement = random.choice([-1, 1])
    position += deplacement
    sauts += 1
    print(f"Saut {sauts} : déplacement de {deplacement}, position actuelle = {position}")

print(f"\nLa puce est arrivée à la position {arrivee} en {sauts} sauts.")   
