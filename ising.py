#!/usr/bin/env python3
# -*-coding:utf-8 -*

from random import *
import numpy as np

def voisins(i, j, n):
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

def voisins_plus(i,j, n):
    """
    Ne donne que les voisins à droite et/ou en bas de (i,j)
    """
    res = []
    if (i != n-1):
        res.append((i+1, j))
    if (j != n-1):
        res.append((i, j+1))
    return res

def energie(config, n):
    """
    Calcule l'energie d'une configuration d'Ising
    """
    h = 0
    for i in range(n):
        for j in range(n):
            for (k,l) in voisins_plus(i, j, n):
                h += config[i,j]*config[k,l]
    return (-h)

def energie_sommet(config, i, j, n):
    """
    Calcule le S(sigma,v)
    """
    h = 0
    for (k, l) in voisins(i, j, n):
        h += config[i, j]*config[k, l]
    return h

def proba_sommet(config, i, j, beta, n):
    """
    Donne la proba p(sigma, v) que v soit changé en +1
    """
    s   = energie_sommet(config, i, j, n)
    res = 0.5*(1+np.tanh(beta*s))   
    return res

def step(config, beta, n):
    """
    rend la configuration avancée d'un pas selon la dynamique de Glauber
    """
    i   = randint(0,n-1)
    j   = randint(0,n-1)
    u   = np.random.rand()
    p   = proba_sommet(config, i, j, beta, n)
    res = np.copy(config)
    if(u<p):
        res[i, j] = +1
    else:
        res[i, j] = -1
    return res

def iter_step(config, beta, n, k):
    """
    itère step
    """
    res = np.copy(config)
    for i in range(k):
        res = step(res, beta, n)
    return res
    
def make_mats(init, nb, beta, n):
    """
    génère une liste de config à partir d'une configuration initiale
    génère nb config (en comptant la config initiale
    """
    mats    = list(np.ones((nb, n, n)))
    mats[0] = np.copy(init)
    for i in range(nb-1):
        mats[i+1] = step(mats[i], beta, n)
    return mats

def get_random_mat(n):
    res = np.ones((n,n))
    for i in range(n):
        for j in range(n):
            res[i, j] = (randint(0, 1) - 0.5)*2
    return res
