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
        Point.__init__(self, composantes)
        if origine is None:
            self.origine = Point([0.0] * self.dim)
        else:
            if self.origine.dim != self.dim:
                raise ValueError("L'origine n'a pas la même dimension que les composantes")
            self.origine = origine

    def __repr__(self):
        try:
            return "Vecteur(" + "composantes: " + str(self.coords) + "/ origine: " + str(self.origine.coords) + ")"
        except AttributeError:
            return "Vecteur (Composantes et origines suprimmées / non-existantes)"

    def effacer(self):
        del self.coords
        del self.origine


        
if __name__ == "__main__":
    print("Test du module")
    A = Point([1.0, 6.0])
    print("Point a:", A)

    A.effacer()
    print("Point a: ", A)

    print("---------")
    V = Vecteur([1.0, 8.2], None)
    print(V)



