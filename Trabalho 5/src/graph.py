from collections import defaultdict

class Grafo(object):
    
    def __init__(self, file):
        self.entrada = defaultdict(list)
        self.arvore_dfs = defaultdict(list)
        self.queue = defaultdict(list)
        self.frequencia = dict()
        self.ler_arquivo(file)
        self.grafo = self.cria_grafo(self.entrada)
        self.cria_frequencia()
        self.vertices = self.get_vertices()
        self.arestas = self.get_arestas()
        self.explored = []
        self.pile = []
        
        

    def ler_arquivo(self, file):
        with open(f"Trabalho 5/input/{file}.txt") as f:
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

    def dfs_r(self, vertice):
        self.explored.append(vertice)

        for vizinho in self.grafo[vertice]:
            if vizinho not in self.explored:
                self.arvore_dfs[vertice].append(vizinho)
                self.arvore_dfs[vizinho].append(vertice)
                self.dfs_r(vizinho)
        

    def dfs_p(self, vertice, counter=0, dfs=defaultdict(list)):
        self.pile.append(vertice)
        
        while self.pile:
            current_node = self.pile.pop() 
            counter += 1
            
            if dfs and counter < (self.arestas + 1):
                dfs[current_node] = self.queue[current_node]
            
            if len(self.explored) == 1:
                dfs[self.explored[-1]].append(current_node)
                dfs[current_node].append(self.explored[-1])
            
            if current_node not in self.explored:
                self.explored.append(current_node)
            
                for vizinho in self.grafo[current_node]:
                        self.queue[vizinho].append(current_node)
                        if vizinho not in self.pile:
                            self.pile.append(vizinho)   

        for v in dfs:
            for u in dfs[v]:
                if u not in self.arvore_dfs:
                    self.arvore_dfs[v].append(u)
                    self.arvore_dfs[u].append(v)
        
    def dfs(self, vertex, type):
        if type == 'r':
            self.dfs_r(vertex)
        if type == 'p':
            self.dfs_p(vertex)      

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
