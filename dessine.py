#!/usr/bin/python
# -*-coding:utf-8 -*

"""
Dessine le carré à partir d'une matrice carrée de +1 ou -1
"""

from PIL import Image, ImageDraw, ImageFont
from cmath import *
from colorsys import *
import sys
import os
import numpy as np

#Constantes 
taille      = 900 #nombre de pixels du carré
col_plus    = (50, 50, 50)

def get_coord(i,j,n):
    """
    rend les coordonnées qui délimite la face (i,j)
    n est la taille de la matrice
    """
    x_1 = i*taille/n
    x_2 = (i+1)*taille/n
    y_1 = j*taille/n
    y_2 = (j+1)*taille/n

    return([(x_1, y_1), (x_2, y_2)])

def dessine_face(i,j,n,col,draw):
    """
    colorie la face (i,j) de la couleur demandée
    """
    draw.rectangle(get_coord(i,j,n), fill=col)

def dessine_carre(mat):
    # On récupère la taille de mat
    n = np.size(mat[0])
    # Déclaration de l'image
    image = Image.new('RGB', (taille, taille), (255, 255, 255))
    # Outil de dessin
    draw = ImageDraw.Draw(image)
    # On parcourt la matrice
    for i in range(n):
        for j in range(n):
            if (mat[i,j] == 1):
                dessine_face(i, j, n, col_plus, draw)
    # On a fini
    return(image)

def gif(images):
    # nombre d'images
    nb  = len(images)
    
    for i in range(nb):
        images[i].save('tmp/im_' + str(i) + '.png') 

    os.system('convert tmp/*.png tmp/animation.gif')
    os.system('rm tmp/*.png')
