import numpy as np
import cv2

a = np.ones([300,300,3],dtype='uint8')*255
cv2.line(a,(0,10),(300,10),(0,0,255),5)
cv2.rectangle(a,(50,50),(100,100),(255,0,0),-5)


cv2.imshow('White Background',a)
cv2.waitKey(0)   
cv2.destroyAllWindows()
