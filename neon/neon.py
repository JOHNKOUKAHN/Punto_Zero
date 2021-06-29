import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from math import sqrt,ceil,floor
import random
color= cv.imread('mk.png')
img = cv.imread('mk.png',0)
edges = cv.Canny(img,10,40)

radio = ceil(( sqrt(pow(color.shape[0],2) + pow(color.shape[1],2)) ) / 2)
centroX = floor(color.shape[1] / 2)
centroY = floor(color.shape[0] / 2)

randomB =int(255 * random.random())
randomG =int(255 * random.random())
randomR =int(255 * random.random())

for i  in range(color.shape[0]):
	for j  in range(color.shape[1]):
		distancia = sqrt(pow(j-centroX,2) + pow(i - centroY, 2))
		color[i,j,0] = color[i,j,0] * (1 - (distancia/radio))
		color[i,j,1] = color[i,j,1] * (1 - (distancia/radio))
		color[i,j,2] = color[i,j,2] * (1 - (distancia/radio))

		'''if(distancia < ceil(color.shape[0])/2):
			if(edges[i,j] != 0): 
				color[i,j,0] = randomB
				color[i,j,1] = randomG
				color[i,j,2] = randomR
		'''	
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)		

for i in range(len(contours)):
	if(sqrt(pow(contours[i][0][0][1]-centroX,2) + pow(contours[i][0][0][0] - centroY, 2)) < floor(radio*0.65)):
		cv.drawContours(color, contours, i , (randomB, randomG, randomR), 3)


#cv.imshow('obscurecida',color)
cv.imwrite('neon.jpg',color)
cv.waitKey(0)
cv.destroyAllWindows()


'''plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

(dist x oscuridad maxima) / radio  '''