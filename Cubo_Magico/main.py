from ray_tracing import *
objetos = []
for i in range(3):
        objetos.append(quadrado([0,i,0], [1,i,0], [1,i+1,0], [1,i,0], i%3 ))
        objetos.append(quadrado([1,i,0], [2,i,0], [2,i+1,0], [2,i,0], (i+1)%3 ))
        objetos.append(quadrado([2,i,0], [3,i,0], [3,i+1,0], [3,i,0], (i+2)%3 ))        

        objetos.append(quadrado([0,0,i], [1,0,i], [0,0,i+1], [1,0,i+1], (i+1)%3 ))         
        objetos.append(quadrado([1,0,i], [2,0,i], [1,0,i+1], [2,0,i+1], (i+2)%3 )) 
        objetos.append(quadrado([2,0,i], [3,0,i], [2,0,i+1], [3,0,i+1], (i+0)%3 )) 

        objetos.append(quadrado([0,0,i], [0,1,i], [0,0,i+1], [0,1,i+1], (i+2)%3 ))         
        objetos.append(quadrado([0,1,i], [0,2,i], [0,1,i+1], [0,2,i+1], (i+0)%3 ))                
        objetos.append(quadrado([0,2,i], [0,3,i], [0,2,i+1], [0,3,i+1], (i+1)%3 ))                
        
        

#q10 = quadrado([0,0,0], [0,1,0], [0,0,1], [0,1,1], [0,255,0]);

#objetos  = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

centroCu = centroCubos(objetos)

nx = 200
ny = 200

l = -5
r = 5
t = 5 
b = -5
e = np.array([3,3,10])

ww = np.round(e/ml.norm_flat(e),4)
uu , vv = buildBases(ww)
image = np.zeros((nx,ny,3))
for i in range(nx):
        for j in range(ny):
                u = l + ((r - l)*(i+1 + 0.5))/nx
                v = b + ((t - b)*(j+1 + 0.5))/ny          
                origin = np.round(np.add(e, np.add(np.multiply(u,uu) ,np.multiply(v,vv))),4)
                direction = -ww
                for ob in range(len(objetos)):
                        tt = np.round(np.divide(np.dot((objetos[ob].p1 - origin), objetos[ob].normal.T) , np.dot(direction, objetos[ob].normal.T)),4)
                        p = np.round(origin + np.multiply(tt, direction),4)
                        aiDento = p[0] >= objetos[ob].minX and p[0] <= objetos[ob].maxX and p[1] >= objetos[ob].minY and p[1] <= objetos[ob].maxY and p[2] >= objetos[ob].minZ and p[2] <= objetos[ob].maxZ
                        if(aiDento):
                                image[i, j, 0] = objetos[ob].rgb[0]
                                image[i, j, 1] = objetos[ob].rgb[1]
                                image[i, j, 2] = objetos[ob].rgb[2]     
cv2.imwrite("saida.jpg", image) 
cv2.imshow("cubo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()