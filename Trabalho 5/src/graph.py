from collections import defaultdict

class Grafo(object):
    
    def __init__(self):
        self.entrada = defaultdict(list)
        # self.grafo = defaultdict(list)
        self.frequencia = dict()
        self.ler_arquivo()
        self.grafo = self.cria_grafo(self.entrada)
        self.cria_frequencia()
        self.vertices = self.get_vertices()
        self.arestas = self.get_arestas()
        self.caminho = []
        self.visitados = []
        self.pilha = []
        self.arvore_dfs = defaultdict(list)
        

    def ler_arquivo(self):
        with open("Trabalho 5/input/G2.txt") as f:
            vertices = f.readline()
            for line in f:
                (key, val) = line.split()
                self.entrada[key].append(val)
            

    def cria_frequencia(self, aux=0):   
        for v in self.grafo:
            for u in self.grafo[v]:
                aux += 1
            self.frequencia[v] = [aux]
            aux = 0
                
    def get_vertices(self, vertices = 0):
        for v in self.grafo:
            vertices += 1
        return vertices 
        

    def get_arestas(self, arestas = 0):
        for v in self.entrada:
            for u in self.entrada[v]:
                arestas += 1
        return arestas

    def mostra_frequencia(self):
        for v in self.frequencia:
            print(v, "=> ", self.frequencia[v], "arestas")


    def cria_grafo(self, entrada, grafo=defaultdict(list)):
        for v in entrada:
            for u in entrada[v]:
                grafo[v].append(u)
                grafo[u].append(v)
        return grafo
        
        
    def existe_aresta(self, v, u):
        return u in self.grafo[v]    

    # def dfs(self, vertice):
    #     self.visitados.append(vertice)

    #     for vizinho in self.grafo[vertice]:
    #         if vizinho not in self.visitados:
    #             self.arvore_dfs[vertice].append(vizinho)
    #             self.dfs(vizinho)

    def dfs(self, vertice):
        self.pilha.append(vertice)
        
        while self.pilha:
            u = self.pilha.pop() 
            if u not in self.visitados:
                self.visitados.append(u)
                if len(self.visitados) > 1:
                    self.arvore_dfs[self.visitados[-1]].append(self.pilha[-1])
                for vizinho in self.grafo[u]:
                    self.pilha.append(vizinho)
                
                
                    


   
                    
            

    # def caminho(self, caminho=[]):
    #     for v in self.arvore_dfs:
    #         for u in self.arvore_dfs[v]:
    #             caminho.append(f'{v} -> {u}')
    #     return caminho
    

    def get_grau_maximo(self, maior=0):
        for v in self.frequencia:
            for u in self.frequencia[v]:
                if u > maior:
                    maior = u
                    vertMaior = v     
        return (vertMaior, maior)    

    def get_grau_minimo(self, menor=1000):
        for f in self.frequencia:
            for g in self.frequencia[f]:
                if g < menor:
                    menor = g
                    vertMenor = f  
        return vertMenor, menor

    def get_grau_medio(self, soma=0):
        for v in self.frequencia:
            for u in self.frequencia[v]:
                soma += u
        return (soma/int(self.vertices))
                              
g = Grafo()
g.dfs('1')
print(g.arvore_dfs)
print(g.visitados)






