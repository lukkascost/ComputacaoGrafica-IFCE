import cv2 
import numpy as np
import time
gamma = 3.0
img = cv2.imread("camel.jpg")
img = img/255.0

imgGamma = np.power(img,1.0/gamma)

imgGamma = imgGamma*255.0
imgGamma = imgGamma.astype(np.uint8)

cv2.imshow("img", imgGamma)

cv2.waitKey(0)
cv2.destroyAllWindows()