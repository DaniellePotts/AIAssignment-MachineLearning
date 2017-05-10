import csv
import numpy as np

class LoadDataSet:
    def __init__(self,):
        x = 0

    def loadData(self):
        lst = list()
        nums = list()
        with open('iris.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            for row in spamreader:
                lst.append(row)
            for x in range(len(lst)):
                for y in range(len(lst[x])):
                    if self.is_number(lst[x][y]):
                        nums.append(float(lst[x][y]))
        return np.array(nums)

    def loadData2D(self):
        lst = list()
        nums = [[], []]
        with open('raw-pima-indians-diabetes.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')

            for row in spamreader:
                lst.append(row)
            nums = [0] * len(lst)
            for x in range(len(lst)):
                nums[x] = [0] * len(lst[x])
                for y in range(len(lst[x])):
                    if self.is_number(lst[x][y]):
                        nums[x][y] = float(lst[x][y])
        return np.array(nums)

    def is_number(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False