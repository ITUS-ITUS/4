from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("L")
img_array = np.array(img)


segmented = np.where(img_array > 128, 255, 0)

segmented_img = Image.fromarray(segmented.astype(np.uint8))

plt.figure(figsize = (10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap = "gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(segmented_img, cmap = "gray")
plt.title("Segmented Image")
plt.axis("off")

plt.show()
