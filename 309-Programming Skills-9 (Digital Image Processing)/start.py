from PIL import Image

img = Image.open(r"C:\Users\khyan\OneDrive\Pictures\Screenshots\Screenshot 2024-03-31 155242.png")
yimg = img.convert("Z")
yimg.show()
