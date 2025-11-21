from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("image.jpg").convert("L")
equ_img = ImageOps.equalize(img)

img_array = np.array(img)
equ_array = np.array(equ_img)

plt.figure(figsize = (12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img_array, cmap = "gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.hist(img_array.ravel(), bins = 256, range = (0, 256), color = "gray")
plt.title("Histogram")

plt.subplot(2, 2, 3)
plt.imshow(img_array, cmap = "gray")
plt.title("Equalized")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.hist(equ_array.ravel(), bins = 256, range = (0, 256), color = "gray")
plt.title("Equalized Histogram")


plt.show()