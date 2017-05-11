import nn
import kmeans
import loadDataSet
import numpy as np
import sofm
import filter;
import tFuncEnum
import datasets

class MachineLearningType:

    data = []
    def __init__(self):
        x=0

    def GetChoice(self):
        machineLTypes = ['Neural Network with Back Propagation', 'K-Means','SOFM']
        for x in range(len(machineLTypes)):
            print x,': ' ,machineLTypes[x]

        print len(machineLTypes) + 1, ': Combination'

        choice = -1
        while int(choice) < 0 or int(choice) > (len(machineLTypes) + 1) - 1:
            choice = int(input('Choose a method by typing the corresponding number'))

        if choice == 2:
            return 2
        else:
            return int(choice)

    def run(self):
        choice = self.GetChoice()
        dataset = self.getDataSet()
        ld = loadDataSet.LoadDataSet()
        data = ld.loadData(dataset)
        if choice == 0:
            self.runNeuralNet(self.filter(data))
        elif choice == 1:
            self.runKMeans(self.filter(data))
        elif choice == 2:
          data = ld.loadData2D(dataset)
          testFil = filter.Filter()
          self.runSOFM(data)

    def runNeuralNet(self,data):
        layerSizes = [1, 10, 1]
        tFuncs = [tFuncEnum.TFuncs.Nothing, tFuncEnum.TFuncs.RationalSigmoid, tFuncEnum.TFuncs.Sigmoid]
        desired = [0.01]
        error = 0.0
        neuralNet = nn.NeuralNetwork(layerSizes, tFuncs)
        input = data
        trainingRate = 0.20
        momentum = 0.5

        output = [0] * layerSizes[len(layerSizes) -1]
        print 'Desired: ', desired
        for x in range(2000):
            error = neuralNet.trainBP(input, output, trainingRate, momentum)
            output = neuralNet.run(input, output)

            if x % 100 == 0:
                print 'Iteration: ', x, ' Input ', input[0], ' Output ', output[0], ' error: ', error;

    def runKMeans(self,data):
        k = kmeans.KMeans()
        k.run(data)
    def runSOFM(selfs,data):
        sf = sofm.SOFM(data)
        sf.run()

    def filter(self,data):
        filterOptions = ["Add Noise","Remove Duplicates","Normalise","Remove Missing or Empty","Stop"];
        x = True
        fil = filter.Filter()
        for x in range(len(filterOptions)):
             print x + 1,": " , filterOptions[x]

        choice = input('Choose a filter')
        if choice != 6:
            print "Chosen Filter: ",filterOptions[choice -1]
        if int(choice) == 1:
            data = fil.addNoise(data)
        elif int(choice) == 2:
            data = fil.removeDuplicates(data)
        elif int(choice) == 3:
            data = fil.normalise(data)
        elif int(choice) == 4:
            data = fil.removeMissingOrEmpty(data)
        else:
              print 'Filtered data: ',data
              return data

        print 'Filtered data: ', data
        return data

    def getDataSet(self):
        choice = 0
        while choice > 2 or choice < 1:
            choice = input('choose a dataset\n1: Iris\n2: Pima-Diabetes')

        if choice == 1:
            return 'iris.csv'
        else:
            return 'raw-pima-indians-diabetes.csv'

