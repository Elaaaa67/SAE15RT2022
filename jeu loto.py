from numpy.random import randint
import numpy as np

y = int(input("Seed:"))
np.random.seed(0)

#tri cocktail
def cocktailSort(a):
    retour = True
    n = len(a)
    debut = 0
    fin = n-1
    while (retour==True):
        retour = False
        #les retours pertmets de changer de direction a chaque fois qu'une passes a été faites.
        #Premiere loop pour les passes de la droite a la gauche.
        #Ce qui permet de mettre les nombres les plus grand au debut c'est a dire à droite.

        for i in range(debut,fin):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                retour = True
        if (retour == False):
            break
        retour = False

        fin = fin - 1

        #deuxieme loop pour les passes de gauche a droit
        #ce qui permet de mettre les nombres les plus petit au début c'est a dire à la gauche
        for i in range(fin - 1, debut - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                retour = True
            debut = debut + 1
    return a
        #Return permet de renvoyer la valeur pour pouvoir la récuperer et la skocker dans une variable



if __name__ == '__main__':
    x = int(input("Entrez le nombre de tirages que vous voulez:"))
    for i in range(x):
        a = np.random.choice(range(1, 45), 5, replace=False)
        a = list(a)
        print("Le tirage est :", a)
        print("Tirage triée:", cocktailSort(a))

