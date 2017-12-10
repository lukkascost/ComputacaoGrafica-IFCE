import numpy as np
import matplotlib.mlab as ml
import cv2



def centroCubos(objetos):
        pontos= []
        for i in objetos:
                pontos.append(i.p1)
                pontos.append(i.p2)
                pontos.append(i.p3)
                pontos.append(i.p4)
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
                cores = [[255,0,0],[0,255,0],[0,0,255]]
                self.p1 = p1;
                self.p2 = p2;
                self.p3 = p3;
                self.p4 = p4;
                self.rgb  = cores[cor]
                self.centro =  np.matrix([p1,p2,p3,p4]).mean(axis=0)
                self.normal = np.cross(p1 - self.centro, p2 - self.centro)
        
                self.minX = min([p1[0],p2[0],p3[0],p4[0]])
                self.maxX = max([p1[0],p2[0],p3[0],p4[0]])
                self.minY = min([p1[1],p2[1],p3[1],p4[1]])
                self.maxY = max([p1[1],p2[1],p3[1],p4[1]])
                self.maxZ = max([p1[2],p2[2],p3[2],p4[2]])
                self.minZ = min([p1[2],p2[2],p3[2],p4[2]])              
                
    
        