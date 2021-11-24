from collections import defaultdict

class Grafo(object):
    
    def __init__(self, file):
        self.grafo = []
        self.ler_arquivo(file)

    def ler_arquivo(self, file):
        with open(f"Trabalho 7/input/{file}.txt") as f:
            vertices = f.readline()
            for line in f:
                (origem, destino, peso) = line.split()
                self.adicionar_aresta(int(origem), int(destino), int(peso), direcionado=True)
            self.vertices = int(vertices)
                
    def adicionar_aresta(self, origem, destino, peso, direcionado):
        self.grafo.append([origem, destino, peso])
        if direcionado == False: 
            self.grafo.append([destino, origem, peso])


