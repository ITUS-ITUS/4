import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("p4.jpg").convert("L")
orig = img.copy()


img_matrix = np.array(img)
img_max = max(img_matrix.flatten())
img_min = min(img_matrix.flatten())


def get_table(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    gray = {}
    for i in matrix.flatten():
        if i not in gray.keys():
            gray[i] = 1
        else:
            gray[i] += 1
    N = sum(gray.values())   

    cdf = 0
    final = {}

    for i in sorted(gray.items(), key=lambda x: x[0]):
        gray_scale, frequency = i
        pdf = frequency / N
        cdf += pdf
        cdf_max = cdf * img_max
        final_pixels_gray = round(cdf_max)
        final[gray_scale] = final_pixels_gray

    for i in range(m):
        for j in range(n):
            pixel = matrix[i][j]
            change = final[pixel]
            matrix[i][j] = change
    return matrix


matrix = get_table(img_matrix)

new_img = Image.fromarray(matrix)


# Create a figure with 1 row, 2 columns
plt.figure(figsize=(10, 5))

# Plot original image
plt.subplot(1, 2, 1)
plt.imshow(orig, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Plot updated (equalized) image
plt.subplot(1, 2, 2)
plt.imshow(new_img, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.tight_layout()
plt.show()
