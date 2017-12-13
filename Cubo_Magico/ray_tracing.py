import numpy as np
import matplotlib.mlab as ml
import cv2
import math as mt

def centroCubos(objetos):
        pontos= []
        for i in objetos:
                pontos.append(i.pontos[1])
                pontos.append(i.pontos[2])
                pontos.append(i.pontos[3])
                pontos.append(i.pontos[4])
        return np.array(pontos).mean(axis=0)
#----------------------------------------------------------------------
def buildBases(w):
        """"""
        t = np.copy(w)
        _, p  = np.abs(w).min(0) ,np.abs(w).argmin(0)
        t[p] = 1
        
        u = np.divide(np.cross( t, w ),  ml.norm_flat(np.cross(t, w)))
        v = np.cross(w,u)
        return np.round(u,4), np.round(v,4)
        
########################################################################
class quadrado(object):
        """"""

        #----------------------------------------------------------------------
        def __init__(self, p1, p2 ,p3 ,p4 , cor):
                """Constructor"""
                cores = [[255,0,0],[0,255,0],[0,0,255],[255,255,255],[255,255,0],[0,255,255]]
                self.pontos = np.array([[0,0,0], p1,p2,p3,p4])
                self.centro = np.matrix([p1,p2,p3,p4]).mean(axis=0)
                self.rgb  = cores[cor]
                self.normal = np.cross(p1 - self.centro, p2 - self.centro)
        
                self.minX = min([p1[0],p2[0],p3[0],p4[0]])
                self.maxX = max([p1[0],p2[0],p3[0],p4[0]])
                self.minY = min([p1[1],p2[1],p3[1],p4[1]])
                self.maxY = max([p1[1],p2[1],p3[1],p4[1]])
                self.maxZ = max([p1[2],p2[2],p3[2],p4[2]])
                self.minZ = min([p1[2],p2[2],p3[2],p4[2]])              
                
        def rotateZ(self,Ruvw, q,f):
                for i in range(len(self.pontos)):
                        self.pontos[i] = np.dot(Ruvw,self.pontos[i])
                        #x = 0
                        #y = self.pontos[i][0]*mt.sin(q)+ self.pontos[i][1]*mt.cos(q)
                        #z = self.pontos[i][0]*mt.cos(q)*mt.sin(f)- self.pontos[i][1]*mt.sin(q)*mt.sin(f) + self.pontos[i][2]*mt.cos(f)
                        #self.pontos[i] = np.array([x,y,z])
                
########################################################################
class Cubo:
        """"""

        #----------------------------------------------------------------------
        def __init__(self):
                """Constructor"""
                self.objetos = []
                for i in range(3):
                        self.objetos.append(quadrado([0,i,0], [1,i,0], [0,i+1,0], [2,i+1,0], (i+0)%6 ))
                        self.objetos.append(quadrado([1,i,0], [2,i,0], [1,i+1,0], [2,i+1,0], (i+1)%6 ))
                        self.objetos.append(quadrado([2,i,0], [3,i,0], [2,i+1,0], [3,i+1,0], (i+2)%6 ))        
        
                        self.objetos.append(quadrado([0,i,3], [1,i,3], [0,i+1,3], [1,i+1,3], (i+3)%6 ))
                        self.objetos.append(quadrado([1,i,3], [2,i,3], [1,i+1,3], [2,i+1,3], (i+4)%6 ))
                        self.objetos.append(quadrado([2,i,3], [3,i,3], [2,i+1,3], [3,i+1,3], (i+5)%6 ))   
                        
                        self.objetos.append(quadrado([0,0,i], [1,0,i], [0,0,i+1], [1,0,i+1], (i+6)%6 ))         
                        self.objetos.append(quadrado([1,0,i], [2,0,i], [1,0,i+1], [2,0,i+1], (i+7)%6 )) 
                        self.objetos.append(quadrado([2,0,i], [3,0,i], [2,0,i+1], [3,0,i+1], (i+8)%6 )) 
                
                        self.objetos.append(quadrado([0,3,i], [1,3,i], [0,3,i+1], [1,3,i+1], (i+9)%6 ))
                        self.objetos.append(quadrado([1,3,i], [2,3,i], [1,3,i+1], [2,3,i+1], (i+10)%6 ))
                        self.objetos.append(quadrado([2,3,i], [3,3,i], [2,3,i+1], [3,3,i+1], (i+11)%6 ))   
                        
                        self.objetos.append(quadrado([0,0,i], [0,1,i], [0,0,i+1], [0,1,i+1], (i+12)%6 ))         
                        self.objetos.append(quadrado([0,1,i], [0,2,i], [0,1,i+1], [0,2,i+1], (i+13)%6 ))                
                        self.objetos.append(quadrado([0,2,i], [0,3,i], [0,2,i+1], [0,3,i+1], (i+14)%6 ))                      
                
                        self.objetos.append(quadrado([3,0,i], [3,1,i], [3,1,i+1], [3,0,i+1], (i+15)%6 ))
                        self.objetos.append(quadrado([3,1,i], [3,2,i], [3,2,i+1], [3,1,i+1], (i+16)%6 ))
                        self.objetos.append(quadrado([3,2,i], [3,3,i], [3,3,i+1], [3,2,i+1], (i+17)%6 ))                           