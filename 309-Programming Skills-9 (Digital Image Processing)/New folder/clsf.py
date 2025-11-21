import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from scipy.fft import fft2, ifft2

# Read grayscale image
img = Image.open("img.jpg").convert("L")
img = np.array(img, dtype=np.float32)

# Make a simple blur (PSF)
psf = np.ones((5, 5)) / 25  # average blur

# Blur the image
blurred = convolve2d(img, psf, mode='same', boundary='wrap')

# CLSF function
def clsf(blurred, psf, gamma):
    H = fft2(psf, s=blurred.shape)      # Fourier of PSF
    G = fft2(blurred)                   # Fourier of blurred image
    P = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])  # Laplacian
    P = fft2(P, s=blurred.shape)        # Fourier of Laplacian
    
    H_conj = np.conj(H)
    F_hat = (H_conj / (np.abs(H)**2 + gamma * np.abs(P)**2)) * G
    restored = np.abs(ifft2(F_hat))
    return restored

# Apply CLSF
restored = clsf(blurred, psf, gamma=1e-10)

# Plot images
plt.figure(figsize=(12,8))

plt.subplot(2,3,1), plt.imshow(img, cmap='gray'), plt.title("Original")
plt.subplot(2,3,2), plt.imshow(blurred, cmap='gray'), plt.title("Blurred")
plt.subplot(2,3,3), plt.imshow(restored, cmap='gray'), plt.title("Restored")

# Plot histograms
plt.subplot(2,3,4), plt.hist(img.ravel(), bins=256, color='black'), plt.title("Original Histogram")
plt.subplot(2,3,5), plt.hist(blurred.ravel(), bins=256, color='black'), plt.title("Blurred Histogram")
plt.subplot(2,3,6), plt.hist(restored.ravel(), bins=256, color='black'), plt.title("Restored Histogram")

plt.tight_layout()
plt.show()
