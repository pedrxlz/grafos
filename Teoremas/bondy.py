from collections import defaultdict

#grafo1

grafo =   {   1: {3, 6}, 
                2: {4, 1},
                7: {1, 6}, 
                3: {2, 5},
                6: {2, 5},
                4: {3, 7},
                5: {4, 7}
            }

#grafo2

# grafo = {1: {2, 3, 6, 7},
#                  2: {3, 4, 6}, 
#                  3: {4}, 
#                  6: {5, 7}, 
#                  7: {4, 5},
#                  4: {5},
#                 }

#grafo3

# grafo = {1: {2, 3, 6, 7}, 
#                 2: {3}, 
#                 3: {4},
#                 6: {5, 7},
#                 7: {5},
#                 4: {5}, 
#                 }

#grafo4

# grafo = {1: {2, 3, 6, 7},
#                  2: {3},
#                  3: {4},
#                  6: {5, 7},
#                  4: {3, 5}, 
#                  }


i = 0
vizinhos = defaultdict(list)
for v in grafo:
    for u in grafo[v]:
        vizinhos[v].append(u)
        vizinhos[u].append(v)
   
g = 0
frequencia = dict()
for v in vizinhos:
    for u in vizinhos[v]:
        g += 1
    frequencia[v] = [g]
    g = 0        
        
    
print("\n===============================================================")

print("\nFrequencia do grau de cada vertice: ")
print()
for v in frequencia:
    print(v, "=> ", frequencia[v], "arestas")

print("\n===============================================================")

vertices = 0
arestas = 0
for v in grafo:
    vertices += 1
    for u in grafo[v]:
       arestas += 1


def existeAresta(v, u):
    return u in vizinhos[v]


print("\n===============================================================")

print("\nVertices e seus respectivos vizinhos:\n ")
for v in vizinhos:
    print(v, "=> ", vizinhos[v])
    
print("\n===============================================================")


adjacentes = 0
naoAdjacentes = 0
listaNaoAdjacente = []

for v in vizinhos:
    for u in vizinhos:
        if u != v:
            if existeAresta(v, u):
                adjacentes += 1
            else:
                if not [u, v] in listaNaoAdjacente:
                    listaNaoAdjacente.append([v, u])
                else:
                    pass
                naoAdjacentes += 1
        else:
            pass

print('\nSoma de vizinhos adjacentes', adjacentes)
print('\nSoma de vizinhos não adjacentes', naoAdjacentes)

print("\n===============================================================")

print('\nLista de pares não adjacentes:\n')
print(listaNaoAdjacente)




print("\n===============================================================")


b = 0
contador = 1
frequenciaBondy = dict()

while (contador < 8):
    for v in range(len(listaNaoAdjacente)):
        if (contador == listaNaoAdjacente[v][0]) or (contador == listaNaoAdjacente[v][1]): 
            b += 1
    frequenciaBondy[contador] = [b]
    b = 0  
    contador += 1

print("\n===============================================================")

print("\nFrequencia do grau de cada vertice: ")
print()
for v in frequenciaBondy:
    print(v, "=> ", frequenciaBondy[v], "arestas")

print("\n===============================================================")


def verificaBondy():
    ore = 0
    indice = 0
    for v in listaNaoAdjacente:
            if sum(frequenciaBondy[listaNaoAdjacente[indice][0]] + frequenciaBondy[listaNaoAdjacente[indice][1]]) >= vertices:
                ore += 1
                indice += 1
            else:
                pass
    
    if ore == len(listaNaoAdjacente):
        print('O grafo cumpre com os requisitos do teorema de Bondy & Chvatal!')
    else:
        print("O grafo nao cumpre com os requisitos do teorema de Bondy & Chvatal!")

print("\n===============================================================\n")

verificaBondy()