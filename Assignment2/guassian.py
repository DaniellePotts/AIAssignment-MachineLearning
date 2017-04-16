import math
import random
import numpy as np

class Guassian:

    def __init__(self):
        print("Guassian")
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
        t = np.sqrt((-2.0*np.log(s))/s)

        return stdev*u+mean
    def guassian(self,mean,stddev):
        val1 = 0.0
        val2 = 0.0
        val1 =self.getRandGuassian(mean,stddev,val1,val2)
        return val1

    def getGuassian(self):
        return self.guassian(0.0,1.0)