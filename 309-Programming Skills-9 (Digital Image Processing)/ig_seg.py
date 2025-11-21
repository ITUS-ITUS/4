import cv2

img = cv2.imread(r"E:/sahilsem3/DIP/mountain.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
seg_img = cv2.Canny(img,160,255,4)

cv2.imshow("OG Image : ",img)
cv2.imshow(f"Segmented Image : ",seg_img)

cv2.waitKey(0)
