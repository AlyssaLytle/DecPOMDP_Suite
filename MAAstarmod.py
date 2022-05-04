# Main methods of MAAstar for human and machine
#from DPOMDP_Writer.ACCDPOMDP import ACC_DPOMDP
from ArrayTree import ArrayTree
#from Dlist import Dlistelem, Dlist
import copy
import itertools
from DecPOMDP import decPOMDP

def H(delta, dpomdp):
    #TODO: Write Method
    # H must be an admissible heuristic, 
    # which means it must be an overestimation of the actual expected reward 
    # for a policy
    
    [h_tree, m_tree] = delta
    if h_tree.get_height() == (dpomdp.horizon - 1):
        # If trees are height = horizon - 1, then just return 0 because there is not future to predict
        return 0
    else:
        return 0

def F(delta, dpomdp):
    #TODO: Write Method to compute tree value
    [h_tree, m_tree] = delta
    return dpomdp.get_value(h_tree,m_tree,dpomdp.start_state,0,0) + H(delta, dpomdp)

def prune_by_score(dlist, score):
    #only keep elements with fscore >= input score
    ret_list = []
    for elem in dlist:
        if score >= elem[1]:
            ret_list.append(elem)
    return ret_list

def get_min_score(dlist):
    #returns the minimum fscore that shows up in list
    min = dlist[0][1]
    for elem in dlist:
        if min > elem[1]:
            min = elem[1]
    return min
        

def get_max(dlist, horizon):
    #input dlist and return max fscore tree that hasn't been fully explored
    #if it returns an empty list, this means all trees are fully explored
    max_elem = []
    max_val = dlist[0][1]
    for elem in dlist:
        if elem[1]>=max_val:
            if (elem[0][0].fully_explored(horizon) == False):
                max_val = elem[1]
                max_elem = elem
    return max_elem

def all_k_length(set, k):
    #print("LENGTH:")
    #print(len(set))
    return list(itertools.product(set, repeat=k))

def get_new_trees(roots, agent_name, dpomdp):
    if agent_name == "human":
        action_set = dpomdp.human_actions
        
        print("Finding all possible sets of size " + str(len(dpomdp.human_observations)) + " of children from set of size " + str(len(action_set)) + "...")
        #TODO: modify these methods to be indexed
        #children_not_nodes = all_k_length(action_set, len(edges))
        #print("First input type: ")
        #print(type(action_set))
        #print((type(action_set[0])))
        #action set is a list of tuples
        possible_leaves_one_child = [p for p in list(itertools.product(action_set,repeat=len(dpomdp.human_observations)))]
        #print("second input type")
        #print(type(possible_leaves_one_child))
        #print(type(possible_leaves_one_child[1]))
        #print("Number of branches: " + str(len(dpomdp.human_observations)))
        if len(roots) > 1:
            all_leaf_assignments = [p for p in list(itertools.product(possible_leaves_one_child, repeat=len(roots)))]
        else:
            all_leaf_assignments = possible_leaves_one_child
        print("Number of leaf assignments for human: " + str(len(all_leaf_assignments)))
        print("Size of one leaf assignment: " + str(len(all_leaf_assignments[0])))
        return all_leaf_assignments
    elif agent_name == "machine":
        edges = dpomdp.machine_observations
        action_sets = []
        for obs in edges:
            action_sets.extend([dpomdp.get_allowed_machine_actions(obs)])
        #print("First input type: ")
        #print(type(action_sets))
        #print((type(action_sets[0])))
        print("Getting all combinations of possible machine actions")
        possible_assignments = list(itertools.product(*action_sets))
        #print("Possible machine action assignment:")
        #print("second input type")
        #print(type(possible_assignments))
        #print(type(possible_assignments[0]))
        #print(str(len(possible_assignments)) + " possible action combos. \n Now getting all combinations of leaf assignments.")
        if len(roots) > 1:
            all_leaf_assignments = [p for p in list(itertools.product(possible_assignments, repeat= len(roots)))]
        else:
            all_leaf_assignments = possible_assignments
        #print(str(len(all_leaf_assignments)) + " possible leaf assignments")
        #print(len(all_leaf_assignments[0]))
        return all_leaf_assignments
        #TODO write method that computes all possible trees with limited set

def expand(delta, dpomdp):
    print("Expanding Trees")
    #returns a list of trees and their new f scores
    human_tree, machine_tree = delta
    human_leaves = human_tree.get_leaves()
    machine_leaves = machine_tree.get_leaves()
    human_leaf_assignments = get_new_trees(human_leaves, "human", dpomdp)
    print("num human leaf assignments: " + str(len(human_leaf_assignments)))
    machine_leaf_assignments = get_new_trees(machine_leaves, "machine", dpomdp)
    print("num machine leaf assignments: " + str(len(machine_leaf_assignments)))
    #check values for pruning
    # h_tree = human_tree.add_level(human_leaf_assignments[0], human)
    # m_tree = machine_tree.add_level(machine_leaf_assignments[0])
    # max_val = F([h_tree,m_tree],dpomdp)
    # list_of_deltas = []
    # for leaves in human_leaf_assignments:
    #     h_tree = human_tree.add_level(leaves)
    #     for leaves in machine_leaf_assignments:
    #         m_tree = machine_tree.add_level(leaves)
    #         #prune here
    #         if F([h_tree,m_tree],dpomdp) == max_val:
    #             list_of_deltas.append([[h_tree, m_tree]])
    #         elif F([h_tree,m_tree],dpomdp) > max_val:
    #             list_of_deltas = [[h_tree,m_tree]]
    #             max_val = F([h_tree,m_tree],dpomdp)
    dlist = []
    print("Creating " + str(len(human_leaf_assignments)*len(machine_leaf_assignments)) + " new trees")
    pruned_count = 0
    for leaves in human_leaf_assignments:
        h_tree = human_tree.copy_and_add_level(leaves,dpomdp.human_observations)
        #h_tree.print()
        for leaves in machine_leaf_assignments:
            m_tree = machine_tree.copy_and_add_level(leaves,dpomdp.machine_observations)
            #prune here
            #only include incidents where an accident hasn't happened
            if F([h_tree,m_tree],dpomdp) > dpomdp.costs["unsafe"]:
                dlist.append([[h_tree,m_tree],F([h_tree,m_tree],dpomdp)])
                #print("!!!!!!!!!!!!! Tree kept")
                #print("Value: " + str(F([h_tree,m_tree],dpomdp)))
            else: 
                pruned_count += 1
                print("Number of trees pruned: " + str(pruned_count))
                print(F([h_tree,m_tree],dpomdp))         
    print("Number of new trees: " + str(len(dlist)))
    return dlist

def solve(dPOMDP):
    #input any type of decPOMDP
    human_tree_list = []
    machine_tree_list = []
    init_human_action = dPOMDP.init_actions["human"]
    init_machine_action = dPOMDP.init_actions["machine"]
    human_tree = ArrayTree(len(dPOMDP.human_observations),[init_human_action],[""])
    machine_tree = ArrayTree(len(dPOMDP.machine_observations),[init_machine_action],[""])
    init_set = [human_tree, machine_tree]
    D = [[init_set, F(init_set, dPOMDP)]]
    tree_exp_count = 0
    print("*****************D initialized*****************")
    while len(D) > 0:
        d_star = get_max(D, dPOMDP.horizon)
        #print("DSTAR")
        #print(d_star)
        if (len(d_star) == 0) & (len(D)==1):
            #this means all trees are fully explored and we have one optimal tree left
            print("One optimal tree found.")
            return D
        elif (len(d_star) == 0):
            #this means all trees are fully explored
            print("All trees fully explored. Multiple optimal trees found.")
            return D
        else:
            D.remove(d_star)
            #expand tree list which is d_star[0], THIS RETURNS AN ALREADY PRUNED LIST
            tree_exp_count += 1
            print("Expanding tree number " + str(tree_exp_count))
            d_star_prime_list = expand(d_star[0],dPOMDP)
            #new threshold is d_star prime's minimum
            if get_min_score(d_star_prime_list) > get_min_score(D):
                #if any existing tree has a score less than these new trees, delete it
                prune_by_score(D, get_min_score(d_star_prime_list))
            D.extend(d_star_prime_list)
            print("new length of D: " + str(len(D))) 