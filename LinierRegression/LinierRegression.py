import numpy as np


class LinearRegression:
    def __init__(self):
        self.X = 0
        self.y = 0
        self.jumlah = 0

    def fit(self,X, y):
        self.X = X
        self.y = y
        self.X = np.array(self.X)
        self.y = np.array(self.y)

    def mean(self, x):
        self.jumlah = x
        return sum(self.jumlah) / len(self.jumlah)

    def slope(self):
        return np.array(self.covariance() / self.variance(self.X)).reshape(1, len(self.X[0]))

    def covariance(self):
        return (sum((self.X - np.mean(self.X))*(self.y - np.mean(self.y)))) / (len(self.X) - 1)

    def variance(self, x):
        return  np.var(x.flatten(), ddof=1)

    def intercept(self):
        return np.array(np.mean(self.y) - self.slope() * self.mean(self.X)).reshape(len(self.X[0]))

    def predict(self, x):
        hasil = self.intercept() + self.slope() * x
        return np.array(hasil)

    def r_squared(self, ytest, yprediksi):
        ytest = np.array(ytest)
        yprediksi = np.array(yprediksi)
        ss_res = sum((ytest - yprediksi) ** 2)  
        ss_tot = sum((ytest - self.mean(ytest))**2)
        hasil = 1 - (ss_res / ss_tot)
        return hasil[0]

    

import pandas as pd
import sklearn.linear_model as lm
import sklearn.model_selection as ms
from sklearn.metrics import r2_score

if __name__ == "__main__":
    data = pd.read_csv("bensin.csv")
    X = data[["Liter"]]
    y = data[["Kilometer"]]

    X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.2)

    model = lm.LinearRegression()
    model.fit(X_train, y_train)
    prediksi1 = model.predict(X_test)
    print(f"slope: {model.coef_}")
    print(f"intercept: {model.intercept_}")
    print(f"r2_squared: {r2_score(y_test, prediksi1)}")
    print(f"prediksi: \n {prediksi1}")

    print()

    model2 = LinearRegression()
    model2.fit(X_train, y_train)
    prediksi2 = model2.predict(X_test)
    print(f"slope: {model2.slope()}")
    print(f"intercept: {model2.intercept()}")
    print(f"r2_squared: {model2.r_squared(y_test, prediksi2)}")
    print(f"prediksi: \n {prediksi2}")

