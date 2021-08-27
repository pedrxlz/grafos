import operator
from collections import defaultdict

grafo = {
        'RS': ['SC'],
        'SC': ['PR'],
        'PR': ['SP', 'MS'],
        'SP': ['MS', 'MG', 'RJ'],
        'MS': ['MT', 'GO', 'MG'],
        'RJ': ['ES', 'MG'],
        'MG': ['GO', 'ES', 'DF'],
        'GO': ['BA'],
        'MT': ['RO', 'PA', 'TO'],
        'ES': ['BA'],
        'DF': ['GO'],
        'BA': ['PE', 'AL', 'PI', 'TO', 'MG'],
        'SE': ['BA', 'AL'],
        'AL': ['PE'],
        'PE': ['CE', 'PI', 'PB'],
        'PI': ['CE', 'TO', 'MA'],
        'TO': ['PA', 'MA'],
        'PA': ['AM', 'RR'],
        'RO': ['AC'],
        'AC': ['AM'],
        'AM': ['RO'],
        'RR': ['AM'],
        'AP': ['PA'],
        'MA': ['PA'],
        'CE': ['PB'],
        'PB': ['RN'],
        'RN': ['CE']
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

print("\nEstado com o maior numero de vizinhos: " + max(frequencia.items(), key=operator.itemgetter(1))[0])

print("\n===============================================================")

print("\nVertices e seus respectivos vizinhos:\n ")
for v in vizinhos:
    print(v, "=> ", vizinhos[v])
    
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

print('\nDensidade do grafo:', arestas/vertices)

print("\n===============================================================")
