#!/usr/bin/python
# -*-coding:utf-8 -*
from dessine import *
from random import *
import time

n = 20
nb = 40
mats = list(range(nb))

for k in range(nb):
    mats[k] = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            mats[k][i,j] = randint(0,1)

images = make_images(mat)

make_film(images)
read_film()
