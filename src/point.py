class Point:
    def __init__(self, coordonnees):
        """
        Description de la fonction

        Args:
            nom (type): [Description].
            nom (type): [description].

        Returns:
            type: Description.
        """
        self.coords = coordonnees[:]
        self.dim = len(coordonnees)

    def __repr__(self):
        try:
            return "Points(" + str(self.coords) + ")"
        except AttributeError:
            return "Point (Données suprimmées / non-existantes)"
    
    def __del__(self):
        del self.coords
        del self.dim


if __name__ == "__main__":
    print("----Test du module----\n")
    
    print("--Les points--")

    mes_coords = [1.0, 6.0]
    print(mes_coords)

    A = Point(mes_coords)
    print("Point a:", A)

    mes_coords.append(5)
    print(mes_coords)

    print("Point a: ", A)

    print("---------\n")