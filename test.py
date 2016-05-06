#!/usr/bin/env python3
# -*-coding:utf-8 -*
from dessine import *
from random import *
from ising import *
import time

n = 20      # taille du carré
nb = 400     # nombre d'images

init = np.ones((n,n))
# for i in range(n):
#     for j in range(n):
#         init[i, j] = (randint(0,1)-0.5)*2


mats = make_mats(init, nb)

images = make_images(mats)

make_film(images)
read_film()
