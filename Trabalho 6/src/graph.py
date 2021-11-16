from collections import defaultdict

class Grafo(object):
    
    def __init__(self, file):
        self.dicionario = defaultdict(list)
        self.ler_arquivo(file)

    def ler_arquivo(self, file):
        with open(f"Trabalho 6/input/{file}.txt") as f:
            vertices = f.readline()
            for line in f:
                (origem, destino, peso) = line.split()
                self.adicionar_aresta(origem, destino, peso, direcionado=True)
                
    def adicionar_aresta(self, origem, destino, peso, direcionado):
        self.dicionario[origem].append((destino, int(peso)))
        if direcionado == False: 
            self.dicionario[destino].append((origem, int(peso)))
        
    def get_vertices(self, vertices = 0):
        for v in self.dicionario:
            vertices += 1
        return vertices 
        
    def get_arestas(self, arestas = 0):
        for v in self.entrada:
            for u in self.entrada[v]:
                arestas += 1
        return arestas

