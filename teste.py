import numpy as np
from sklearn.utils.extmath import cartesian
import math as mt
import cv2

teta = 30
a = np.array([5,5,5])
p = np.array([5,5,6])
def rotateZ(teta):
        return np.matrix([[mt.cos(teta), -mt.sin(teta), 0],
                         [mt.sin(teta),  mt.cos(teta),0],
                         [0,0,1]])
w = a/np.linalg.norm(a)
t = np.copy(w)
t[np.argmin(t)] = 1

u = np.cross(t,w)/ np.linalg.norm(np.cross(t,w))

v = np.cross(u,w)

Ruvw = np.matrix([u,v,w])
auvw = np.linalg.multi_dot([Ruvw,rotateZ(teta),Ruvw.T])
print auvw.dot([1,2,3])
print auvw.dot([2,3,4])
print 
