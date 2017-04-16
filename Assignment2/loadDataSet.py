import numpy as np

class LoadDataSet:
    dataSet = ''
    def __init__(self,dataset):
        self.dataSet = dataset

    def loadData(self):
        return np.loadtxt(self.dataSet,delimiter=',')