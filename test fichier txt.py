filin = open("test.txt","r")
lignes = filin.readlines()
filin.close()
print(lignes)

with open("test.txt",'r') as filin:
    lignes = filin.readlines()
    for ligne in lignes:
        print(ligne)

animaux2 = ["poisson ","abeille ","chat ","chien "]
with open("test.txt",'a') as filout:
    for animal in animaux2:
        filout.write(animal + "\n")

