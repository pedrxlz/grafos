from graph import *
import codecs

class Dijkstra(object):

    def __init__(self, grafo: Grafo, origem): 

        controle = {}
        distanciaAtual = {}
        noAtual = {}
        naoVisitados = []
        atual = origem
        noAtual[atual] = 0

        for vertice in grafo.dicionario.keys():
            naoVisitados.append(vertice)   
            distanciaAtual[vertice] = float('inf')
            
        distanciaAtual[atual] = [0, origem]
        
        naoVisitados.remove(atual)
        
        while naoVisitados:
            
            for vizinho, peso in grafo.dicionario[atual]:
                
                if vizinho and peso == 0:
                    break

                else: 
                    pesoCalc = peso + noAtual[atual]
                    
                    if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                        distanciaAtual[vizinho] = [pesoCalc, atual]
                        controle[vizinho] = pesoCalc
          
            if controle == {}: 
                break    
                
            minVizinho = min(controle.items(), key=lambda x: x[1]) 
            atual = minVizinho[0]
            noAtual[atual] = minVizinho[1]
            naoVisitados.remove(atual)
            del controle[atual]

        
        f = codecs.open("Trabalho 6/output/report.txt", 'w', "utf-8")
        for vertice in distanciaAtual:  
            if vertice != origem:
                if distanciaAtual[vertice] == float('inf'):
                    f.write(f"{origem} até {vertice}: \nNão existe caminho.\n\n" )  
                else:
                    f.write(f"{origem} até {vertice}: \nCusto: {distanciaAtual[vertice][0]} \nCaminho: {self.mostra_caminho(distanciaAtual, origem, vertice)}\n\n") 
            else:
                pass
        f.close()
        
                            
    def mostra_caminho(self, distancias,inicio, fim):
            if  fim != inicio:
                return "%s -- > %s" % (self.mostra_caminho(distancias, inicio, distancias[fim][1]), fim)
            else:
                return inicio

grafo = Grafo('G1')
dijkstra = Dijkstra(grafo, 'A')

    