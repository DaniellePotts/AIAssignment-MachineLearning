import numpy as np

class Filter:

    def __init__(self):
        x =0

    def addNoise(self,data):
        noise = np.random.normal(0, 1, 100)
        lst = list(data)
        for x in range(len(noise)):
            lst.append(noise[x])
        return np.array(lst)

    def addNoise2D(selfs,data):
        noise = np.random.normal(0,1,100)

        lst = list(data)

        for x in range(len(lst)):
            for y in range(len(lst[x])):
                lst[x].insert(noise[x])

        return np.array(lst)

    def removeDuplicates(self,data):
        return list(set(data))

    def normalise(self,data):
        lst = list(data)
        norm = [float(i)/sum(lst) for i in lst]
        norm = [float(i)/sum(norm) for i in norm]
        result = np.array(norm)
        return result

    def removeMissingOrEmpty(self,data):
        lst = list(data)
        index = list()
        for x in range(len(lst)):
            if lst[x] == 0.0:
                index.append(lst[x])

        for x in range(len(index)):
            print index[x]
            lst.remove(index[x])

        return np.array(lst)