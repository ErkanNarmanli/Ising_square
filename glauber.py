#!/usr/bin/env python3
# -*-coding:utf-8 -*

from dessine import *
from ising import *
from random import *
from PIL import ImageTk
import sys
import time
import tkinter as tk

n               = 100
update_time     = 1    # en millisecondes
nb_step         = 40

if(sys.argv[1]=="COLD"):  beta    = 1
elif(sys.argv[1]=="HOT"): beta    = 0.4
elif(sys.argv[1]=="MID"): beta    = 0.7

if(sys.argv[2]=="RANDOM"): mat = get_random_mat(n)
elif(sys.argv[2]=="UNIF"): mat     = np.ones((n,n))

app     = tk.Tk()
frame   = dessine_carre(mat)
tkimage = ImageTk.PhotoImage(frame)
label   =  tk.Label(app, image=tkimage)
label.pack()


def main():
    app.after(500, update_image)
    app.mainloop()

def update_image():
    global mat
    global frame
    global tkimage
    global new_frame
    (frame, new_mat) = frame_step(mat)
    tkimage = ImageTk.PhotoImage(frame)
    mat     = new_mat
    label.config( image = tkimage)
    # call this function again
    label.after(update_time, update_image)

def frame_step(mat):
    frame   = dessine_carre(mat) 
    new_mat = iter_step(mat, beta, n, nb_step)
    return(frame, new_mat)

if __name__ == "__main__":
        main()
