from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

digit = load_digits()
x = digit.data
y = digit.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy Score : ", accuracy_score(y_test, y_pred))
print("Classification Report : ", classification_report(y_test, y_pred))

plt.subplots(2, 5)
plt.imshow(x_test[0].reshape(8, 8), cmap = "gray")
plt.title(f"True: {y_test[0]}\nPred: {y_pred[0]}")
plt.axis("off")

plt.show()