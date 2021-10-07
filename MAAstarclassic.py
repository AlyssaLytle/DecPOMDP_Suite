# Main methods of MAAstar for human and machine
from NodeClass import Node
from TreeClass import Tree
from Dlist import Dlistelem, Dlist
import copy
from helper_methods import *

def H(delta):
    #TODO: Write Method
    return 0

def F(delta):
    #TODO: Write Method
    return 0

def get_new_trees(roots, agent):
    action_set = agent.get_action_set()
    edges = agent.get_observation_set()
    num_leaves = len(roots)
    print("Finding all possible sets of size " + str(len(edges)) + " of children from set of size " + str(
        len(action_set)) + "...")
    children_not_nodes = all_k_length(action_set, len(edges))
    all_leaf_assignments = all_k_length(children_not_nodes, num_leaves)
    leaf_assignments = []
    for assignment in all_leaf_assignments:
        condition = False
        leaf_list = []
        for i in range(len(roots)):
            children = assignment[i]
            temp_node = copy.deepcopy(roots[i])
            for j in range(len(children)):
                child = children[j]
                edge = edges[j]
                temp_node.add_child(edge, Tree(Node(child)))
                if (edge[1] == "None") & (child[1]== "Open"):
                    condition = True
                temp_tree = Tree(temp_node)
                leaf_list.append(temp_tree)
        if (condition == False):
            leaf_assignments.append(leaf_list)
    print("Number of new trees: " + str(len(leaf_assignments)))
    print("Number of leaves: " + str(len(leaf_assignments[0])))
    #new_tree = leaf_assignments[0][0]
    #print(new_tree.get_root().get_children())
    return leaf_assignments

def expand(delta):
    print("Expanding Trees")
    #returns a list of trees and their new f scores
    human_tree, machine_tree = delta
    human = self.decpomdp.human
    machine = self.decpomdp.machine
    human_leaves = get_leaves(human_tree)
    print("HUMAN LEAVES:")
    print(human_leaves)
    machine_leaves = get_leaves(machine_tree)
    if (isinstance(human_leaves[0], list)):
        human_leaves = unnest_list(human_leaves)
    if (isinstance(machine_leaves[0], list)):
        machine_leaves = unnest_list(machine_leaves)
    #TODO: get_new_trees method for modified MAA*
    human_leaf_assignments = get_new_trees(human_leaves, human)
    machine_leaf_assignments = get_new_trees(machine_leaves, machine)
    new_human_trees = []
    new_machine_trees = []
    for leaves in human_leaf_assignments:
        #TODO: replace_leaves method in TreeClass.py
        new_tree = replace_leaves(human_tree, leaves)
        new_human_trees += [new_tree]
    for leaves in machine_leaf_assignments:
        new_tree = replace_leaves(machine_tree, leaves)
        new_machine_trees += [new_tree]
    '''Pruning option:
    if (len(new_human_trees)<1000) & (len(new_machine_trees)<1000):
        [human_pruned, machine_pruned] = [new_human_trees, new_machine_trees]
        #[human_pruned, machine_pruned] = self.prune(new_human_trees, new_machine_trees, human, machine)
    elif (len(new_human_trees)<1000):
        human_pruned = new_human_trees
        machine_pruned = random.sample(new_machine_trees, 100)
    elif (len(new_machine_trees)<1000):
        human_pruned = random.sample(new_human_trees, 100)
        machine_pruned = new_machine_trees
    else:
        human_pruned = random.sample(new_human_trees, 100)
        machine_pruned = random.sample(new_machine_trees, 100)
        #[human_pruned, machine_pruned] = self.prune_est(new_human_trees, new_machine_trees, human, machine, 100)
        #[human_pruned, machine_pruned] = [new_human_trees, new_machine_trees]'''

    [human_pruned, machine_pruned] = [new_human_trees, new_machine_trees]
    print("Combining " + str(len(human_pruned)) + " human and " + str(len(machine_pruned)) + " machine trees...")
    list_of_deltas = []
    for htree in human_pruned:
        for mtree in machine_pruned:
            list_of_deltas += [[htree, mtree]]
    #print(list_of_deltas)
    print("Number of combined trees: " + str(len(list_of_deltas)))
    dlist = []
    for elem in list_of_deltas:
        fscore = F(elem)
        dlist.append(Dlistelem(elem, fscore))
    return dlist

def solve(dPOMDP):
    human_tree_list = []
    machine_tree_list = []
    init_human_action = dPOMDP.init_actions["human"]
    init_machine_action = dPOMDP.init_actions["machine"]
    human_actions = [init_human_action]
    machine_actions = [init_machine_action]
    human_tree = Tree(Node(init_human_action))
    machine_tree = Tree(Node(init_machine_action))
    init_set = [human_tree, machine_tree]
    init_D = [Dlistelem(init_set, F(init_set))]
    D = Dlist(init_D)
    print("*****************D initialized*****************")
    while D.not_empty():
        [d_star, fully_explored] = D.get_max() #Gets tree pair that's not fully explored with max F-score.  If all trees are fully explored, fully_explored = True.
        # todo: make sure not to remove a tree if it's been fully explored
        print("D STAR:")
        d_star_treelist = d_star.get_treelist()
        print(d_star_treelist)
        if fully_explored:
            print("All trees fully explored. Multiple optimal trees found.")
            return D
        elif D.length()==1:
            print("One optimal tree found.")
            return D
        else:
            D.remove_from_list(d_star)
            d_star_prime_list = expand(d_star_treelist)
            max_fscore = d_star.get_fscore()
            D.add_list_to_list(d_star_prime_list)
            list_to_add = []
            for d_star_prime in d_star_prime_list:
                fscore = d_star_prime.get_fscore()
                if fscore > max_fscore:
                    D.removebyscore(fscore) #remove all elements in D with lower fscore
                    max_fscore = fscore
                    list_to_add = [d_star_prime]
                elif fscore == max_fscore:
                    list_to_add.append(d_star_prime)
            D.add_list_to_list(list_to_add)
        print("Length of D: " + str(len(D.get_list())))