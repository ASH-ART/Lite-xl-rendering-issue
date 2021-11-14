# Créé par Lucien Arnauld, le 04/10/2021 en Python 3.7
from time import *
def listechai_vide():
    return ()

def est_vide(lst):
    return lst==()

def ajoute_tete(x,lst):
    return(x,lst)

def renvoie_tete(lst):
    if est_vide(lst): return 0
    else:
        return lst[0]

def renvoie_queue(lst):
    if not est_vide(lst):
        return lst[1:]
    #return lst[1]

def afficherListe(lst):
    listeJolie = ""
    for e in lst:
        listeJolie += str(e)
    return listeJolie

def lireElement(lst,position):
    liste = lst
    for i in range(1,position):
        liste = liste[1]
    return liste[0]

def insererElement(x,lst,position):
    ele = x
    lstchain = lst
    pos = position

    for i in range (1,pos):
        liste = liste[1]
    lstchain[1] = (ele,lstchain[1][0])

liste = listechai_vide()
ajoute_tete(1,liste)
ajoute_tete(32,liste)
insererElement(3,liste,1)