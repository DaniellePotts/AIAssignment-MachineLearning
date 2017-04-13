import numpy as np;

class NeuralNetwork:
    layerCount = 0
    inputSize = 0
    layerSize = []

    def __init__(self,lSize):
            self.layerCount = len(lSize) - 1

            self.inputSize = lSize[0]
            self.layerSize = [None] * self.layerCount
            layerOutput = [[None] * self.layerCount,[]]
            layerInput = [[None] * self.layerCount,[]]
            delta = [[None] * self.layerCount,[]]
            biases = [[None] * self.layerCount,[]]
            previousBiasDelta = [[None] * self.layerCount,[]]

            weights = [[None] * self.layerCount,[],[]]
            previousWeightsDelta = [[None] * self.layerCount,[],[]]

            for x in range(self.layerCount):
                self.layerSize[x] = lSize[x+1]

            for x in range(self.layerCount):
                biases[x] = [None] * self.layerSize[x]
                previousBiasDelta[x] = [None] * self.layerSize[x]
                delta[x] = [None] * self.layerSize[x]
                layerOutput[x] = [None] * self.layerSize[x]
                layerInput[x] = [None] * self.layerSize[x]

                weights[x] = [None] * self.layerSize[x]
                previousWeightsDelta[x] = [None] * self.layerSize[x]


            print(previousWeightsDelta)

