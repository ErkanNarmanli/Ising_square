#!/usr/bin/env python3
# -*-coding:utf-8 -*
from dessine import *
from random import *
from ising import *
import time

beta    = 2
n       = 120     # taille du carré
nb      = 400     # nombre d'images

init = get_random_mat(n)

mats = make_mats(init, nb, beta, n)

images = make_images(mats)

make_film(images)
