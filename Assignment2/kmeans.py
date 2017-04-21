from random import random as rand
import numpy as np


class KMeans:
    def __init__(self):
        print('k-means')

    def run(self,dataset):
     means = [rand() for i in range(10)]
     data =  dataset
     param = 0.01

     for x in range(2):
         for y in range(len(dataset[x])):
            closest_k = 0
            smallest_error = 9999
            for k in enumerate(means):
                error = np.abs(x-k[1])

                if error < smallest_error:
                    smallest_error = error
                    closest_k - error
                    closest_k = k[0]
                means[closest_k] = means[closest_k]*(1-param)+x*(param)
         print('means ', x, ': ', means)


