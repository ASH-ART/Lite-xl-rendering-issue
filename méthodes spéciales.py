# Créé par Lucien Arnauld, le 16/09/2021 en Python 3.7
class Voiture:
    """Un objet de cette classe est une Voiture, définie par sa marque, son modèle et sa couleur"""
    def __init__(self,marque,modele,couleur):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
    def __str__(self):
        return (("Marque : {} "+"\n"+"Modèle : {}"+"\n"+"Couleur : {}").format(self.marque,self.modele,self.couleur))
    def __eq__(self,other):
        return self.couleur==other.couleur

v1 = Voiture("Peugeot","3008","rouge")
v2 = Voiture("Peuheot","5008","rouge")


