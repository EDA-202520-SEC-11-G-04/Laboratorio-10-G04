from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v  
from DataStructures.Graph import edge as e

DEFAULT_LOAD_FACTOR = 0.5
DEFAULT_PRIME = 109345121


def new_graph(order):
    graph = {
        "vertices": mp.new_map(order, DEFAULT_LOAD_FACTOR, DEFAULT_PRIME),
        "num_edges": 0
    }
    return graph


def insert_vertex(my_graph, key_u, info_u):

    adj_map = mp.new_map(3, DEFAULT_LOAD_FACTOR, DEFAULT_PRIME)

    vertex = {
        "key": key_u,
        "value": info_u,
        "adjacents": adj_map
    }

    mp.put(my_graph["vertices"], key_u, vertex)

    return my_graph


def add_edge(graph, key_u, key_v, weight=1.0):

    if not mp.contains(graph["vertices"], key_u):
        raise Exception("El vertice u no existe")

    if not mp.contains(graph["vertices"], key_v):
        raise Exception("El vertice v no existe")

    vertex_u = mp.get(graph["vertices"], key_u)  # <-- direct

    existing_edge = v.get_edge(vertex_u, key_v)

    if existing_edge is None:
        new_edge = e.new_edge(key_v, weight)
        v.add_adjacent(vertex_u, key_v, new_edge)
        graph["num_edges"] += 1
    else:
        existing_edge["weight"] = weight

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
    return graph["num_edges"]

def vertices(graph):
    return mp.key_set(graph["vertices"])

def degree(graph, key_u):
    if not mp.contains(graph["vertices"], key_u):
        raise Exception("El vertice no existe")

    vertex_u = mp.get(graph["vertices"], key_u)
    adj = v.get_adjacents(vertex_u)
    return mp.size(adj)

