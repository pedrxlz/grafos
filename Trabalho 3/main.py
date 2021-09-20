from collections import defaultdict

class Grafo(object):
    
    def __init__(self, grafo):
        self.grafo_direcionado = grafo
        self.grafo = defaultdict(list)
        self.frequencia = dict()
        self.cria_grafo(grafo) 
        self.arestas = self.get_arestas()
        self.vertices = self.get_vertices()

    def cria_frequencia(self, aux=0):   
        for v in self.grafo:
            for u in self.grafo[v]:
                aux += 1
            self.frequencia[v] = [aux]
            aux = 0
                
    def get_vertices(self, vertices = 0):
        for v in self.grafo_direcionado:
            vertices += 1
        return vertices 
        

    def get_arestas(self, arestas = 0):
        for v in self.grafo_direcionado:
            for u in self.grafo_direcionado[v]:
                arestas += 1
        return arestas

    def mostra_frequencia(self):
        for v in self.frequencia:
            print(v, "=> ", self.frequencia[v], "arestas")


    def cria_grafo(self, grafo):
        for v in grafo:
            for u in grafo[v]:
                self.grafo[v].append(u)
                self.grafo[u].append(v)
        self.cria_frequencia()
        
    def existe_aresta(self, v, u):
        return u in self.grafo[v]    

    def test_euler(self, counterPar=0, counterImpar=0):
        self.g_impar = dict()
        for v in self.frequencia:
            for u in self.frequencia[v]:
                if u % 2 == 0:
                    counterPar += 1
                else:
                    self.g_impar[v] = [u]  
                    counterImpar += 1
        if counterPar == v:
            print ('\nEuleriano')
        elif counterImpar == 2:
            print ('\nSemi-Euleriano')
        elif counterImpar >= 2:
            print ('\nNão Euleriano')
        
        if self.g_impar:
            for v in self.g_impar:
                print(f'Vértice: {v} ==> Grau: {self.g_impar[v]}')
        
            



g1 =   {        1: {3, 6},
                2: {4, 1},
                3: {2, 5},
                4: {3, 7},
                5: {4, 7},
                6: {2, 5},
                7: {1, 6}  
            }

g2 =   {        1: {2, 3, 6},
                2: {3, 4, 6}, 
                3: {4}, 
                4: {5, 7},
                5: {6, 7},
                6: {7}, 
                7: {1}
                
            }

g3 =   {        1: {2, 3, 6},
                2: {3},
                3: {4},
                4: {5},
                5: {6, 7}, 
                6: {7},
                7: {1}
            }  

g4 =   {        1: {2, 3, 6},
                2: {3},
                3: {4},
                4: {5},
                5: {6}, 
                6: {7},
                7: {1}

            }                      


grafo = Grafo(g1)
print(f'\nNúmero de arestas do grafo: {grafo.arestas}\nNúmero de vertices do grafo: {grafo.vertices}')
grafo.test_euler()

grafo2 = Grafo(g2)
print(f'\nNúmero de arestas do grafo: {grafo2.arestas}\nNúmero de vertices do grafo: {grafo2.vertices}')
grafo2.test_euler()

grafo3 = Grafo(g3)
print(f'\nNúmero de arestas do grafo: {grafo3.arestas}\nNúmero de vertices do grafo: {grafo3.vertices}')
grafo3.test_euler()


grafo4 = Grafo(g4)
print(f'\nNúmero de arestas do grafo: {grafo4.arestas}\nNúmero de vertices do grafo: {grafo4.vertices}')
grafo4.test_euler()







 