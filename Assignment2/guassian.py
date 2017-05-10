import numpy as np
class Guassian:

    vals = []
    def __init__(self):
        self.vals = [0] * 2
    def getRandGuassian(self,mean,stdev,val1,val2):
        u = 0
        v = 0
        s = 0
        t = 0

        while True:
            u = 2*np.random.rand() - 1
            v = 2 * np.random.rand() - 1

            if u*u + v*v > 1 or (u == 0 and v == 0):
                break
        s = u*u + v*v
        t = np.sqrt((-2.0 * np.log(s)) / s);

        self.vals[0] = stdev*u+mean
        self.vals[1] = stdev*u+mean
        return self.vals
    def guassian(self,mean,stddev):
        self.vals[0] = 0.0
        self.vals[1] = 0.0
        vals =self.getRandGuassian(mean,stddev,self.vals[0],self.vals[1])
        return self.vals[0]

    def getGuassian(self):
        result= self.guassian(0.0,1.0)
        return result