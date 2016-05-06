#!/usr/bin/python3
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
    """
    dessine une image à partir de la matrice de +1 et -1
    """
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

def make_images(mats):
    """
    dessine une liste d'images à partir d'une liste
    de matrices de +1 et -1
    """
    return list(map(dessine_carre, mats))

def make_film(images):
    """
    génère un film à partir d'une liste d'images
    stock le film à l'emplacement 'tmp/movie.mp4'
    plus tard il pourra être utile de mettre 
    l'emplacement du fichier en argument
    """
    # nombre d'images
    nb       = len(images)
    nb_digit = len(str(nb))
    
    for i in range(nb):
        images[i].save('tmp/im_' + str(i+1).zfill(nb_digit) + '.png') 

    os.system('cd tmp ; ffmpeg -r 10 -f image2 -i im_%0{}d.png -vcodec mpeg4 -y movie.mp4'.format(nb_digit))
    os.system('rm tmp/*.png')

def read_film():
    """
    lit l'emplacement du film
    """
    os.system('cvlc tmp/movie.mp4')

