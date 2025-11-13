from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v  
from DataStructures.Graph import edge as e

def new_graph():
    """
    Crea un nuevo grafo dirigido vacío.
    Retorna: Grafo con mapa de vértices inicializado.
    """
    graph = {
        'vertices': mp.new_map() 
    }
    return graph



def insert_vertex(graph, key, value):
    """
    Inserta un vértice en el grafo si no existe.
    """
    if mp.contains(graph['vertices'], key):
        return graph
    new_v = v.new_vertex(key, value)
    mp.put(graph['vertices'], key, new_v)
    return graph


def add_edge(graph, key_u, key_v, weight):
    """
    Agrega un arco dirigido de key_u a key_v con peso weight.
    Requiere que ambos vértices existan.
    """
    if not mp.contains(graph['vertices'], key_u) or not mp.contains(graph['vertices'], key_v):
        return graph  # No agregar si no existen vértices
    vertex_u = mp.get(graph['vertices'], key_u)['value']
    if v.get_edge(vertex_u, key_v) is None:  # No agregar si ya existe
        new_edge = e.new_edge(key_v, weight)
        v.add_adjacent(vertex_u, new_edge)
    return graph

def contains_vertex(graph, key):
    """
    Verifica si el vértice con key existe en el grafo.
    """
    return mp.contains(graph['vertices'], key)

def order(graph):
    """
    Retorna el orden (número de vértices) del grafo.
    """
    return mp.size(graph['vertices'])

def size(graph):
    """
    Retorna el tamaño (número de arcos) del grafo.
    """
    total_edges = 0
    vertices_list = mp.value_set(graph['vertices'])  # Lista de vértices
    for vertex in vertices_list['elements']:
        if vertex is not None:
            adjacents = v.get_adjacents(vertex)
            total_edges += mp.size(adjacents)
    return total_edges
