class Vertex:
    """
    Clase vertice que contiene un elemento
    """
    __slots__ = '_element'

    def __init__(self, element):
        self._element = element

    @property
    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return self._element == other.element

    def to_string(self):
        return "(" + str(self.element) + ")"


class Edge:
    """
    Clase arista que contiene el vertice de origen, el de destino y el peso de la arista, que puede ser cero
    """
    __slots__ = '_start', '_end', '_weight'

    def __init__(self, u, v, w=0):
        self._start = u
        self._end = v
        self._weight = w

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def weight(self):
        return self._weight

    def endpoints(self):
        """
        Metodo para devolver los vertices de origen y destino de una arista
        :return: tupla de vertices
        """
        return self._start, self._end

    def opposite(self, v):
        """
        Metodo para encontrar el vertice opuesto a uno dado en una arista
        :param v: vertice
        :return: vertice opuesto al que se le pasa por parametros
        """
        return self._end if self._start is v else self._start

    def __hash__(self):
        return hash((self._start, self._end, self._weight))

    def to_string(self):
        tmp = "" if self._weight == 0 else str(self._weight) + "-"
        return str(self._start.to_string()) + "-" + str(tmp) + str(self._end.to_string())


class Graph:
    """
    Clase grafo representada mediante mapas de adyacencia
    """

    def __init__(self, directed=False, weighted=False):
        # mapa de cada vertice del grafo con sus aristas salientes
        self._outgoing = {}
        # mapa de cada vertice del grafo con sus aristas entrantes si es un digrafo, si esta opcion esta en False es igual a outgoing
        self._incoming = {} if directed else self._outgoing
        # indica si el grafo es dirigido
        self._directed = directed
        # indica si el grafo es ponderado
        self._weighted = weighted
        self._edges = 0

    @property
    def outgoing(self):
        return self._outgoing

    @property
    def incoming(self):
        return self._incoming

    def is_directed(self):
        # es dirigido si ambos son distintos
        return self._incoming is not self._outgoing

    def is_weighted(self):
        """Devuelve verdadero si el grafo es ponderado"""
        return self._weighted

    def vertex_count(self):
        """Devuelve la cantidad de vertices del grafo"""
        return len(self._outgoing)

    def vertices(self):
        """Devuelve una lista con los vertices del grafo"""
        return self._outgoing.keys()

    def edge_count(self):
        """
        Devuelve la cantidad de aristas del grafo
        :return: entero
        """
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total//2

    def edges(self):
        """
        Devuelve una lista con las aristas del grafo
        :return: lista de aristas
        """
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, x, y):
        """
        Devuelve la arista que contenga los dos vertices que se le pasan por parametros
        :param x: string que representa el elemento del vertice origen
        :param y: string que representa el elemento del vertice destino
        :return: arista
        """
        u = self.__contains__(x)
        v = self.__contains__(y)
        return self._outgoing[u].get(v)

    def degree(self, x, outgoing=True):
        """
        Metodo que permite calcular el grado de un vertice
        :param x: vertice
        :param outgoing:
        :return: cantidad de aristas salientes del vertice
        """
        v = self.__contains__(x)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, x, outgoing=True):
        """
        Metodo que permite encontrar los vertices adyacentes a uno dado
        :param x: vertice
        :param outgoing:
        :return: Aristas que conectan a los vertices adyacentes
        """
        v = self.__contains__(x)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def __contains__(self, item):
        """
        Metodo que dado un elemento permite buscar si esta en un vertice del grafo
        :param item: elemento de un nodo
        :return: verdadero si esta contenido en algun vertice del grafo
        """
        for v in self.vertices():
            if item == v.element:
                return v
        return None

    def insert_vertex(self, x=None):
        """
        Metodo para insertar un nuevo vertice al grafo
        :param x: string con el elemento que contendra el vertice
        :return: vertice insertado en el grafo
        """
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, x, y, w=0):
        """
        Metodo que annade una nueva arista al grafo
        :param x: string que representa el elemento del vertice de origen
        :param y: string que representa el elemento del vertice de destino
        :param w: peso de la arista
        :return: el metodo no devuelve nada
        """
        u = self.__contains__(x)
        v = self.__contains__(y)
        e = Edge(u, v, w)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

