import numpy as np;

class BackPropagationNetwork:
    """a neural network"""
    layerCount = 0
    shape = None
    weights = []

    def __init__(self,layerSize):
        self.layerCount = len(layerSize) - 1 #input layer is just a "buffer" that holds values
        self.shape = layerSize

        #inputs and outputs
        self._layerInput = []
        self._layerOutput = []

        #create weight arrays
        for (l1,l2) in zip(layerSize[:-1],layerSize[1:]):
