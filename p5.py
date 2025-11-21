from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("image.jpg")

translated_img = img.transform(img.size, Image.AFFINE, (1, 0, 50, 0, 1, 30))

rotaed_img = img.rotate(45)

scaled_img = img.resize((200, 200))

flip_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
flip_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

plt.figure(figsize = (16, 6))

plt.subplot(2, 3, 1)
plt.imshow(translated_img)
plt.title("Translated")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(rotaed_img)
plt.title("Rotate")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(scaled_img)
plt.title("Resize")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(flip_horizontal)
plt.title("Flip Horizontal")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(flip_vertical)
plt.title("Flip Vertical")
plt.axis("off")

plt.show()