from numpy import genfromtxt;
import datasets
class LoadDataSet:
    def __init__(self,):
        print('load-dataset')

    def loadData(self,dSet):
        data = genfromtxt(dSet.value,delimiter=',')
        return data

    def chooseDataSet(self):
        csvfiles = list(map(str, datasets.Datasets))
        enumCsv = list(datasets.Datasets)
        print('choose a dataset')
        for x in range(len(csvfiles)):
            print(x, ': ', csvfiles[x])

        choice = input("")
        #y = datasets.Datasets.value(csvfiles[choice])
        set = self.loadData(dSet=datasets.Datasets.pima)
        return set