from graph import *
import codecs


g = Grafo('G1')
f = codecs.open("Trabalho 7/output/report.txt", 'w', "utf-8")


def bellmanFord(src):
   
    caminho = []
    dist = [float("Inf")] * g.vertices
    dist[src] = 0
    caminho = [-1] * g.vertices 

    for _ in range(g.vertices - 1):
        for u, v, w in g.grafo:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    caminho[v] = u

    for u, v, w in g.grafo:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    f.write("O grafo possui um ciclo negativo")
                    return

    print(dist, caminho)
    printSolution(dist, caminho)
    printArr(dist)
    

def printArr(dist):
    f.write("\nDistancia do vertice para a origem\n")
    for i in range(g.vertices):
        f.write(f"{i}      {dist[i]}\n")

def printPath(parent, j):
    if parent[j] == -1 :
        f.write(f"{j} --> ")
        return
    printPath(parent , parent[j])
    f.write(f"{j} --> ")

def printSolution(dist, parent):
    f.write("Caminho\n")
    for i in range(1, len(dist)):
        printPath(parent, i)
        f.write('\n')

bellmanFord(0)


    