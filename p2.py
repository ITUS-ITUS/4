from PIL import Image

img = Image.open("image.jpg")
img.show(title = "RGB Image")

gray_img = img.convert("L")
gray_img.show(title = "Gray Scale Image")

resize_img = img.resize((200, 200))
resize_img.show(title = "Resize Iage")