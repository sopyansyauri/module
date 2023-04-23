import math
class Statistika:
    def __init__(self):
        self.x = []
        self.y = []
        self.hasil = []
        self.jumlah = 0

    def mean(self,x):
        self.jumlah = x
        return sum(self.jumlah) / len(self.jumlah)
    
    
    def variance(self, x):
        self.x = x
        self.x = [x - self.mean(self.x) for x in self.x]
        self.x = [x * x for x in self.x]
        self.x = sum(self.x) / len(self.x)
        return self.x
    
    def standarDeviation(self, x):
        self.x = x
        return math.sqrt(self.variance(self.x))

if __name__ == "__main__":
    import numpy as np

    statistika = Statistika()
    x = [6, 8, 10, 14, 18]
    speed = np.array(x)

    print(f"Mean: {statistika.mean(speed)}")
    print(f"Variance: {statistika.variance(speed)}")
    print(f"Standard Deviation: {statistika.standarDeviation(speed)}")