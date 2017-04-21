import graphviz as gv;

class GUI:
    def __init__(self):
        print('gui')

    def drawGraph(self):
        g1 = gv.Graph(format='svg')
        g1.node('A')
        g1.node('B')
        g1.edge('A','B')
        print(g1.source)
        filename = g1.render()
        print(filename)