import nn

layerSizes = [4,5,4]



print('length of array',len(layerSizes))
input = [1]
input[0] = 1.0

desired = [1]
desired[0] = 2.5

output = [1]
error = 0.0
y = 0
neuralNet = nn.NeuralNetwork(layerSizes)
