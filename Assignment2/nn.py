import numpy as np;
import guassian
import math
import random

import transferFunctions


class NeuralNetwork:
    layerCount = 0
    inputSize = 0
    layerSize = []
    weights = [[],[],[]]
    biases = [[],[]]
    delta = [[],[]]
    layerInput = [[],[]]
    layerOutput = [[],[]]
    previousBiasDelta = [[],[]]
    previousWeightsDelta = [[],[],[]]
    g = guassian.Guassian()
    def __init__(self,lSize):
            self.layerCount = len(lSize) - 1
            self.inputSize = lSize[0]
            self.layerSize = [None] * self.layerCount
            self.layerOutput = [[None] * self.layerCount,[]]
            self.layerInput = [[None] * self.layerCount,[]]
            self.delta = [[None] * self.layerCount,[]]
            self.biases = [[None] * self.layerCount,[]]
            self.previousBiasDelta = [[None] * self.layerCount,[]]

            self.weights = [[None] * self.layerCount,[],[]]
            self.previousWeightsDelta = [[None] * self.layerCount,[],[]]

            for x in range(self.layerCount):
                self.layerSize[x] = lSize[x+1]

            for x in range(self.layerCount):
                self.biases[x] = [None] * self.layerSize[x]
                self.previousBiasDelta[x] = [None] * self.layerSize[x]
                self.delta[x] = [None] * self.layerSize[x]
                self.layerOutput[x] = [None] * self.layerSize[x]
                self.layerInput[x] = [None] * self.layerSize[x]

                loopVal = 0

                if x == 0:
                    loopVal = self.inputSize
                else:
                    loopVal = self.layerSize[x-1]

                self.weights[x] = [None] * loopVal
                self.previousWeightsDelta[x] = [None] * loopVal

                for y in range(loopVal):
                    self.weights[x][y] = [None] * self.layerSize[x]
                    self.previousWeightsDelta[x][y] = [None] * self.layerSize[x]

            for x in range(self.layerCount):
                for y in range(self.layerSize[x]):
                    self.biases[x][y] = self.g.getGuassian()
                    self.previousBiasDelta[x][y] = 0.0
                    self.layerOutput[x][y] = 0.0
                    self.layerInput[x][y] = 0.0
                    self.delta[x][y] = 0.0

                loopVal = 0
                if x == 0:
                    loopVal = self.inputSize
                else:
                    loopVal = self.layerSize[x -1]

                for y in range(loopVal):
                    for z in range(self.layerSize[x]):
                        self.weights[x][y][z] = self.g.getGuassian()
                        self.previousWeightsDelta[x][y][z] = 0.0

    def run(self,input,output):
        output = [None] * self.layerSize[self.layerCount-1]
        tFunc = transferFunctions.TransferFunctions()
        for x in range(self.layerCount):
            for y in range(self.layerSize[x]):
                sum = 0.0

                loopVal = 0

                if x == 0:
                    loopVal = self.inputSize
                else:
                    loopVal = self.layerSize[x]

                for z in range(loopVal):
                    if x == 0:
                        sum += self.weights[x][z][y] * input[x]
                    else:
                        sum += self.weights[x][z][y] * self.layerOutput[x-1][z]

                sum += self.biases[x][y]
                self.layerInput[x][y] = sum
                self.layerOutput[x][y] = tFunc.sigmoid(sum)

        for x in range(self.layerSize[self.layerCount - 1]):
            output[x] = self.layerOutput[self.layerCount-1][x]


        return output

    def trainBP(self,input,desired,trainingRate,momentum):
        error = 0.0
        sum = 0.0
        weightDelta = 0.0
        biasDelta = 0.0
        tFunc = transferFunctions.TransferFunctions()
        output = [None] * self.layerSize[self.layerCount-1]

        output= self.run(input,output);

        #backpropagate
        for x in reversed(range(self.layerCount - 1)):
            if x == self.layerCount - 1:
                for y in range(self.layerSize[x]):
                    self.delta[x][y] = output[y] - desired[x]
                    error += np.pow(self.delta[x][y],2)
                    self.delta[x][y] = tFunc.sigmoidDerivative(self.layerInput[x][y])

            else:
                for y in range(self.layerSize[x]):
                    sum = 0.0
                    for z in range(self.layerSize[x +1]):
                        sum += self.weights[x+1][y][x]*self.delta[x][z]

                sum *= tFunc.sigmoidDerivative(self.layerInput[x][y])
                self.delta[x][y]=sum

        for x in range(self.layerCount):
            loopVal = 0

            if x == 0:
                loopVal = self.inputSize
            else:
                loopVal = self.layerSize[x-1]

            for y in range(loopVal):
                for z in range(self.layerSize[x]):
                    multiplyAmount = 0
                    if x == 0:
                        multiplyAmount = input[y]
                    else:
                        multiplyAmount = self.layerOutput[x-1][y]

                    weightDelta = trainingRate*self.delta[x][z]*multiplyAmount
                    self.weights[x][y][z] -= weightDelta + momentum*self.previousWeightsDelta[x][y][z]

                    self.previousWeightsDelta[x][y][z] = weightDelta

        for x in range(self.layerCount):
            for y in range(self.layerSize[x]):
                biasDelta = trainingRate*self.delta[x][y]
                self.biases[x][y] -= biasDelta + momentum * self.previousBiasDelta[x][y]
                self.previousBiasDelta[x][y] = biasDelta

        return error