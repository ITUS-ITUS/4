from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

img = Image.open(r"E:/sahilsem3/DIP/mountain.jpg").convert("L")
##img.show()
imimage = np.array(img)/255
h,w = imimage.shape
ksize = 21
sigma = 3.0
ax = np.arange(-(ksize//2),ksize//2+1)
xx,yy = np.meshgrid(ax,ax)
print(xx,"\n",yy)
psf = np.exp(-(xx**2+yy**2)/(2*sigma*sigma))
psf /= psf.sum()
psf_pad = np.zeros_like(imimage)
psf_pad[:ksize,:ksize] = psf
psf_pad = np.roll(np.roll(psf_pad,-ksize//2,axis = 0),-ksize//2,axis = 1)
h_off = np.fft.fft2(psf_pad)
blurred = np.real(np.fft.ifft2(np.fft.fft2(imimage) * h_off))
np.random.seed(0)
noise_sigma = 0.01
g = np.clip(blurred + noise_sigma * np.random.randn(h,w),0,1)
lop = np.array([[0,-1,0],[-1,-1,-1],[0,-1,0]],dtype = np.float32)
p_pad = np.zeros_like(imimage)
p_pad[:3,:3] = lop
p_pad = np.roll(np.roll(p_pad,-1,axis = 0),-1,axis = 1)
p_oft = np.fft.fft(p_pad)
gamma = 0.005
G = np.fft.fft2(g)
den = (np.abs(h_off)**2+gamma*(np.abs(p_oft)**2))
f_hat = (np.conj(h_off)/den)*G
f_cls = np.real(np.fft.ifft2(f_hat))
f_cls = np.clip(f_cls,0,1)
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.imshow(img,cmap="gray")
plt.title("og")
plt.axis("off")
plt.subplot(2,3,2)
plt.imshow(blurred,cmap="gray")
plt.title("blurred")
plt.axis("off")
plt.subplot(2,3,3)
plt.imshow(g,cmap="gray")
plt.title("blurred_noise")
plt.axis("off")
plt.subplot(2,3,4)
plt.imshow(img,cmap="gray")
plt.title("CLS Restoration ")
plt.axis("off")
plt.subplot(2,3,5)
plt.hist((g*255).ravel(),bins = 256)
plt.title("Observed Histogram")
plt.subplot(2,3,6)
plt.hist((f_cls*255).ravel(),bins = 256)
plt.title("Restored Histogram")
plt.tight_layout()
plt.show()


