import copy
import networkx as nx

def contract_edges(G, nodes, new_node, ):

    G2 = nx.MultiGraph()
    G2.add_nodes_from(G.nodes(data=True))
    G2.add_edges_from(G.edges(data=True))
    # Add the node with its attributes
    G2.add_node(new_node)
    # Create the set of the edges that are to be contracted
    cntr_edge_set = G.edges(nodes, data=True)
    edge_set = copy.deepcopy(cntr_edge_set)
    for edge in edge_set:
        if not isinstance(G,nx.MultiGraph):
            source_attr = G.edges[(edge[0], edge[1])]
            if edge[0] in nodes and edge[1] not in nodes:
                key=G2.number_of_edges(new_node,edge[1])
                G2.add_edge(new_node, edge[1],key)
                nx.set_edge_attributes(G2, {(new_node, edge[1],key): source_attr})
            elif edge[1] in nodes and edge[0] not in nodes:
                key=G2.number_of_edges(edge[0],new_node)
                G2.add_edge(edge[0], new_node,key)
                nx.set_edge_attributes(G2, {(edge[0], new_node,key): source_attr})

        else:
            for id in range(G2.number_of_edges(edge[0],edge[1])):
                source_attr = G.edges[(edge[0], edge[1],id)]
                if edge[0] in nodes and edge[1] not in nodes:
                    G2.add_edge(new_node, edge[1],id)
                    nx.set_edge_attributes(G2, {(new_node, edge[1],id): source_attr})
                elif edge[1] in nodes and edge[0] not in nodes:
                    G2.add_edge(edge[0], new_node,id)
                    nx.set_edge_attributes(G2, {(edge[0], new_node,id): source_attr})
    G2.remove_nodes_from(nodes)
    return G2.copy()

def min_edge_cut_multiple_st(G,source_nodes, target_nodes,edge_id=None):
    data = copy.deepcopy(G.edges(data=True))
    nodes = target_nodes
    if len(nodes):
        G1 = G.copy()
        G1 = contract_edges(G1, nodes, 'super_target')
      
    externs = [node for node in G.nodes if node in source_nodes]
  
    G2 = contract_edges(G1.copy(), externs, 'super_entry')
  
    cut_set = nx.minimum_edge_cut(G2, t='super_target', s='super_entry')
    if edge_id:
        final_set = []
        for edge in cut_set:
            a = list(edge)
            for j in range(G2.number_of_edges(a[0], a[1])):
                edge_to_find_id = G2.edges[a[0], a[1], j][edge_id]
                edge_to_find = [edge for edge in data if edge[2][edge_id] == edge_to_find_id]
                final_set.append((edge_to_find[0][0], edge_to_find[0][1]))
    
        return final_set
    else:
      return cut_set
