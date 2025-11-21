import cv2
import numpy as np

# Load the image
image = cv2.imread('img3.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image_rgb.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# Define stopping criteria for the cluster formation
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# Apply K-Means clustering
k = 3  # Number of clusters (segments)
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers to uint8
centers = np.uint8(centers)

# Map labels to colors from the centers
segmented_image = centers[labels.flatten()]

# Reshape back to the original image dimensions
segmented_image = segmented_image.reshape(image_rgb.shape)

# Display the original and segmented images
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image (K-Means)', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
