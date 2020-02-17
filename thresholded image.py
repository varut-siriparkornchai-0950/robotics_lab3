import cv2
import numpy as np

img = cv2.imread('container.jpg', 0)                            #import image and convert to GRAY.SCALE
ret,thresh1 = cv2.threshold(img,85,255,cv2.THRESH_BINARY)       #img, __pixel value under this will be BLACK__, __maximum value of WHITE__
cv2.imshow("Processed image", thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()