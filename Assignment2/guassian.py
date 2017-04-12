import math
import random


class Guassian:

    def __init__(self):
        print("Guassian")
    def getRandGuassian(self,mean,stdev):
        u,v,s,t = 0
        while u*u + v*v > 1 | (u == 0 & v == 0):
            u = 2*random.random() - 1
            v = 2 * random.random() - 1

        s = u*u + v*v
        t = math.sqrt((-2.0*math.log(s))/s)

        val1 = stdev*u+mean
        val2 = stdev*u+mean

    def guassian(self,mean,stddev):
        val1,val2 = 0.0
        self.getRandGuassian(mean,stddev,val1,val2)
        return val1

    def getGuassian(self):
        return self.guassian(0.0,1.0)