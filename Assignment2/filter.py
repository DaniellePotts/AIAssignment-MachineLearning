import numpy as np

class Filter:
    data = []

    def __init__(self,data):
        self.data = data

    def AddNoise(self):
        noise = np.random.normal(0, 1, 100)
        lst = list(self.data)
        for x in range(len(noise)):
            print(self.data[0])
            lst.append(noise[x])
        return np.array(lst)

    def removeDuplicates(self):
        return list(set(self.data))

    def normalise(self):
        lst = list(self.data)
        norm = [float(i)/sum(lst) for i in lst]
        norm = [float(i)/sum(norm) for i in norm]
        return np.array(norm)