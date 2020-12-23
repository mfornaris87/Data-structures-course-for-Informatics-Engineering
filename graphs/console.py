from graphs.graph import *
from graphs import graph_utils


def test_graph():
    g = Graph()
    g.insert_vertex('A')
    g.insert_vertex('B')
    g.insert_vertex('C')
    g.insert_vertex('D')
    g.insert_vertex('E')
    g.insert_vertex('F')
    g.insert_edge('A', 'B', 368)
    g.insert_edge('A', 'C', 63)
    g.insert_edge('B', 'C', 125)
    g.insert_edge('B', 'E', 150)
    g.insert_edge('B', 'D', 350)
    g.insert_edge('C', 'E', 205)
    g.insert_edge('E', 'D', 110)
    g.insert_edge('E', 'F', 130)
    g.insert_edge('D', 'F', 100)
    g.insert_edge('C', 'F', 600)
    print('Aristas:')
    for i in g.edges():
        print(i.to_string())
    print('Vertices:')
    for x in g.vertices():
        print(x.to_string())

    print('Cantidad de vertices:', g.vertex_count())
    print('Cantidad de aristas:', g.edge_count())
    print('Devuelve la arista de C a E: ', g.get_edge('C', 'E').to_string())
    print('Grado de F: ', g.degree('F'))
    print('Aristas incidentes sobre F:')
    for x in g.incident_edges('F'):
        print(x.to_string())
    print("Demostracion del Algoritmo de Floyd:")
    fl = graph_utils.floyd(g)
    for x in fl:
        for y in g.vertices():
            print(f'{x.to_string()} --> {y.to_string()} : {fl[x][y]}')

    print("Recorrido en profundidad:")
    dfs = {}
    s = g.__contains__('A')
    graph_utils.dfs(g, s, dfs)
    for x in g.vertices():
        print(dfs[x].to_string())

    print("Recorrido a lo ancho:")
    bfs = {}
    s = g.__contains__('A')
    graph_utils.dfs(g, s, bfs)
    for x in g.vertices():
        print(bfs[x].to_string())

    print("Camino desde A hasta B:")
    a = g.__contains__('A')
    f = g.__contains__('F')
    my_path = graph_utils.path(a, f, dfs)
    for i in range(len(my_path)):
        print(my_path[i].to_string())

    print("Dijkstra:")
    src = 'A'
    djk = graph_utils.dijkstra(g, src=src)
    for x in djk:
        print(f'({src}) --> {x.to_string()} : {djk[x]}')

    print("Arbol de expansion minima con Prim:")
    mst = graph_utils.prim(g)
    for x in mst:
        print(x.to_string())

    print("Arbol de expansion minima con Kruskal:")
    mst = graph_utils.kruskal(g)
    for x in mst:
        print(x.to_string())


if __name__ == '__main__':
    test_graph()
