from colas.cola import Cola
from math import *
from funcionesAuxiliares import *
from colas.cola import *
from colas.colaPrioridades import *


class Grafo:

    def __init__(self, fichero):
        self.n = 0 # Número de nodos
        self.m = 0 # Número de aristas
        self.dirigido = 0 # Grafo dirigido | No dirigido
        self.pesos = None # Grafo con pesos | Sin pesos
        self.listaSucesores = []
        self.listaPredecesores = []

        f = open(fichero)

        linea = f.readline()
        datos = algoritmoFichero(linea)

        if(datos[2] != 0 and datos[2] != 1):
            print("ERROR: NO ha indicado si se trata de un grafo dirigido (1) o no dirigido (0).")
        else:
            self.n = datos[0]
            self.m = datos[1]
            self.dirigido = datos[2]
            aristas = datos[1]
            nodoActual = 0
            listaNodos = [] # Nodos a los que se puede llegar desde el nodo actual
            info = [] # Par nodo origen y nodo destino

            for i in range(self.n):
                self.listaSucesores.append([])
                self.listaPredecesores.append([])

            pesos = 2
            while(pesos != 0 and pesos != 1):
                pesos = int(input("¿Es un grafo con pesos? 0 (No) | 1 (Sí) "))
                self.pesos = pesos
                
            if(pesos == 0):
                while(aristas != 0):
                    linea = f.readline()
                    info = algoritmoFichero(linea)
                    info = [info[0] - 1, info[1] - 1]

                    if (nodoActual == info[0]):
                        listaNodos.append(info[1])
                    elif(aristas - 1 == 0):
                        self.listaSucesores.pop(nodoActual)
                        self.listaSucesores.insert(nodoActual, listaNodos)
                        listaNodos = []
                        listaNodos.append(info[1])
                        self.listaSucesores.pop(info[0])
                        self.listaSucesores.insert(info[0], listaNodos)
                    else:
                        self.listaSucesores.pop(nodoActual)
                        self.listaSucesores.insert(nodoActual, listaNodos)
                        nodoActual = info[0]
                        listaNodos = []
                        listaNodos.append(info[1])

                    if (self.dirigido == 1):
                        listaAux = self.listaPredecesores[info[1]]
                        listaAux.append(info[0])
                        self.listaPredecesores.pop(info[1])
                        self.listaPredecesores.insert(info[1], listaAux)

                    aristas -= 1
            else:
                while(aristas != 0):
                    linea = f.readline()
                    info = algoritmoFichero(linea)
                    info = [info[0] - 1, info[1] - 1, info[2]]

                    if (nodoActual == info[0]):
                        listaNodos.append([info[1], info[2]])
                    elif(aristas - 1 == 0):
                        self.listaSucesores.pop(nodoActual)
                        self.listaSucesores.insert(nodoActual, listaNodos)
                        listaNodos = []
                        listaNodos.append([info[1], info[2]])
                        self.listaSucesores.pop(info[0])
                        self.listaSucesores.insert(info[0], listaNodos)
                    else:
                        self.listaSucesores.pop(nodoActual)
                        self.listaSucesores.insert(nodoActual, listaNodos)
                        nodoActual = info[0]
                        listaNodos = []
                        listaNodos.append([info[1], info[2]])

                    if (self.dirigido == 1):
                        listaAux = self.listaPredecesores[info[1]]
                        listaAux.append([info[0], info[2]])
                        self.listaPredecesores.pop(info[1])
                        self.listaPredecesores.insert(info[1], listaAux)

                    aristas -= 1



    def esDirifido(self):

        if (self.dirigido == 1):
            return True
        else:
            return False


    def infoGrafo(self):

        if(self.dirigido == 1):
            print(f"EL grafo tiene {self.n} nodos, {self.m} aristas y es dirigido.")
        else:
            print(f"EL grafo tiene {self.n} nodos, {self.m} aristas y no es dirigido.")


    def mostrarLista(self, lista): # lista --> 0 = Sucesores / Adyacencia | lista --> 1 = Predecesores

        assert (lista == 0) or (lista == 1), "Tiene que indicar qué lista quiere ver:  (0) Sucesores / Adyacencia (1) Predecesores"

        if(self.pesos == 0):
            if (lista == 0):
                if (self.dirigido == 1):
                    print("\n\nLa lista de sucesores es: \n")
                else:
                    print("\n\nLa lista de adyacencia es: \n")
                
                for i in range(len(self.listaSucesores)):
                    aux = i + 1
                    tam = len(self.listaSucesores[i])
                    print(f"[{aux}]: ", end="")

                    for j in range(tam):
                        aux = self.listaSucesores[i][j]
                        aux += 1
                        print(aux, end="")
                        if(j != tam - 1):
                            print(" | ", end="")

                    if(len(self.listaSucesores[i]) == 0):
                        print("null", end="")

                    print()

            elif (lista == 1):
                print("\n\nLa lista de predecesores es: \n")

                for i in range(len(self.listaPredecesores)):
                    aux = i + 1
                    tam = len(self.listaPredecesores[i])
                    print(f"[{aux}]: ", end=" ")

                    for j in range(tam):
                        aux = self.listaPredecesores[i][j]
                        aux += 1
                        print(aux, end="")
                        if(j != tam - 1):
                            print(" | ", end="")

                    if(len(self.listaPredecesores[i]) == 0):
                        print("null", end="")

                    print()
        else:
            if (lista == 0):
                if (self.dirigido == 1):
                    print("\n\nLa lista de sucesores es: \n")
                else:
                    print("\n\nLa lista de adyacencia es: \n")
                
                for i in range(len(self.listaSucesores)):
                    aux = i + 1
                    tam = len(self.listaSucesores[i])
                    print(f"[{aux}]: ", end="")

                    for j in range(tam):
                        aux = self.listaSucesores[i][j][0]
                        aux += 1
                        print(f" -> {aux} ({self.listaSucesores[i][j][1]})", end="")
                        if(j != tam - 1):
                            print(" | ", end="")

                    if(len(self.listaSucesores[i]) == 0):
                        print("null", end="")

                    print()

            elif (lista == 1):
                print("\n\nLa lista de predecesores es: \n")

                for i in range(len(self.listaPredecesores)):
                    aux = i + 1
                    tam = len(self.listaPredecesores[i])
                    print(f"[{aux}]: ", end=" ")

                    for j in range(tam):
                        aux = self.listaPredecesores[i][j][0]
                        aux += 1
                        print(f" <- {aux} ({self.listaPredecesores[i][j][1]})", end="")
                        if(j != tam - 1):
                            print(" | ", end="")

                    if(len(self.listaPredecesores[i]) == 0):
                        print("null", end="")

                    print()

        


    def dfs(self, i, estado):

        estado[i] = True
        print(f"{i + 1}, ", end="")

        for j in range(len(self.listaSucesores[i])):
            if (estado[self.listaSucesores[i][j][0]] == False):
                self.dfs(self.listaSucesores[i][j][0], estado)
            
            j += 1

    
    def bfs(self, u, estado, distancia):

        distancia[u] = 0

        # Cola
        cola = Cola()
        cola.push(u) # Se mete el nodo

        while(cola.vacia() != True):
            j = cola.pop()
            print(f"{j+1}, ", end="")
            for i in self.listaSucesores[j]:
                if(estado[i[0]] == False):
                    estado[i[0]] = True
                    distancia[i[0]] = distancia[j] + 1
                    cola.push(i[0])
                

    def componentesConexas(self, modo): # modo -> 0 = dfs | modo -> 1 = bfs

        assert (modo == 0) or (modo == 1), "Tiene que indicar en qué modo quiere que funcione:  (0) DFS (1) BFS"

        componentesConexas = 0
        estado = []

        if(modo == 1):
            print("\n\nRecorrido BFS:\n")
            distancia = []

            for i in range(self.n):
                distancia.append(inf)

        else:
            print("\n\nRecorrido DFS:")


        for i in range(self.n):
            estado.append(False)

        for i in range(self.n):

            if (estado[i] == False):
                print(f"\nComponente conexa: {componentesConexas + 1}")
                print("{", end=" ")
                if(modo == 0):
                    self.dfs(i, estado)
                else:
                    self.bfs(i, estado, distancia)
                print("}")
                componentesConexas += 1

        print(f"\nEl número total de componentes conexas es: {componentesConexas}")


    def dijkstra(self, s):
        distancia = [] # [distancia, nodo predecesor]
        visto = [] # True | False

        for i in range(self.n):
            distancia.append([inf, 0])
            visto.append(False)

        distancia[s] = [0, 0]

        # Cola
        cola = ColaPrioridades()
        cola.push([s, distancia[s]]) # Se mete el nodo y la distancia en cola de prioridades

        print("\n\nEl camino mínimo por Dijkstra es: ")
       

        while(cola.vacia() != True):
            u = cola.pop()
            visto[u] = True
            for i in self.listaSucesores[u]:
                salir = False
                if(visto[i[0]] == False):
                    if(distancia[i[0]][0] > distancia[u][0] + i[1]):
                        for j in self.listaPredecesores:
                            if (salir == True):
                                break
                            else:
                                for k in range(len(j)):
                                    if (j[k][1] == i[1]):
                                        predecesor = j[k][0]
                                        salir = True
                                        break
                        distancia[i[0]] = [distancia[u][0] + i[1], predecesor+1]
                        cola.push([i[0], distancia[i[0]]])

        print("\n\nLas distancias son:")
        for i in range(len(distancia)):
            print(f"\n\nNodo {i+1}, distancia total: {distancia[i][0]}")
            if (distancia[i][0] != 0):
                print("\nEl camino a seguir es:\n")
                camino = []
                j = i
                distanciasAux = distancia[j][0]
                camino.append(j)
                while distanciasAux != 0:
                    camino.append((distancia[j][1] - 1))
                    j = (distancia[j][1] - 1)
                    distanciasAux = distancia[j][0]
                    
                cont = len(camino) - 1

                for k in reversed(camino):
                    if (cont == 0):
                        print(f"{k + 1}\n")
                    else:
                        print(f"{k + 1} -->", end=" ")
                    cont -= 1
        

grafo1 = Grafo("./ficherosMuestra/grafo10.gr")

grafo1.mostrarLista(0)
grafo1.mostrarLista(1)

grafo1.componentesConexas(0)
grafo1.componentesConexas(1)

grafo1.dijkstra(0)