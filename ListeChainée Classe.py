# Créé par Lucien Arnauld, le 11/10/2021 en Python 3.7
class Cellule:
    def __init__(self,val,suivant):
        self.valeur = val
        self.suivant = suivant
    def getSuivant(self):
        return self.suivant
    def getValue(self):
        return self.valeur
    def setSuivant(self,suivant):
        self.suivant = suivant

def longueur(lst):
    n = 0
    listeChain = lst
    while listeChain.getSuivant() is not None:
        n+=1
        listeChain = listeChain.getSuivant()

def longueurRec(lst):
    listeChain = lst
    if listeChain is None: return 0
    else: return 1+longueurRec(listeChain.getSuivant())

def ajouter(lst,cel,n):
    i = 0
    lstchai = lst
    while i<n and lstchain.getSuivant() is not None:
        i+=1
        lstchai = lstchai.getSuivant()

    pointeur = lstchai.getSuivant()
    cel = Cellule(cel,pointeur)
    lstchai.setSuivant(cel)

def retirer(lst,ele):
    element = ele
    cellule = lst
    precedent = None
    suivant = None
    while cellule.valeur != ele:
        precedent = cellule
        cellule = cellule.suivant
        suivant = cellule.suivant
    precedent.suivant = suivant
