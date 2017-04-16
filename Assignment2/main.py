import nn

layerSizes = [2,2,1]
input = [1.0,1.5]
desired = [2.5,1.9]
print('length ', len(desired))
output = [0] * 1
error = 0.0

neuralNet = nn.NeuralNetwork(layerSizes)

for x in range(1000):
    error = neuralNet.trainBP(input,output,0.17,0.1)
    output = neuralNet.run(input,output)

    if x%100 == 0:
        print('Iteration ', x, ' Input: ', input[0], ' output: ', output[0], 'error: ', error)