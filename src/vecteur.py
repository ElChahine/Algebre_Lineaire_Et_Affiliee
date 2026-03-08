class Vecteur:
    def __init__(self, composantes):
        self.coords = composantes[:]
        self.dim = len(composantes)
            

    def __repr__(self):
        return "Vecteur(" + "composantes: " + str(self.coords) + ", dimension: " + str(self.dim) + ")"

    def __del__(self):
        del self.coords
        del self.dim
        
    def getitem(self, index):
        if index < self.dim:
            return self.coords[index]
        else:
            raise IndexError("Il n'y a pas d'index de cette valeur dans le vecteur")
        
    def dimension(self):
        return self.dim
        
    def inverse(self):
        coordonnees = []
        for i in range (self.dim):
            coordonnees.append(self.coords[i] * -1)
        return Vecteur(coordonnees)
        
    def compatible(self, autre):
        if isinstance(self, Vecteur) and isinstance(autre, Vecteur):
            if self.dim == autre.dim:
                return True
            else:
                raise ValueError("Les deux vecteurs ne sont pas de la même dimension, addition impossible")
        else:
            raise TypeError ("L'un ou les deux attributs ne sont pas des vecteurs")  
        
    def __add__(self, autre):
        if self.compatible(autre):
            coordonnees = []
            for i in range (self.dim):
                coordonnees.append(self.coords[i] + autre.coords[i])
            return Vecteur(coordonnees)

    def __sub__(self, autre):
        if self.compatible(autre):
            coordonnees = []
            for i in range (self.dim):
                coordonnees.append(self.coords[i] - autre.coords[i])
            return Vecteur(coordonnees)
        
    def __truediv__(self, coefficient):
        coordonnees = []
        for i in range(self.dim):
            coordonnees.append(self.coords[i] / coefficient)
        return Vecteur(coordonnees)
        
    def __mul__(self, coefficient):
        coordonnees = []
        for i in range (self.dim):
            coordonnees.append(self.coords[i] * coefficient)
        return Vecteur(coordonnees)
        
    def __rmul__(self, coefficient):
        return self.__mul__(coefficient)
        
        
    def __matmul__(self, autre):
        if self.compatible(autre):
            resultat = 0
            for i in range (self.dim):
                resultat += self.coords[i] * autre.coords[i]
            return resultat
        
    def norme_carre(self):
        return self @ self
        
    def norme(self):
        return self.norme_carre() ** 0.5
    
    
    def normaliser(self):
        norme = self.norme()
        if norme == 0:
            raise ValueError("Impossible de calculer la norme d'un vecteur nul")
        return self * (1/norme)


        
if __name__ == "__main__":
    
    print("----Test du module----\n")
        
    print("--Les vecteurs--\n")
    
    print("-Affichage-\n")
    # Initialisation d'un vecteur simple en 2D
    V1 = Vecteur([1.0, 8.2])
    print(V1)

    print("\n-Supression-\n")

    del V1
    # On supprime l'étiquette V1
    try:
        print(V1)
        # On vérifie que V1 n'existe plus dans l'espace de noms
    except NameError:
        print("Vecteur (Composantes supprimée / non-existante)")


    print("\n-index-\n")

    V2 = Vecteur([5.6, 8.3, 9.4])
    print(V2.getitem(2))
    
    try:
        print(V2.getitem(3))
    except IndexError as e:
        print(e)


    print("\n-dimension-\n")

    print(V2.dimension())
    
    
    print("\n-inverse-\n")

    V2 = Vecteur([5.6, 8.3, 9.4])
    print(V2.inverse())


    print("\n-Addition-\n")

    V3 = Vecteur([4.7, 9.2, 1.8])

    # Test d'une addition valide (3D + 3D)
    V_add = V2 + V3
    print("V2 + V3 = ", V_add, "\n")

    V5 = Vecteur([5.54])

    try:
        # Test d'addition impossible, dimensions incompatibles
        V_add_err = V_add + V5
        print("V2 + V3 = ", V_add, "\n")
    except ValueError as e:
        print(e)

    print("\n-Multiplication-\n")

    # Test multiplication d'un vecteur par un scalaire
    V_mult = V2 * 2
    print("V2 * 2 = ", V_mult, "\n")
    
    V_mult_2 = 2 * V_mult
    print("2 * V_mult = ", V_mult_2, "\n")

    

    print("\n-Produit scalaire-\n")
    
    # Rappel : V2 = [5.6, 8.3, 9.4] et V3 = [4.7, 9.2, 1.8]
    V_scal = V2 @ V3
    print("V2 @ V3 = ", V_scal, "\n")

    try:
        # Test avec des dimensions différentes (V2: dim 3, V5: dim 1)
        V_scal_err = V2 @ V5
    except ValueError as e:
        print(e)

    print("\n-Norme-\n")

    print("Norme au carré de V2 = ", V2.norme_carre())
    print("Norme de V2 = ", V2.norme(), "\n")

    print("\n-Normalisation-\n")

    V2_unitaire = V2.normaliser()
    print("V2 normalisé = ", V2_unitaire)
    # On vérifie que la norme du vecteur normalisé est bien égale à 1
    print("Vérification de la norme de V2 normalisé = ", V2_unitaire.norme(), "\n")

    try:
        # Test avec un vecteur nul (norme = 0)
        V_nul = Vecteur([0.0, 0.0, 0.0])
        V_nul.normaliser()
    except ValueError as e:
        print(e)