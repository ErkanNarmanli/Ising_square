#!/usr/bin/env pyton3
# -*-coding:utf-8 -*

from random import *

beta = 1
n    = 20 # taille du carré

def voisins(i,j):
    """
    Donne la liste des coordonnées des voisins de (i,j) dans la matrice
    """
