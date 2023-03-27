import numpy as np

class LinierRegression:
    def __init__(self):
        self.X = []
        self.y = []
        self.xy = [] 
        self.data = 0
        self.koefisien = 0



    def XY(self, X, y):
        self.X = X 
        self.y = y
        for i in self.X:
            for j in self.y:
                return self.X * self.y

    def kuadratX(self, X):
        self.X = X
        for i in self.X:
            return self.X ** 2

    def sigmaX(self, X):
        self.X = X
        return sum(self.X)

    def sigmaY(self, y):
        self.y = y
        return sum(self.y)

    def sigmaXY(self, XY):
        self.xy = XY
        return sum(self.xy)

    def sigmaKuadratX(self, X):
        self.X = X
        return sum(self.X)

    def jumlahData(self, jumlah):
        self.data = jumlah
        return len(self.data)

    def coef(self ):
        self.koefisien = ((self.jumlahData(self.X) * self.sigmaXY(self.xy)) - (self.sigmaX(self.X) * self.sigmaY(self.y))) / ((self.jumlahData(self.X) * self.sigmaKuadratX(self.X)) - (self.sigmaX(self.X) * self.sigmaX(self.X)))
        return self.koefisien

    def intercept(self):
        return (self.sigmaY(self.y) / self.jumlahData(self.X)) - (self.coef() * (self.sigmaX(self.X) / self.jumlahData(self.X)))

import pandas as pd

data = pd.read_csv("bensin.csv")

linier = LinierRegression()

x = data["Liter"]
y = data["Kilometer"]

x = np.array([1,2,3])
y = np.array([1,2,3])
xy = linier.XY(x,y)
print(xy)