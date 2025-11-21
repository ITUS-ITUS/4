from PIL import Image
import numpy as np
ig = Image.open(r"E:/sahilsem3/DIP/mountain.jpg")
scaled_ig = ig.resize((int(ig.width*1.5),int(ig.height*1.5)))
tx,ty = 50,30
trans_ig = ig.transform(ig.size,Image.AFFINE,(1,0,tx,0,1,ty))
rotate_ig = ig.rotate(45,expand = True)
shear_x,shear_y = 0.5,0.5
sheard_matrix = (1,0.5,0,0.5,1,0)
sheard_ig = ig.transform((int(ig.width*1.5),int(ig.height*1.5)),Image.AFFINE,sheard_matrix)
ig.show(title = "Orignal Image")
scaled_ig.show(title = "Scaled Image")
trans_ig.show(title = "Translated Image")
rotate_ig.show(title = "Rotated Image ")
sheared_ig.show(title = "Sheared Image")
