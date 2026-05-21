from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as al
from DataStructures.Stack import stack as st
from DataStructures.Graph import digraph as G


def dfs(my_graph, source):
    visited_map = mp.new_map(100, 0.5)

    mp.put(visited_map, source, {
        "marked": True,
        "edge_from": None
    })

    dfs_vertex(my_graph, source, visited_map)

    return visited_map


def dfs_vertex(my_graph, vertex, visited_map):
    adjacents_map = G.adjacents(my_graph, vertex)
    adj_keys = mp.key_set(adjacents_map)

    for i in range(al.size(adj_keys)):
        adj = al.get_element(adj_keys, i)
        if not has_path_to(adj, visited_map):
            mp.put(visited_map, adj, {
                "marked": True,
                "edge_from": vertex
            })
            dfs_vertex(my_graph, adj, visited_map)
            
    return visited_map


def has_path_to(key_v, visited_map):
    return mp.contains(visited_map, key_v)


def path_to(key_v, visited_map):
    if not has_path_to(key_v, visited_map):
        return None

    path = st.new_stack()
    actual = key_v

    while actual is not None:
        st.push(path, actual)

        info = mp.get(visited_map, actual)
        actual = info["edge_from"]

    return path