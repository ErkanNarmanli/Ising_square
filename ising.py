#!/usr/bin/env pyton3
# -*-coding:utf-8 -*

from random import *
import numpy as np


beta = 1
n    = 20 # taille du carré

def voisins(i, j):
    """
    Donne la liste des coordonnées des voisins de (i,j) dans la matrice
    """
    res = []
    if (i != n-1):
        res.append((i+1, j))
    if (i != 0):
        res.append((i-1, j))
    if (j != n-1):
        res.append((i, j+1))
    if (j != 0):
        res.append((i, j-1))
    return res

def voisins_plus(i,j):
    """
    Ne donne que les voisins à droite et/ou en bas de (i,j)
    """
    res = []
    if (i != n-1):
        res.append((i+1, j))
    if (j != n-1):
        res.append((i, j+1))
    return res

def energie(config):
    """
    Calcule l'energie d'une configuration d'Ising
    """
    h = 0
    for i in range(n):
        for j in range(n):
            for (k,l) in voisins_plus(i,j):
                h += config[i,j]*config[k,l]
    return (-h)

def energie_sommet(config, i, j):
    """
    Calcule le S(sigma,v)
    """
    h = 0
    for i in range(n):
        for j in range(n):
            for (k, l) in voisins(i, j):
                h += config[i, j]*config[k, l]
    return h

def proba_sommet(config, i, j):
    """
    Donne la proba p(sigma, v) que v soit changé en +1
    """
    s   = energie_sommet(config, i, j)
    res = np.exp(beta*s)/(np.exp(beta*s)+np.exp(-beta*s))
    return res

def step(config):
    """
    rend la configuration avancée d'un pas selon la dynamique de Glauber
    """
    i   = randint(0,n-1)
    j   = randint(0,n-1)
    u   = np.randon.rand()
    p   = proba_sommet(config, i, j)
    res = np.copy(config)
    if(u<p):
        res[i, j] = +1
    else:
        res[i, j] = -1
    return res
    

