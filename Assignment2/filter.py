import numpy as np

class Filter:

    def __init__(self):
        print('filtering...')

    def AddNoise(self,data):
        noise = np.random.normal(0, 1, 100)
        lst = list(data)
        for x in range(len(noise)):
            print(data[0])
            lst.append(noise[x])
        return np.array(lst)

    def removeDuplicates(self,data):
        return list(set(data))

    def normalise(self,data):
        lst = list(data)
        norm = [float(i)/sum(lst) for i in lst]
        norm = [float(i)/sum(norm) for i in norm]
        result = np.array(norm)
        return result

    def removeNonNumbers(self,data):
        return np.array(input[~np.isnan(input)])

    def removeMissingOrEmpty(self,data):
        lst = list(data)
        for x in range(len(lst)):
            if lst[x] == 0.0:
                lst.remove(lst[x])

        return np.array(lst)