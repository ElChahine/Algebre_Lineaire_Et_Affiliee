class Point:
    def __init__(self, coordonnees):
        self.coords = coordonnees
        self.dim = len(coordonnees)

    def __repr__(self):
        try:
            return "Points(" + str(self.coords) + ")"
        except AttributeError:
            return "Point (Données suprimmées / non-existantes)"
    
    def effacer(self):
        del self.coords
        del self.dim

class Vecteur(Point):
    def __init__(self, composantes, origine=None):
        if isinstance(composantes, Point):
            Point.__init__(self, composantes.coords)
        else:
            Point.__init__(self, composantes)

        if origine is None:
            self.origine = Point([0.0] * self.dim)
        else:
            if isinstance(origine, Point):
                self.origine = origine
            else:
                self.origine = Point(origine)
            if self.origine.dim != self.dim:
                raise ValueError("L'origine n'a pas la même dimension que les composantes")
            

    def __repr__(self):
        try:
            return "Vecteur(" + "composantes: " + str(self.coords) + "/ origine: " + str(self.origine.coords) + ")"
        except AttributeError:
            return "Vecteur (Composantes et origines suprimmées / non-existantes)"

    def effacer(self):
        Point.effacer(self)
        del self.origine
        
    def dimensions(self):
        return "Le vecteur possède " + str(self.dim) + " dimensions"
        
    def __add__(self, autre):
        if isinstance(self, Vecteur) and isinstance(autre, Vecteur):
            if self.dim != autre.dim:
                raise ValueError("Les deux vecteurs ne sont pas de la même dimension, addition impossible")
            else:
                coordonnees = []
                for i in range (self.dim):
                    coordonnees.append(self.coords[i] + autre.coords[i])
                return Vecteur(coordonnees, self.origine)
        else:
            raise AttributeError ("L'un ou les deux attributs ne sont pas des vecteurs")     
        
    def __mul__(self, coefficient):
        if isinstance(self, Vecteur) and isinstance(coefficient,(int, float)):
            coordonnees = []
            for i in range (self.dim):
                coordonnees.append(self.coords[i] * coefficient)
            return Vecteur(coordonnees, self.origine)
        else:
            raise AttributeError("Les attributs ne sont pas dans le bon ordre ou ne sont pas du bon type")
        
    def __matmul__(self, autre):
        if isinstance(self, Vecteur) and isinstance(autre, Vecteur):
            if self.dim != autre.dim:
                raise ValueError ("Les deux vecteurs ne sont pas de la même dimension, produit scalaire impossible")
            resultat = 0
            for i in range (self.dim):
                resultat += self.coords[i] * autre.coords[i]
            return resultat
        else:
            raise AttributeError ("L'un ou les deux attributs ne sont pas des vecteurs")
        
    def norme_carre(self):
        return self @ self
        
    def norme(self):
        return self.norme_carre() ** 0.5
    
    def normaliser(self):
        norme = self.norme
        if norme == 0:
            raise ValueError("Impossible de calculer la norme d'un vecteur nul")
        return self * (1/norme)


        
if __name__ == "__main__":
    print("----Test du module----\n")
    
    print("--Les points--")
    
    A = Point([1.0, 6.0])
    print("Point a:", A)
    A.effacer()
    print("Point a: ", A)

    print("---------\n")
    
    print("--Les vecteurs--")
    
    V = Vecteur([1.0, 8.2], [3.0, 4.2])
    print(V)
    print(V.dim)
    V.effacer()
    print("Vecteur v: ", V)
    
    try:
        V2 = Vecteur([1.0, 8.2], [3.0, 4.2, 4.85])
    except ValueError as e:
        print("Erreur interceptée: ", e)
        
    P1 = Point([1.0, 3.0])
    V1 = Vecteur(P1)
    
    P2 = Point([4.0, 0.4])
    P3 = Point([1.6, 5.7])
    V2 = Vecteur(P2, P3)
    print("Vecteur v1: ", V1)
    print("Vecteur v2: ", V2)
    print(V1.dimensions())
    V3 = V1 + V2
    print("V1 + V2: ", V3)
    
    try:
        V3 * 'string'
    except AttributeError as e:
        print("Erreur interceptée: ", e)
    





