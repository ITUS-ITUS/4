from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

img = Image.open(r"D:/sem-3 AI/DIP/architecture.jpg").convert("L")
dictt = {}

img_matix = np.array(img)
flatten_matrix = img_matix.flatten()
maxi = max(flatten_matrix)
for i in flatten_matrix:
    if i not in dictt.keys():
        dictt[i] = 1
    else:
        dictt[i]+=1
summ = len(flatten_matrix)
dic = {}
sk = 0
for i,j in sorted(dictt.items(),key=lambda x:x[0]):
    pd = j/summ
    sk = pd+sk
    skm = sk * maxi
    dic[i] = round(skm)
neu_img = []
for i in flatten_matrix:
    neu_img.append(dic[i])
print(neu_img)
neu_img_matix = np.array(neu_img).reshape(img_matix.shape).astype(np.uint8)
neu_img = Image.fromarray(neu_img_matix)
fig,axes = plt.subplots(2,2,figsize=(9,9))
axes[0,0].imshow(img)
axes[0,1].imshow(neu_img)
axes[1,0].hist(img_matix)
axes[1,1].hist(neu_img_matix)
plt.show()

