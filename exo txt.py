notes = []
with open('test.txt','r') as notes_read:
    lignes = notes_read.readlines()
    for ligne in lignes:
        notes.append(float(ligne))

print(notes)

sommes = 0
for note in notes:
    sommes += note
print(sommes)

moyenne = sommes/len(notes)
print(moyenne)


with open("test.txt", "r") as f:       #read only donc on peut seulement lire d'ou le r
    lignes = f.readlines()        

notes = []                              #initialise la liste vide qui contiendra les notes 

                                        # Parcourt chaque ligne et extrait les notes
for ligne in lignes:
        note = float(ligne.strip())     # Convertit la ligne en float
        notes.append(note)

                                        # Écrit le résultat dans un nouveau fichier
with open("notes2.txt", "w") as f2:       #write avec le d'ou le w pour écire 
    for note in notes:
        statut = "admis" if note >= 10 else "recalé"        #étape de vérification si la note est >10 alors admis sinon recalé
        f2.write(f"{note} {statut}\n")                      #écrire dans le fichier  

print("Fichier 'notes2.txt' créé avec succès !")
