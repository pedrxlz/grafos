from terminaltables import AsciiTable
from graph import *



def report(message):        
    with open("Trabalho 5/report.txt", 'w') as w:
        w.writelines(str(message))



table_data = [
    ['///', '///'],
    ['Numero de vertices', grafo.vertices],
    ['Numero de arestas', grafo.arestas],
    ['Grau minimo', grafo.get_grau_minimo()[1]],
    ['Grau maximo', grafo.get_grau_maximo()[1]],
    ['Grau medio', grafo.get_grau_medio()],
    ['Caminho arvore', grafo.caminho()]
]
table = AsciiTable(table_data)

report(table.table)

print(grafo.entrada)
print(grafo.vertices)