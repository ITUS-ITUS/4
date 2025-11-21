from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

img = Image.open("image.jpg").convert("L")
img_array = np.array(img, dtype = float)

sobel_x = ndimage.sobel(img_array, axis = 0)
sobel_y = ndimage.sobel(img_array, axis = 1)

sobel_edges = np.hypot(sobel_x, sobel_y)
sobel_edges = (sobel_edges / sobel_edges.max()) * 255

sobel_img = Image.fromarray(sobel_edges.astype(np.uint8))

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.imshow(img, cmap="gray")
plt.title("Original Concrete Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(sobel_x, cmap="gray")
plt.title("Sobel X (Vertical Edges)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(sobel_y, cmap="gray")
plt.title("Sobel Y (Horizontal Edges)")
plt.axis("off")

plt.figure()
plt.imshow(sobel_img, cmap="gray")
plt.title("Final Edge Detection (Cracks)")
plt.axis("off")
plt.show()