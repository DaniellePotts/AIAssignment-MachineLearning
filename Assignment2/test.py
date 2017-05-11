import unittest
import transferFunctions
class TestActivationFunctions(unittest.TestCase):
    def test_sigmoid(self):
        tFunc = transferFunctions.TransferFunctions()
        self.assertEqual(0.9525741268224334,tFunc.sigmoid(3))

    def test_gaussian(self):
        tFunc = transferFunctions.TransferFunctions()
        self.assertEqual(0.00012340980408667956,tFunc.guassian(3))

    def test_rationalSig(self):
        tFunc = transferFunctions.TransferFunctions()
        self.assertEqual(1.3162277660168382,tFunc.rationalSigmoidDerivative(3))