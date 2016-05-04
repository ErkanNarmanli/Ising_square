#!/usr/bin/python
# -*-coding:utf-8 -*
from dessine import *
from random import *
import time

n = 20

# On initialise la matrice
mat = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        mat[i,j] = randint(0,1)

mat2 = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        mat2[i,j] = randint(0,1)

# On dessine
im  = dessine_carre(mat)
im2 = dessine_carre(mat2)

gif([im, im2])
