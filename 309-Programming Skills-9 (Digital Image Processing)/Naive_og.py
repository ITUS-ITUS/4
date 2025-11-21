from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,classification_report
import numpy as np
from PIL import Image,ImageFile
from pathlib import Path 

##iris = load_iris()
##y = iris.target
##X = iris.data

ImageFile.LOAD_TRUNCATED_IMAGES = True

fold = Path(r"E:\sahilsem3\DIP\flower image dataset\flowers")
x = []
y = []
image_files = list(fold.glob("*.jpg"))
print(f"Found{len(image_files)} images.")

for indx,file_path in enumerate(image_files):
    try:
        img = Image.open(file_path).convert("L")
        img = img.resize((64,64))
        x.append(np.array(img).flatten())
        y.append(indx%5)

    except Exception as e:
        prin(f"Skipping corrupted image :{file_path},Error : {e}")

x = np.array(x)
y = np.array(y)

##X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 9)

model = GaussianNB()
model.fit(x,y)
test_img_path = image_files[0]
test_img = Image.open(test_img_path).convert("L")
test_img = test_img.resize((64,64))
test_data = np.array(test_img).flatten().reshape(1,-1)
pred_label = model.predict(test_data)[0]
print(f"Predicted Label for test Image{test_img_path.name} : {pred_label}")

##model = GaussianNB()
##model.fit(X_train,y_train)
y_p = model.predict(x)
print("Accuracy %:",accuracy_score(y,y_p))
##print("Classification Report : \n",classification_report(y_test,y_p,target_names = iris.target_names))

