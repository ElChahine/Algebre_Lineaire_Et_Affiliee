from vecteur import Vecteur

class Matrice:
    def __init__(self, donnees):
        self.mat = []
        for liste in donnees:
            self.mat.append(Vecteur(liste[:]))
        self.nb_lignes = len(donnees)
        self.nb_colonnes = len(donnees[0])

        for ligne in self.mat:
            if ligne.dim != self.nb_colonnes:
                raise ValueError("Toutes les lignes doivent avoir la même longueur")
    
    def __str__(self):
        try:
            res = "Matrice (" + str(self. nb_lignes) + " x " + str(self.nb_colonnes) + " :\n"
            for v in self.mat:
                res += "  " + str(v) + "\n"
            return res
        except AttributeError:
            return "Point (Données suprimmées / non-existantes)"
        
    def compatible(self, autre):
        return self.nb_lignes == autre.nb_lignes and self.nb_colonnes == autre.nb_colonnes

    def __add__(self, autre):
        if self.compatible(autre):
            donnees = []
            for i in range(self.nb_lignes):
                somme_v = self.mat[i] + autre.mat[i]
                donnees.append(somme_v.coords)
        return Matrice(donnees)
              
    def __mul__(self, coefficient):
        donnees = []
        for i in range(self.nb_lignes):
            mult_v = self.mat[i] * coefficient
            donnees.append(mult_v.coords)
        return Matrice(donnees)
    
    def __rmul__(self, coefficient):
        return self.__mul__(coefficient)

    def __matmul__(self, autre):
        pass

    def get_colonnes(self, j):
        if j < self.nb_colonnes:
            colonne = []
            for v in self.mat:
                colonne.append(v.getitem(j))
            return colonne
        else:
            raise IndexError("le numéro de colonne donné n'existe pas dans la matrice")

    def transposer(self):
        donnees = []
        for i in range (self.nb_colonnes):
            colonne = self.get_colonnes(i)
            donnees.append(colonne)
        return Matrice(donnees)

    def permuter_ligne(self, i, j):
        self.mat[i], self.mat[j] = self.mat[j], self.mat[i]

    def inserer_ligne(self, liste_nombres):
        nouveau_v = Vecteur(liste_nombres)
        if nouveau_v.dim != self.nb_colonnes:
            raise ValueError("La ligne n'a pas la bonne dimension")
        self.mat.append(nouveau_v)
        self.nb_lignes += 1

    def ajouter_ligne():
        pass

    def resolution_gauss():
        pass


if __name__ == "__main__":

    print("----Test du module----\n")

    print("---les matrices---\n")

    print("- Création et Affichage -\n")
    M1 = Matrice([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ])
    print(M1)

    print("\n- Test erreur de construction -\n")
    try:
        # Lignes de tailles différentes
        M_err = Matrice([[1, 2], [3, 4, 5]])
    except ValueError as e:
        print(e)

    print("\n Test de compatibilité \n")

    M2 = Matrice([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ])
    print(M2)

    print(M1.compatible(M2))

    M3 = Matrice([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [5.2, 8.4, 4.0]
    ])
    print(M3)

    print(M1.compatible(M3))


    print("\n Addition \n")

    print(M1)
    print(M2)

    M4 = M1 + M2

    print(M4)


    print("\n Multiplication \n")

    M4 = M4 * 2

    print(M4)

    print("\n Colonne \n")

    print(M4.get_colonnes(0))
    print(M4.get_colonnes(2))
    
