

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
    value = -1000
    f = open(filename, "r")
    #skip first 3 lines
    if f.readline():
        f.readline()
        f.readline()
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
                    if l[:6] == "Sample":
                        value = l[17:-19]
            else:
                flag = False
        agent1_tree = ArrayTree(agent1_branch_size, nodes, edges) 
        return [agent0_tree, agent1_tree, value]
    else:
        return []

