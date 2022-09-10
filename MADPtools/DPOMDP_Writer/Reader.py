

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

def trees_equal(tree1, tree2):
    """Returns true if two array trees are equal"""
    same_edges = (tree1.edges == tree2.edges)
    same_nodes = (tree1.nodes == tree2.nodes)
    return (same_edges & same_nodes)

def read_tree(tree):
    """Reads an array and creates a new tree from it"""
    [nb, nodes, edges] = tree
    new_tree = ArrayTree(nb,nodes,edges)
    return new_tree

def write_tree(tree):
    """ Returns a list that describes the tree """
    return [tree.num_branches, tree.nodes, tree.edges]

def read_unbalanced_tree(filename):
    """ Reads a tree in Graphviz format 
    and outputs it in a more readable format"""
    edge_str = ""
    node_str = ""
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        if "->" in line:
            edges = line.split("->")
            start_node = edges[0][:-1]
            edges = edges[1].split(" ")
            end_node = edges[1]
            label = edges[2][8:-4]
            entry = [start_node, end_node, label]
            edge_str += start_node + "," + end_node + "," + label + "-"
        else:
            elem = line.split(" ")
            if(elem):
                if (elem[0][:-1] == "node"):
                    node = elem[0]
                    name = elem[4]
                    entry = [node, name]
                    node_str += node + "," + name + "-"
    return (node_str + ";" + edge_str + "\n")
                
    

