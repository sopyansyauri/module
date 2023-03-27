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
    
    def std(self, x):
        self.x = x
    
    def variance(self, x):
        self.x = x
        self.y = [self.mean(self.x)]
        for i in self.x:
                float(i)
                self.hasil = self.x - self.y
                return self.hasil
