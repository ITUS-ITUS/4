import numpy as np
import  cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

img=cv.imread("img2.jpg",cv.COLOR_BGR2GRAY)
img_pil=Image.open("img3.jpg")

fig,axes=plt.subplots(1,2)


#===================Geometric Transformation=========================
#scale
scaled=cv.resize(img,None,fx=0.7,fy=0.7)
##cv.imshow("scaled",scaled)



#rotate  with center using pil
rotated=img_pil.rotate(45,expand=True,fillcolor='white',center=None)
transpose_rotate=img_pil.transpose(Image.Transpose.ROTATE_90)
##transpose_rotate.show()


#rotate with cv
rot180=cv.rotate(img,cv.ROTATE_180)
##cv.imshow("rot180",rot180)


#rotate with cv hard  method
col,row=img.shape[:2]


M=cv.getRotationMatrix2D((col/2,row/2),180,0.3)
rotated_hard=cv.warpAffine(img,M,(col,row))
##cv.imshow("rotated_hard",rotated_hard)


#image cropping
#manual
crop=img[0:2000,0:10000]
##cv.imshow("orig",img)
##cv.imshow("cropped",crop)

#smart
##roi=cv.selectROI('select roi',img)
##x,y,w,h=roi
##cropped=img[y:y+h,x:x+w]
##cv.imshow("smart cropped",cropped)

#==================================================================

#=======================Gray level transfomation=========================

#grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
##cv.imshow("gray",gray)

#from grayscale to negative transformation (white->black, black->white)
neg=255-gray
##cv.imshow("Negative image",neg)

#Logarithmic Transform
c=255/np.log(1+np.max(gray))
log_transform=c*np.log1p(gray)
log_transform=np.array(log_transform,dtype=np.uint8)
##plt.imshow(log_transform,cmap='gray')



#Gamma Transformation

gamma=0.3
c=255/(255**gamma)
gray_norm=gray/255
gamma_transform=c*np.power(gray_norm,gamma)
gamma_transform=np.array(gamma_transform,dtype=np.uint8)
##plt.imshow(gamma_transform,cmap='gray')


#=============================================================

#===============================Edge Detection===========================
#sobel
crack=cv.imread("crack.jpg")
crack_gray=cv.cvtColor(crack,cv.COLOR_BGR2GRAY)
sobelx=cv.Sobel(crack_gray,cv.CV_64F,1,0,ksize=3)
sobely=cv.Sobel(crack_gray,cv.CV_64F,0,1,ksize=3)
sobel=cv.magnitude(sobelx,sobely)
sobel=np.array(sobel,dtype=np.uint8)
##plt.imshow(sobel,cmap='gray')



#Canny
canny=cv.Canny(crack_gray,100,200)
plt.imshow(canny,cmap='gray')


#Prewitt
kernelx=np.array([[-1,0,1],
                  [-1,0,1],
                  [-1,0,1]])
kernely=np.array([[-1,-1,-1],
                  [0,0,0],
                  [1,1,1]])

prewittx=cv.filter2D(crack_gray,-1,kernelx)
prewitty=cv.filter2D(crack_gray,-1,kernely)
prewitt=cv.magnitude(prewittx.astype(np.float32),prewitty.astype(np.float32))
prewitt=np.uint(prewitt)

plt.imshow(prewitt,cmap='gray')



#==============================================================================


#=========================Image segmentation/clustering=======================
#Threshold
_,binary=cv.threshold(gray,128,255,cv.THRESH_BINARY)
##plt.imshow(binary,cmap='gray')


#Edge based-canny/sobel


#Region based
ret,thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.imshow(thresh,cmap='gray')
plt.show()
cv.waitKey(0)
#===========================================================================

 
