from ray_tracing import *

"""Geraçao das matrizes de Rotaçao"""
def rotateZ(teta):
        return np.matrix([[mt.cos(teta), -mt.sin(teta), 0],
                         [mt.sin(teta),  mt.cos(teta),0],
                         [0,0,1]])
def rotateX(teta):
        return np.matrix([[1,0,0],
                          [0,mt.cos(teta), -mt.sin(teta)],
                          [0, mt.sin(teta),  mt.cos(teta)]])
def rotateY(teta):
        return np.matrix([[mt.cos(teta),0, mt.sin(teta)],
                          [0,1,0],
                          [-mt.sin(teta), 0,  mt.cos(teta)]])


for k in range(1):
        
        cubo = Cubo()
        
        centroCu = centroCubos(cubo.objetos)
        
        nx = 100
        ny = 100
        teta = 0
        
        l = -6
        r = 6
        t = 6 
        b = -6

        
        """ Aplica a Rotação em X, Y e Z nos graus informados"""
        e = np.array([1 + 1e-3 ,1 +  1e-3, -1 + 1e-3])
        e = np.array(rotateX(mt.radians(-20)).dot(e))[0,:]
        e = np.array(rotateY(mt.radians(0)).dot(e))[0,:]
        e = np.array(rotateZ(mt.radians(0)).dot(e))[0,:]
        
        ww = np.round(e/ml.norm_flat(e),4)
        uu , vv = buildBases(ww)
        image = np.zeros((nx,ny,3))

        """ Inicio do Ray-Trace"""
        for i in range(nx):
                for j in range(ny):
                        u = l + ((r - l)*(i+1 + 0.5))/nx
                        v = b + ((t - b)*(j+1 + 0.5))/ny   
                        origin = np.round(np.add(e, np.add(np.multiply(u,uu) ,np.multiply(v,vv))),4)
                        direction = -ww
                        menorTT = 10000000000
                        indMenor = -1
                        for ob in range(len(cubo.objetos)):
                                tt = np.round(np.divide(np.dot((cubo.objetos[ob].pontos[1] - origin), cubo.objetos[ob].normal.T) , np.dot(direction, cubo.objetos[ob].normal.T)),4)
                                p = np.round(origin + np.multiply(tt, direction),4)
                                
                                aiDento = p[0] >= cubo.objetos[ob].minX and p[0] <= cubo.objetos[ob].maxX and p[1] >= cubo.objetos[ob].minY and p[1] <= cubo.objetos[ob].maxY and p[2] >= cubo.objetos[ob].minZ and p[2] <= cubo.objetos[ob].maxZ
                                
                                if(aiDento and menorTT > tt):
                                        menorTT = tt
                                        indMenor = ob   
                        if(indMenor!=-1):
                                image[i, j, 0] = cubo.objetos[indMenor].rgb[0]
                                image[i, j, 1] = cubo.objetos[indMenor].rgb[1]
                                image[i, j, 2] = cubo.objetos[indMenor].rgb[2]     
                                        
        #cv2.imwrite("Z/_saidaX{:03d}.jpg".format(k), image) 
print "pronto"
cv2.imshow("cubo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()