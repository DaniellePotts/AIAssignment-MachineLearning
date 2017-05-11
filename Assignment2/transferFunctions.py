import numpy as np
import tFuncEnum

class TransferFunctions:
    def sigmoid(self,x):
        return 1.0 / (1.0 + np.exp(-x))
    def sigmoidDerivative(self,x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))
    def linear(self,x):
        return x
    def linearDerivative(self,x):
        return 1.0
    def guassian(self,x):
        return np.exp(-np.power(x,2))
    def guassianDerivative(self,x):
        return -2.0 * x * x * self.guassian(x)
    def rationalSigmoid(self,x):
        return x / (1.0 + np.sqrt(1.0 + x * x))
    def rationalSigmoidDerivative(self,x):
        val = np.sqrt(1.0 + x * x)
        return 1.0 / val *(1+val)

    def Evaulate(self,func,x):
        if func == tFuncEnum.TFuncs.Sigmoid:
            return self.sigmoid(x)
        elif func == tFuncEnum.TFuncs.Linear:
            return self.linear(x)
        elif func == tFuncEnum.TFuncs.Gaussian:
            return self.guassian(x)
        elif func == tFuncEnum.TFuncs.RationalSigmoid:
            return self.rationalSigmoid(x)
        elif func == tFuncEnum.TFuncs.Nothing:
            return x
    def EvaulateDerivative(self,func,x):
        if func == tFuncEnum.TFuncs.Sigmoid:
            return self.sigmoidDerivative(x)
        elif func == tFuncEnum.TFuncs.Linear:
            return self.linearDerivative(x)
        elif func == tFuncEnum.TFuncs.Gaussian:
            return self.guassianDerivative(x)
        elif func == tFuncEnum.TFuncs.RationalSigmoid:
            return self.rationalSigmoidDerivative(x)
        elif func == tFuncEnum.TFuncs.Nothing:
            return x

