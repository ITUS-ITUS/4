import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'E:/sahilsem3/DIP/mountain.jpg',cv2.IMREAD_GRAYSCALE)

sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize = 3)
sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 3)

sobel = cv2.magnitude(sx,sy)
sobel = cv2.convertScaleAbs(sobel)

plt.subplot(1,2,1)
plt.title("Original Image ")
plt.imshow(img,cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Sobel Edge Detection")
plt.imshow(sobel,cmap='gray')
plt.axis('off')

plt.show()
cv2.waitKey(0)
