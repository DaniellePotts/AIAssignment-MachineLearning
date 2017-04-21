import nn
import kmeans
import loadDataSet
import numpy as np
class MachineLearningType:
    def __init__(self):
        print('AI Machine Learning')

    def GetChoice(self):
        machineLTypes = ['Neural Network with Back Propagation', 'K-Means']
        for x in range(len(machineLTypes)):
            print(x ,': ' ,machineLTypes[x])

        print(len(machineLTypes) + 1, ': Combination')

        choice = -1
        while int(choice) < 0 or int(choice) > (len(machineLTypes) + 1) - 1:
            choice = int(input('Choose a method by typing the corresponding number'))

        if choice == 2:
            return 2
        else:
            return machineLTypes[choice]

    def run(self):
        choice = self.GetChoice()
        lData = loadDataSet.LoadDataSet()
        data = lData.chooseDataSet()
        if choice == 0:
            self.runNeuralNet(data)
        elif choice == 1:
            self.runKMeans(data)
        elif choice == 2:
            result = self.runNeuralNet()
            self.runKMeans(result)


    def runNeuralNet(self,data):
        layerSizes = [2, 3, 2]
        desired = [2.5, 1.9]
        print('length ', len(desired))

        error = 0.0

        neuralNet = nn.NeuralNetwork(layerSizes)
        data = np.array(data)
        input = [x for x in data if str(x) != 'nan']
        print(len(input))
        output = [0] * len(input)
        for x in range(1000):
            error = neuralNet.trainBP(input, output, 0.17, 0.1)
            output = neuralNet.run(input, output)

            if x % 100 == 0:
                print('Iteration ', x, ' Input: ', input[0], ' output: ', output[0], 'error: ', error)

        return output

    def runKMeans(self,data):
        k = kmeans.KMeans()
        data = np.array(data)
        input = [x for x in data if str(x) != 'nan']
        k.run(input)