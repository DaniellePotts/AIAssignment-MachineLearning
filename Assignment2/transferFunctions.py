import math

class TransferFunctions:
    def sigmoid(self,x):
        return 1.0 / (1.0 + math.exp(-x))

    def sigmoidDerivative(self,x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

