import operator

grafo = {
        'RS': {'SC'},
        'SC': {'RS', 'PR'},
        'PR': {'SC', 'SP', 'MS'},
        'SP': {'PR', 'MS', 'MG', 'RJ'},
        'MS': {'MT', 'SP', 'GO', 'MG', 'PR'},
        'RJ': {'ES', 'SP', 'MG'},
        'MG': {'SP', 'GO', 'ES', 'MS', 'RJ', 'DF'},
        'GO': {'BA', 'DF', 'MG', 'MS'},
        'MT': {'RO', 'PA', 'TO', 'MS'},
        'ES': {'BA', 'MG', 'RJ'},
        'DF': {'GO', 'MG'},
        'BA': {'PE', 'AL', 'PI', 'GO', 'SE', 'ES', 'TO', 'MG'},
        'SE': {'BA', 'AL'},
        'AL': {'BA', 'PE', 'SE'},
        'PE': {'CE', 'BA', 'AL', 'PI', 'PB'},
        'PI': {'BA', 'PE', 'CE', 'TO', 'MA'},
        'TO': {'MT', 'BA', 'PI', 'PA', 'MA'},
        'PA': {'MT', 'AP', 'TO', 'MA', 'AM', 'RR'},
        'RO': {'AC', 'MT', 'AM'},
        'AC': {'RO', 'AM'},
        'AM': {'RO', 'AC', 'PA', 'RR'},
        'RR': {'AM', 'PA'},
        'AP': {'PA'},
        'MA': {'PA', 'TO', 'PI'},
        'CE': {'PE', 'PI', 'RN', 'PB'},
        'PB': {'RN', 'PE', 'CE'},
        'RN': {'PB', 'CE'}}

i = 0
vizinhos = dict()
for v in grafo:
    for u in grafo[v]:
        i += 1
    vizinhos[v] = [i]
    i = 0

print("\n===============================================================")

print("\nEstado com o maior numero de vizinhos: " + max(vizinhos.items(), key=operator.itemgetter(1))[0])

print("\n===============================================================")

print("\nVertices e seus respectivos vizinhos: ")
print(grafo)

print("\n===============================================================")

print("\nFrequencia do grau de cada vertice: ")
print(vizinhos)

print("\n===============================================================")

vertices = 0
arestas = 0
for v in grafo:
    vertices += 1
    for u in grafo[v]:
        arestas += 1
print('\nDensidade do grafo:', arestas/vertices)

print("\n===============================================================")


