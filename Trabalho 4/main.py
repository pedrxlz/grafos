from collections import defaultdict

class Grafo(object):
    
    def __init__(self):
        self.entrada = defaultdict(list)
        self.grafo = defaultdict(list)
        self.frequencia = dict()
        self.vertices = self.ler_arquivo()
        self.arestas = self.get_arestas()
        self.visitados = []
        self.fila = []
        self.arvore_bfs = []
        self.cria_grafo()

    def ler_arquivo(self):
        with open("Trabalho 4/g2.txt") as f:
            vertices = f.readline()
            for line in f:
                (key, val) = line.split()
                self.entrada[key].append(val)
            return vertices

    def cria_frequencia(self, aux=0):   
        for v in self.grafo:
            for u in self.grafo[v]:
                aux += 1
            self.frequencia[v] = [aux]
            aux = 0
                
    def get_vertices(self, vertices = 0):
        for v in self.entrada:
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


    def cria_grafo(self):
        for v in self.entrada:
            for u in self.entrada[v]:
                self.grafo[v].append(u)
                self.grafo[u].append(v)
        self.cria_frequencia()
        
    def existe_aresta(self, v, u):
        return u in self.grafo[v]    

    def bfs(self, vertice):
        self.visitados.append(vertice)
        self.fila.append(vertice)

        while self.fila:
            s = self.fila.pop(0) 
            self.arvore_bfs.append(s) 
        
            for vizinho in self.entrada[s]:
                if vizinho not in self.visitados:
                    self.visitados.append(vizinho)
                    self.fila.append(vizinho)           
    
    
    def get_grau_maximo(self, maior=0):
        for v in self.frequencia:
            for u in self.frequencia[v]:
                if u > maior:
                    maior = u
                    vertMaior = v     
        return vertMaior, maior    

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
                              
   

def report(message):
        with open("Trabalho 4/report.txt", 'r') as r: 
            conteudo = r.readlines()
            conteudo.append(str(message))
            with open("Trabalho 4/report.txt", 'w') as w:
                    w.writelines(conteudo)
        
grafo = Grafo()
    
grafo.bfs('B')

for x in grafo.arvore_bfs:
    report(f'{x} ')

report(f'\nNumero de vertices: {grafo.vertices}Numero de arestas: {grafo.arestas}\nGrau minimo: {grafo.get_grau_minimo()[0]} => [{grafo.get_grau_minimo()[1]}]\nGrau maximo: {grafo.get_grau_maximo()[0]} => [{grafo.get_grau_maximo()[1]}]\nGrau medio: {grafo.get_grau_medio()}')

report('\n\n')




