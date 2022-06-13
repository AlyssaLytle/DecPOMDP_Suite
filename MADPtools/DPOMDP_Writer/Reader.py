

import sys
sys.path.append("..")
from ArrayTree import ArrayTree

def get_node_and_edge(line):
    [edge, node] = line.split("-->")
    if len(edge) > 3:
        edge = edge[1:-2]
    else:
        edge = ""
    node = node[1:-1]
    node = node.split("-")
    return [edge,node]

def get_trees(filename, agent0_branch_size, agent1_branch_size):   
    f = open(filename, "r")
    #skip first 3 lines
    line0 = f.readline()
    if line0 == False:
        return []
    f.readline()
    f.readline()
    flag = True
    edges = []
    nodes = []
    while(flag):
        l = f.readline()
        print("newline")
        print(l)
        if l:
            [edge, node] = get_node_and_edge(l)
            nodes.append(node)
            edges.append(edge)
        else:
            flag = False
    agent0_tree = ArrayTree(agent0_branch_size, nodes, edges)
    flag = True
    edges = []
    nodes = []
    while(flag):
        l = f.readline()
        if l:
            if l[0] == "(":
                [edge, node] = get_node_and_edge(l)
                nodes.append(node)
                edges.append(edge)
        else:
            flag = False
    agent1_tree = ArrayTree(agent1_branch_size, nodes, edges)
    return [agent0_tree, agent1_tree]

