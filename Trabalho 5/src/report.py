from typing import Tuple
import igraph as ig
from igraph import plot 
from terminaltables import AsciiTable
from graph import *
from tree import *


def tree_plot(graph, x_box, y_box, color, layout_type, root_number):   
    G = ig.Graph(directed=False)
    graph_keys = list(graph.keys())
    G.add_vertices(len(graph_keys))
    graph_edges = []

    for i, key in enumerate(graph_keys):
        for j in graph[key]:
            if not (graph_keys.index(j), i) in graph_edges:
                if (i, graph_keys.index(j)) in graph_edges:
                    pass
                else:
                    graph_edges.append((i, graph_keys.index(j)))
    # print(graph_edges)
    G.add_edges(graph_edges)

    box = (x_box, y_box)
    layout = G.layout(layout_type, root=[root_number]) 
    colors = [color] * len(graph_keys)
    return plot(G, "Trabalho 5/output/Tree.png", layout=layout, bbox = box, vertex_label=graph_keys, vertex_color=colors, vertex_size=40, vertex_label_dist=0, margin=40)

def graph_plot(graph, x_box, y_box, color, layout_type):   
    G = ig.Graph(directed=False)
    graph_keys = list(graph.keys())
    G.add_vertices(len(graph_keys))
    graph_edges = []

    for i, key in enumerate(graph_keys):
        for j in graph[key]:
            if not (graph_keys.index(j), i) in graph_edges:
                if (i, graph_keys.index(j)) in graph_edges:
                    pass
                else:
                    graph_edges.append((i, graph_keys.index(j)))
    # print(graph_edges)
    G.add_edges(graph_edges)

    box = (x_box, y_box)
    layout = G.layout(layout_type) 
    colors = [color] * len(graph_keys)
    return plot(G, "Trabalho 5/output/Graph.png", layout=layout, bbox = box, vertex_label=graph_keys, vertex_color=colors, vertex_size=40, vertex_label_dist=0, margin=40)

def report(message):        
    with open("Trabalho 5/output/report.txt", 'w') as w:
        w.writelines(str(message))



g = Grafo()
g.dfs('4')
t = Tree(g.arvore_dfs)








table_data = [
    ['///', '///'],
    ['Numero de vertices', g.vertices],
    ['Numero de arestas', g.arestas],
    ['Grau minimo', g.get_grau_minimo()[1]],
    ['Grau maximo', g.get_grau_maximo()[1]],
    ['Grau medio', g.get_grau_medio()],
    ['Caminho arvore', g.caminho()]
]
table = AsciiTable(table_data)
report(table.table)


tree_plot(t.grafo, 600, 600, 'green', 'tree', 0)
graph_plot(g.grafo, 600, 600, 'red', 'circle')


print(t.grafo)
print(g.grafo)
