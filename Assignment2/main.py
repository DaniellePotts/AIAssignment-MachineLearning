import nn
import loadDataSet
import numpy as np
import kmeans
layerSizes = [2,2,1]
desired = [2.5,1.9]
print('length ', len(desired))

error = 0.0

neuralNet = nn.NeuralNetwork(layerSizes)

lData = loadDataSet.LoadDataSet()
data = lData.chooseDataSet()
data = np.array(data)

input = [x for x in data if str(x) != 'nan']
output = [0] * len(input)
for x in range(1000):
    error = neuralNet.trainBP(input,output,0.17,0.1)
    output = neuralNet.run(input,output)

    print('Iteration ', x, ' Input: ', input[0], ' output: ', output[0], 'error: ', error)

k = kmeans.KMeans()
k.run(output)