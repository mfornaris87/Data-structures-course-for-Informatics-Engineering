from collections import deque
from queue import PriorityQueue
import heapq


def dfs(g, s, discovered):
    """
    Algoritmo busqueda en profundidad (Depth First Search)
    :param g: Grafo
    :param s: vertice de partida
    :param discovered: diccionario de Python que corresponde un vertice con la arista que condujo a su descubrimiento
    :return: diccionario discovered conteniendo los vertices y aristas del grafo obtenidos mediante la busqueda en profundidad
    """
    for edge in g.incident_edges(s.element):
        v = edge.opposite(s)
        if v not in discovered:
            discovered[v] = edge
            dfs(g, v, discovered)


def path(u, v, discovered_dfs):
    """
    Reconstruye el camino de u a v, comenzando a revisar el recorrido a partir del vertice v
    :param u: vertice origen
    :param v: vertice destino
    :param discovered_dfs: diccionario Python conteniendo el recorrido en profundidad de un grafo
    :return: una lista con el camino del nodo u a v
    """
    p = []
    if v in discovered_dfs:
        p.append(v)
        walk = v
        while walk is not u:
            edge = discovered_dfs[walk]
            parent = edge.opposite(walk)
            p.append(parent)
            walk = parent
        p.reverse()
    return p


def bfs(g, s, discovered):
    """
    Metodo que ejecuta el algoritmo de busqueda a lo ancho sobre el grafo g empezando por el vertice s
    :param g: Grafo
    :param s: Vertice inicial
    :param discovered: diccionario de Python que contiene todos los vertices y las aristas que permitieron descubrirlos
    :return:
    """
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for edge in g.incident_edges(u.element):
                v = edge.opposite(u)
                if v not in discovered:
                    discovered[v] = edge
                    next_level.append(v)
        level = next_level


def my_min(li):
    """Encuentra el minimo elemento de una lista"""
    result = li[0]
    for i in range(1, len(li)):
        if result[0] > li[i][0]: result = li[i]
    return result


def dijkstra(g, src):
    """
    Algoritmo para encontrar el camino minimo de un nodo al resto de los nodos del grafo
    :param g: grafo
    :param src: nodo origen
    :return: diccionario con todos los vertices del grafo y la distancia desde el vertice origen hasta cada uno de ellos
    """
    s = g.__contains__(src)
    # diccionario que contiene cada vertice y la distancia para llegar hasta el
    distance = {}
    # resultado del algoritmo
    result = {}
    # lista de Python que funcionara como una cola con prioridad
    pqueue = []

    # se inicializa la distancia desde el vertice origen hasta el resto de los vertices del grafo a infinito y hacia el mismo a cero
    for v in g.vertices():
        if v is s:
            distance[v] = 0
        else:
            distance[v] = float('inf')
        # se insertan en la cola con prioridad cada nodo y la distancia hasta el desde el origen, este parametro servira como clave
        # para ordenarlos de menor a mayor en la cola con prioridad
        pqueue.append((distance[v], v))

    # mientas la cola no este vacia
    while len(pqueue) > 0:
        # se extrae la tupla cuya clave sea el minimo de la cola
        u = pqueue.pop(pqueue.index(my_min(pqueue)))
        # se guarda en el resultado el nodo que se extrajo y su distancia
        result[u[1]] = distance[u[1]]
        # para cada arista de los vertices adyacentes al extraido
        for edge in g.incident_edges(u[1].element):
            # se busca el vertice opuesto en la arista que se esta examinando
            v = edge.opposite(u[1])
            # si este vertice no esta en el resultado
            if v not in result:
                weight = edge.weight
                # si la distancia al nodo extraido de la cola mas el peso de la arista que conduce al nodo adyacente
                # es menor que el peso que tenia v en el diccionario de las distancias
                if distance[u[1]] + weight < distance[v]:
                    # se toma la posicion del vertice v dentro de la cola
                    i = pqueue.index((distance[v], v))
                    # se actualiza la distancia de v en el diccionario de las distancias
                    distance[v] = distance[u[1]] + weight
                    # se actualiza la distancia de v en la cola
                    pqueue[i] = (distance[v], v)
    return result


def floyd(g):
    """
    Algoritmo para encontrar caminos minimos en un grafo dirigido y ponderado
    :param g: grafo
    :return: diccionario con las distancias entre cada par de vertices del grafo
    """
    distance = {}
    vertices = g.vertices()
    # para vertice del grafo
    for v in vertices:
        # se crea un diccionario de resultados
        result = {}
        # para cada vertice del grafo
        for u in vertices:
            # se busca la arista que los conecta
            edge = g.get_edge(v.element, u.element)
            # si existe
            if edge is not None:
                # se guarda en el resultado el nodo origen, el destino y el peso de la arista que los conecta
                result[u] = edge.weight
            else:
                # si u y v son iguales el peso es 0
                if v is u:
                    result[u] = 0
                else:
                    # si no hay arista es infinito
                    result[u] = float('inf')
        # se actualiza en el diccionario de distancias la distancia desde cada vertice a cada uno de los restantes
        distance[v] = result
    # por ultimo se comprueba para cada par de vertices si existe algun vertice intermedio que tenga una arista cuya sumatoria
    # de los pesos sea menor que la via conocida para llegar a ellos y se actualiza en el arreglo de distancia si es asi
    for k in vertices:
        for i in vertices:
            for j in vertices:
                weight = distance[i][k] + distance[k][j]
                if distance[i][j] > weight:
                    distance[i][j] = weight
    return distance


def prim(g):
    """
    Algoritmo para encontras arbol de expansion minima en un grafo ponderado y no dirigido
    :param g: grafo
    :return: lista que contiene las aristas que conforman el arbol
    """
    # lista que contendra el arbol de expansion minima
    mst = []
    # diccionario de distancias desde el vertices origen a cada vertice
    distance = {}
    # diccionario que permite ubicar mediante que arista se llega a cada nodo
    pqlocator = {}
    # lista que funcionara como cola con prioridad donde la clave sera la distancia para llevar a un vertice y el valor
    # sera dicho vertice
    pqueue = []

    # para cada vertice del grafo se inicializan las distancias del vertice origen al resto en infinito y a el mismo en cero
    for v in g.vertices():
        if len(distance) == 0:
            distance[v] = 0
        else:
            distance[v] = float('inf')
        # se insertan todos los vertices y sus distancias en las cola
        pqueue.append((distance[v], v))
        # se inicaliza el localizador con todos los nodos del grafo, pero si las aristas que los conectan
        pqlocator[v] = None

    # mientras la cola no este vacia
    while len(pqueue) > 0:
        # sacar la tupla con la distancia minima de la cola
        u = pqueue.pop(pqueue.index(my_min(pqueue)))
        # sacar del localizador la arista que permite llegar a ese vertice
        edge = pqlocator[u[1]]
        # borrar del localizador la entrada de ese vertice
        del pqlocator[u[1]]
        # si la arista no esta vacia insertarla en el arbol de expansion minima
        if edge is not None:
            mst.append(edge)
        # para cada arista que conduce a un vertice adyacente al que se saco de la cola
        for link in g.incident_edges(u[1].element):
            # buscar el vertice opuesto en la ariste
            v = link.opposite(u[1])
            # si el vertice esta en el localizador
            if v in pqlocator:
                # tomar el peso de la arista
                weight = link.weight
                # verificar si este peso es menor que la distancia registrada para el nodo
                if weight < distance[v]:
                    # coger la posicion de la entrada de ese nodo en la cola
                    i = pqueue.index((distance[v], v))
                    # se actualiza la distancia del vertice al peso de la nueva arista
                    distance[v] = weight
                    # se inserta una nueva entrada en la cola para ese vertice con la nueva distancia
                    pqueue[i] = (distance[v], v)
                    # se agrega la arista encontrada al vertice v en el localizador
                    pqlocator[v] = link
    return mst


class Partition:
    # ------------class Position---------------------------------------
    class Position:
        """ Estructura para almacenar conjuntos disjuntos """

        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            """ Crea una nueva posicion al frente de su propio grupo """
            self._container = container  # referencia a la instancia de una particion
            self._element = e
            self._size = 1
            self._parent = self  # convencion para el primer elemento del grupo

        def element(self):
            """ Devuelve el elemento almacenado en la posicion actual """
            return self._element

        @property
        def parent(self):
            return self._parent

        @parent.setter
        def parent(self, value):
            self._parent = value

        @property
        def size(self):
            return self._size

        @size.setter
        def size(self, value):
            self._size = value

    # -----------------------------------------------------------------------------

    def make_group(self, e):
        """Crea un grupo que contiene el nuevo elemento e y devuelve su posicion"""
        return self.Position(self, e)

    def union(self, p, q):
        """ Une los grupos que contienen los elementos p y q si son distintos """
        a = self.find(p)
        b = self.find(q)
        if a is not b:  # solamente los mezcla si estan en grupos distintos
            if a.size > b.size:
                b.parent = a
                a.size += b.size
            else:
                a.parent = b
                b.size += a.size

    def find(self, p):
        """ Encuentra el grupo que contiene a p y devuelve la posicion del primer elemento """
        if p.parent != p:
            p.parent = self.find(p.parent)  # sobreescribe p._parent cuando termina la recursividad
        return p.parent


def kruskal(g):
    mst = []
    pqueue = []
    forest = Partition()
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for edge in g.edges():
        pqueue.append((edge.weight, edge))

    size = g.vertex_count()
    while len(mst) != size - 1 and len(pqueue) > 0:
        # el arbol no se expande y aun hay aristas sin procesar
        min_e = pqueue.pop(pqueue.index(my_min(pqueue)))
        edge = min_e[1]
        weight = min_e[0]
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            mst.append(edge)
            forest.union(a, b)
    return mst
