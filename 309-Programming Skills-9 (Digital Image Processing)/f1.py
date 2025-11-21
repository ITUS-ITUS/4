from PIL import Image
img = Image.open("C:/Users/TEST/Pictures/bird.jpg")
c = img.convert("L")
c.show()
