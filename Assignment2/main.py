import nn
import guassian

layerSizes = [4,5,4]

input = [1.0]

desired = [2.5]

output = [None] * 1
error = 0.0
neuralNet = nn.NeuralNetwork(layerSizes)
for x in range(1000):
    error = neuralNet.trainBP(input,output,0.17,0.1)
    output = neuralNet.run(input,output)

    if x%100 == 0:
        print('Iteration ', x, '\nInput: ', input[0], ' output: ', output[0], 'error: ', error)