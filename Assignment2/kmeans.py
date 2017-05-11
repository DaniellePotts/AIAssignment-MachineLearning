import numpy as np
from numpy.random import random


class KMeans:
    def __init__(self):
        x=0

    def run(self,dataset):
     means = dataset
     data = [random() for i in range(10)]
     meansChange = 0.04

     for x in range(len(data)):
        closest_k = 5
        smallest_error = 9999
        for k in enumerate(means):
            error = np.abs(x-k[1])

            if error < smallest_error:
                smallest_error = error
                closest_k - error
                closest_k = k[0]
            means[closest_k] = means[closest_k]*(1-meansChange)+x*(meansChange)
        print('means ', x, ': ', means)