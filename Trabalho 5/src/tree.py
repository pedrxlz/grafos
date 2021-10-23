from graph import *

class Tree(object):
    
    def __init__(self, entrada):
        self.entrada = entrada
        self.grafo = self.cria_grafo(self.entrada)
                
    def cria_grafo(self, entrada, grafo=defaultdict(list)):
        for v in entrada:
            for u in entrada[v]:
                grafo[v].append(u)
                grafo[u].append(v)
        return grafo


