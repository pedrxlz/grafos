from collections import defaultdict

#grafo1

# grafo =   {     1: {3, 6}, 
#                 2: {4, 1},
#                 7: {1, 6}, 
#                 3: {2, 5},
#                 6: {2, 5},
#                 4: {3, 7},
#                 5: {4, 7}
#             }

#grafo2

# grafo =         {1: {2, 3, 6, 7},
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

grafo = {       1: {2, 3, 6, 7},
                 2: {3},
                 3: {4},
                 6: {5, 7},
                 4: {3, 5}, 
                 }

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

# ================================================================================================================s

contadorDirac = 0

for v in frequencia:
    for u in frequencia[v]:
        if u >= (vertices/2) and vertices >= 3:
            contadorDirac += 1
        
if (contadorDirac == vertices):
    print('O grafo cumpre com os requisitos do teorema de Dirac!')   
else:
    print("O grafo nao cumpre com os requisitos do teorema de Dirac!")             


# ===============================================================================================================