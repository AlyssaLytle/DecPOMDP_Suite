import itertools
from builtins import range, len, isinstance, list
#from cvxopt import matrix
import csv

# import numpy as np



# def unnest_list(l):
#     #print("L")
#     #print(l)
#     i = l[0]
#     if isinstance(i, list):
#         if len(l) <= 1:
#             return unnest_list(i)
#         else:
#             return unnest_list(i) + unnest_list(l[1:])
#     elif len(l) <= 1:
#         new_arr = [i]
#         return new_arr
#     else:
#         return [i] + unnest_list(l[1:])

# def unnest_list_1_level(l):
#     new_list = []
#     for elem in l:
#         if isinstance(elem, list):
#             new_list.append(elem[0])
#         else:
#             new_list.append(elem)
#     return new_list


# def clean(inp_string):
#     new_elem = ""
#     for x in inp_string:
#         if (x != "'") & (x != " ") & (x != '"'):
#             new_elem += x
#     new_elem.replace(' ', '')
#     return new_elem

# def str_array_to_tree(inp_array):
#     tree = []
#     for x in inp_array:
#         if len(x)>1:
#             new_elem = x.split(':')
#             tree += [new_elem]
#     print(tree[0])
#     lvl, action = tree[0]
#     new_tree = tree[1:]
#     # print("Num items: " + str(len(new_tree)))
#     top_level = np.int(lvl)
#     edges = []
#     children = []
#     for x in range(len(new_tree)):
#         # print("New Tree:")
#         temp_tree = new_tree[x]
#         # print(temp_tree)
#         lev = temp_tree[0]
#         edge = temp_tree[1]
#         print("Edge:")
#         print(edge)
#         temp_action = temp_tree[2]

#         # print(temp_elem)
#         # print("Elem: " + str(temp_elem))

#         level = np.int(lev)
#         if level == (top_level + 1):
#             edges.append(str_to_array_joint_tree(edge))
#             print("Clean edge: ")
#             print(str_to_array_joint_tree(edge))
#             sub_tree = new_tree[x:]
#             children.append(str_to_joint_tree_rec(sub_tree))
#     new_root = Node(str_to_array_joint_tree(action), edges, children)
#     # print(edges)
#     # print(children)
#     ret_tree = Tree(new_root)
#     return ret_tree



# def str_to_array(string_array):
#     string_array = string_array.replace(']','').replace('[','')
#     new_list = string_array.split(',')

#     elem1 = np.int(clean(new_list[0]))
#     elem2 = clean(new_list[1])

#     return ([elem1, elem2])

# def str_to_array_joint_tree(string_array):
#     string_array = string_array.replace(']', '').replace('[', '')
#     new_list = string_array.split(',')

#     elem1 = np.int(clean(new_list[0]))
#     elem2 = clean(new_list[1])
#     elem3 = np.int(clean(new_list[2]))
#     elem4 = clean(new_list[3])

#     return ([[elem1, elem2],[elem3, elem4]])

# def output_tree_list(treelist, filename):
#     with open(filename, mode='w') as writefile:

#         for tree in treelist:
#             writefile.write(tree.tree_to_str())
#             writefile.write('new_tree \n')


# def output_short_tree_list(treelist, filename):
#     with open(filename, mode='w') as writefile:

#         for tree in treelist:
#             writefile.write(tree.tree_to_short_str())
#             writefile.write('new_tree \n')


# def read_tree_list(filename):
#     with open(filename, 'r') as fd:
#         tree_list = []
#         reader = csv.reader(fd, delimiter=':')
#         tree = []
#         for row in reader:
#             #print(row)
#             if row == ['new_tree ']:
#                 tree_list.append(tree)
#                 tree = []
#             else:
#                 tree.append(row)
#         tree_list.append(tree)
#     return tree_list

# def read_policy_tree(filename):
#     with open(filename, 'r') as fd:
#         reader = csv.reader(fd, delimiter=':')
#         tree = []
#         for row in reader:
#             #print(row)
#             tree.append(row)
#     return tree


# def remove_from_tree(tree, idx):
#     new_tree = tree[:idx] + tree[idx+1:]
#     return new_tree

# def str_to_joint_tree(tree):
#     lvl, action = tree[0]
#     #print("Level")
#     #print(lvl)
#     #print("Action")
#     #print(action)
#    # print("Num items: " + str(len(tree)))
#     new_tree = tree[1:]
#     #print("Num items: " + str(len(new_tree)))
#     top_level = np.int(lvl)
#     edges = []
#     children = []
#     for x in range(len(new_tree)):
#         #print("New Tree:")
#         temp_tree = new_tree[x]
#         #print(temp_tree)
#         lev = temp_tree[0]
#         edge = temp_tree[1]
#         temp_action = temp_tree[2]


#         # print(temp_elem)
#         # print("Elem: " + str(temp_elem))

#         level = np.int(lev)
#         if level == (top_level + 1):
#             edges.append(str_to_array_joint_tree(edge))
#             sub_tree = new_tree[x:]
#             children.append(str_to_joint_tree_rec(sub_tree))
#     new_root = Node(str_to_array_joint_tree(action), edges, children)
#     #print(edges)
#     #print(children)
#     ret_tree = Tree(new_root)
#     return ret_tree

# def str_to_joint_tree_rec(tree):
#     while len(tree)> 0:
#         lvl,edge,action = tree[0]
#         #print("Level")
#         #print(lvl)
#         #print("Observation")
#         #print(edge)
#         #print("Action")
#         #print(action)
#         top_level = np.int(lvl)
#         new_root = Node(action)
#         edges = []
#         children = []
#         new_tree = tree[1:]
#         for x in range(len(new_tree)):
#             lvl,edge,temp_action = new_tree[x]
#             print("Edge Rec: ")
#             print(edge)
#             #print(temp_elem)
#             level = np.int(lvl)
#             if level == top_level:
#                 new_root = Node(str_to_array_joint_tree(action), edges, children)
#                 ret_tree = Tree(new_root)
#                 return ret_tree
#             elif (level == top_level+1):
#                 edges.append(str_to_array_joint_tree(edge))
#                 print("Clean Edge Rec: ")
#                 print(str_to_array_joint_tree(edge))
#                 sub_tree = new_tree[x:]
#                 children.append(str_to_tree_rec(sub_tree))
#         new_root = Node(str_to_array_joint_tree(action), edges, children)
#         print("Action")
#         print(action)
#         print("New Action")
#         print(str_to_array_joint_tree(action))
#         ret_tree = Tree(new_root)
#         return ret_tree

# def str_to_tree(tree):
#     lvl, action = tree[0]
#     #print("Num items: " + str(len(tree)))
#     #print(elem)
#     new_tree = tree[1:]
#     #print("Num items: " + str(len(new_tree)))
#     top_level = np.int(lvl)
#     edges = []
#     children = []
#     for x in range(len(new_tree)):
#         #print("New Tree:")
#         temp_tree = new_tree[x]
#         #print(temp_tree)
#         lev = temp_tree[0]
#         edge = temp_tree[1]
#         temp_action = temp_tree[2]

#         #print(temp_elem)
#         #print("Elem: " + str(temp_elem))

#         level = np.int(lev)
#         if level == (top_level+1):
#             edges.append(str_to_array(edge))
#             sub_tree = new_tree[x:]
#             children.append(str_to_tree_rec(sub_tree))
#     new_root = Node(str_to_array(action),edges,children)
#     ret_tree = Tree(new_root)
#     return ret_tree

# def decode(elem):
#     number, encoded_elem = elem.split("-")
#     int_num = np.int(number)
#     if encoded_elem == "A":
#         str_elem = "Information"
#     elif encoded_elem == "B":
#         str_elem = "None"
#     elif encoded_elem == "C":
#         str_elem = "Open"
#     elif encoded_elem == "D":
#         str_elem = "Wait"
#     elif encoded_elem == "E":
#         str_elem = "Communicate"
#     elif encoded_elem == "F":
#         str_elem = "DontCommunicate"
#     else:
#         print("ERROR! Couldn't decode" + encoded_elem)
#         str_elem = ""
#     return [int_num, str_elem]


# def short_str_to_tree(tree):
#     lvl, action = tree[0]
#     #print("Num items: " + str(len(tree)))
#     #print(elem)
#     new_tree = tree[1:]
#     #print("Num items: " + str(len(new_tree)))
#     top_level = np.int(lvl)
#     edges = []
#     children = []
#     for x in range(len(new_tree)):
#         #print("New Tree:")
#         temp_tree = new_tree[x]
#         #print(temp_tree)
#         lev = temp_tree[0]
#         edge = temp_tree[1]
#         temp_action = temp_tree[2]

#         #print(temp_elem)
#         #print("Elem: " + str(temp_elem))

#         level = np.int(lev)
#         if level == (top_level+1):
#             edges.append(decode(edge))
#             sub_tree = new_tree[x:]
#             children.append(short_str_to_tree_rec(sub_tree))
#     new_root = Node(decode(action),edges,children)
#     ret_tree = Tree(new_root)
#     return ret_tree

# def short_str_to_tree_rec(tree):
#     while len(tree)> 0:
#         lvl,edge,action = tree[0]
#         top_level = np.int(lvl)
#         new_root = Node(action)
#         edges = []
#         children = []
#         new_tree = tree[1:]
#         for x in range(len(new_tree)):
#             lvl,edge,temp_action = new_tree[x]
#             #print(temp_elem)
#             level = np.int(lvl)
#             if level == top_level:
#                 new_root = Node(decode(action), edges, children)
#                 ret_tree = Tree(new_root)
#                 return ret_tree
#             elif (level == top_level+1):
#                 edges.append(decode(edge))
#                 sub_tree = new_tree[x:]
#                 children.append(str_to_tree_rec(sub_tree))
#         new_root = Node(decode(action), edges, children)
#         ret_tree = Tree(new_root)
#         return ret_tree


# def str_to_tree_rec(tree):
#     while len(tree)> 0:
#         lvl,edge,action = tree[0]
#         top_level = np.int(lvl)
#         new_root = Node(action)
#         edges = []
#         children = []
#         new_tree = tree[1:]
#         for x in range(len(new_tree)):
#             lvl,edge,temp_action = new_tree[x]
#             #print(temp_elem)
#             level = np.int(lvl)
#             if level == top_level:
#                 new_root = Node(str_to_array(action), edges, children)
#                 ret_tree = Tree(new_root)
#                 return ret_tree
#             elif (level == top_level+1):
#                 edges.append(str_to_array(edge))
#                 sub_tree = new_tree[x:]
#                 children.append(str_to_tree_rec(sub_tree))
#         new_root = Node(str_to_array(action), edges, children)
#         ret_tree = Tree(new_root)
#         return ret_tree


# def convert_short_tree_list(tree_list):
#     new_list = []
#     for tree in tree_list:
#         if len(tree) > 0:
#             new_list.append(short_str_to_tree(tree))
#     return new_list


# def convert_tree_list(tree_list):
#     new_list = []
#     for tree in tree_list:
#         if len(tree) > 0:
#             new_list.append(str_to_tree(tree))
#     return new_list


# def array_product2(array1,array2):
#     new_array = []
#     for x in array1:
#         for y in array2:
#             new_array.append([x,y])
#     return new_array

# def array_product3(array1,array2,array3):
#     new_array = []
#     for x in array1:
#         for y in array2:
#             for z in array3:
#                 new_array.append([x,y,z])
#     return new_array

# def array_product4(array1,array2,array3, array4):
#     new_array = []
#     for x in array1:
#         for y in array2:
#             for z in array3:
#                 for q in array4:
#                     new_array.append([x,y,z,q])
#     return new_array

#### NEED ALL K LENGTH PERMS W REPETITION

def all_k_length(set, k):
    #print("LENGTH:")
    #print(len(set))
    return [p for p in itertools.product(set, repeat=k)]
    

#def all_k_length(set, k):


# def obs_child_combos(obs1, obs2, child1, child2):
#     obs_child_pair_list1 = []
#     obs_child_pair_list2 = []
#     l = len(obs1)
#     for x in range(l):
#         obs_child_pair_list1.append([obs1[x],child1[x]])
#         obs_child_pair_list2.append([obs2[x],child2[x]])
#     #print(obs_child_pair_list1)
#     #returns all combinations of action observation pairs
#     combos = []
#     for pair1 in obs_child_pair_list1:
#         for pair2 in obs_child_pair_list2:
#             new_arr = pair1 + pair2
#             combos.append(new_arr)
#     return combos


# def all_combos_with_rep(arr, rep):
#     combos = [p for p in itertools.product(arr, repeat=rep)]
#     return combos

# def tuple_to_str(tuple):
#     new_str = "[" + str(tuple[0]) + "," + str(tuple[1]) + "]"
#     return new_str



# def arr_of_tuples_to_array_of_str(array):
#     string_arr = []
#     for x in array:
#         new_str = tuple_to_str(x)
#         string_arr.append(new_str)
#     return string_arr


# def dist_agent_knows_all(locs):
#     hmap = {}
#     for loc in locs:
#         idx = tuple_to_str(loc)
#         hmap[idx] = True
#     return hmap


# def all_dist_agent_doesnt_know_1(locs, start, goal):
#     map_list = []
#     start_idx = tuple_to_str(start)
#     goal_idx = tuple_to_str(goal)
#     locs.remove(start)
#     locs.remove(goal)
#     for unknown_loc in locs:
#         hmap = {}
#         unknown_idx = tuple_to_str(unknown_loc)
#         hmap[unknown_idx] = False
#         hmap[start_idx] = True
#         hmap[goal_idx] = True
#         for other_loc in locs:
#             idx = tuple_to_str(other_loc)
#             if idx != unknown_idx:
#                 hmap[idx] = True
#         map_list.append(hmap)
#     return map_list

# def all_dist_maps(locs, start, goal):
#     map_list = []
#     temp_locations = []
#     temp_locations += locs
#     map_list.append(dist_agent_knows_all(locs))
#     map_list += all_dist_agent_doesnt_know_1(temp_locations, start, goal)
#     return map_list

# '''
# def transpose(mat):
#     h = len(mat)
#     w = len(mat[0])
#     A = matrix(range(h*w), (h,w))
#     #print(new_mat)
#     for i in range(h):
#         for j in range(w):
#             row = mat[i]
#             elem = row[j]
#             print(elem)
#             #print(str(i) + "," + str(j))
#             A[i,j] = elem

#     #print(A[0,0])
#     #print(mat[0][0])

#     return A
    
# '''

# """
# def hash_with_certain_value(val, val_array):
#     hash_tab = {}
#     for x in val_array:
#         if x == val:
#             hash_tab[x] = 1
#         else:
#             hash_tab[x] = 0
#     return hash_tab

# def uncertain_hash(val_array_included, val_array_not_included):
#     hash_tab = {}
#     dist = 1/len(val_array_included)
#     for x in val_array_included:
#         hash_tab[x] = dist
#     for x in val_array_not_included:
#         hash_tab[x] = 0
#     return hash_tab


# def all_possible_distributions(rew_array_included, rew_array_not_included):
#     dist_list = []
#     dist_list.append(uncertain_hash(rew_array_included, rew_array_not_included))
#     rew_array = rew_array_not_included + rew_array_included
#     for x in rew_array_included:
#         dist_list.append(hash_with_certain_value(x, rew_array))
#     return dist_list



# def all_possible_loc_hash_pairs_rew_maps(rew_array_included, rew_array_not_included, locations, goal_loc, goal_rew, start_loc):
#     ret_array = []
#     rew_array = rew_array_not_included + rew_array_included
#     for loc in locations:
#         if loc == goal_loc:
#             dist = [hash_with_certain_value(goal_rew, rew_array)]
#             ret_array.append([loc, dist])
#         elif loc == start_loc:
#             dist = [hash_with_certain_value(0, rew_array)]
#             ret_array.append([loc, dist])
#         else:
#             dists = all_possible_distributions(rew_array_included, rew_array_not_included)
#             ret_array.append([loc, dists])
#     return ret_array


# def hmap_rec(start, dist_list, locs, rew_array_included, rew_array_not_incl, goal_loc, goal_rew, start_loc):
#     #print("Dist list: ")
#     #print(dist_list)
#     #print("Locs:")
#     #print(locs)
#     sol_array = []
#     rew_array = rew_array_not_incl + rew_array_included
#     if len(locs) == 0:
#         return dist_list
#     else:
#         current_loc = locs[0]
#         locs.remove(current_loc)
#         if current_loc == goal_loc:
#             dists = [hash_with_certain_value(goal_rew, rew_array)]
#         elif current_loc == start_loc:
#             dists = [hash_with_certain_value(0, rew_array)]
#         else:
#             dists = all_possible_distributions(rew_array_included, rew_array_not_incl)
#         for d in dists:
#             dist_list.append([current_loc, d])
#             if start:
#                 sol_array.append(hmap_rec(False, dist_list, locs, rew_array_included, rew_array_not_incl, goal_loc, goal_rew, start_loc))
#             else:
#                 return hmap_rec(False, dist_list, locs, rew_array_included, rew_array_not_incl, goal_loc, goal_rew, start_loc)
#     return sol_array


# def hash_rec(solution_set, locs, rew_array_included, rew_array_not_incl, goal_loc, goal_rew, start_loc):
#     rew_array = rew_array_not_incl + rew_array_included
#     print(len(locs))
#     if len(locs) == 0:
#         return solution_set
#     else:
#         new_sol_set = []
#         current_loc = locs[0]
#         locs.remove(current_loc)
#         if current_loc == goal_loc:
#             distrs = [hash_with_certain_value(goal_rew, rew_array)]
#         elif current_loc == start_loc:
#             distrs = [hash_with_certain_value(0, rew_array)]
#         else:
#             distrs = all_possible_distributions(rew_array_included, rew_array_not_incl)
#         for d in distrs:
#             if len(solution_set) == 0:
#                 new_sol = [[current_loc, d]]
#                 new_sol_set = new_sol_set + new_sol
#             else:
#                 for s in solution_set:
#                     #print(d)
#                     #print(s)
#                     new_sol = [s] + [[current_loc, d]]
#                     #print(new_sol)
#                     new_sol_set = new_sol_set + new_sol
#                     #print(new_sol_set)
#         return hash_rec(new_sol_set, locs, rew_array_included, rew_array_not_incl, goal_loc, goal_rew, start_loc)


# def all_possible_rew_dists(locs, incl, not_incl, goal_loc, goal_rew, start_loc):
#     return hash_rec([], locs, incl, not_incl, goal_loc, goal_rew, start_loc)


# def map_unknown(rew_incl, rew_excl):
#     prob = 1/len(rew_incl)
#     hash_table = {}
#     for r in rew_incl:
#         hash_table[r] = prob
#     for r in rew_excl:
#         hash_table[r] = 0
#     return hash_table


# def value_known(val, rew_incl, rew_excl):
#     rew_set = rew_incl + rew_excl
#     hash_table = {}
#     for r in rew_set:
#         if r == val:
#             hash_table[r] = 1
#         else:
#             hash_table[r] = 0
#     return hash_table


# def all_possible_dists_agent_doesnt_know_1(rew_map, locs, rew_incl, rew_excl, goal_loc, starting_loc, goal_rew):
#     list_of_maps = []
#     locs.remove(goal_loc)
#     locs.remove(starting_loc)
#     goal_dist = value_known(goal_rew, rew_incl, rew_excl)
#     start_state_dist = value_known(0, rew_incl, rew_excl)
#     goal_idx = tuple_to_str(goal_loc)
#     start_idx = tuple_to_str(starting_loc)
#     for loc in locs:
#         hash_table = {}
#         hash_table[goal_idx] = goal_dist
#         hash_table[start_idx] = start_state_dist
#         for temp_loc in locs:
#             idx = tuple_to_str(temp_loc)
#             if temp_loc == loc:
#                 hash_table[idx] = map_unknown(rew_incl, rew_excl)
#             else:
#                 hash_table[idx] = value_known(rew_map[idx], rew_incl, rew_excl)
#         list_of_maps.append(hash_table)
#     return list_of_maps

# def all_permutations(list):
#     perm_list = []


# def hash_print_pretty(hash_table):
#     for idx in hash_table:
#         print(idx + " : " + str(hash_table[idx]))

# def all_rew_maps_rec(sol, locs, rew_incl):
#     #print(sol)
#     map_list = []
#     if len(locs) == 0:
#         return sol
#     else:
#         new_sol = []
#         current_loc = locs[0]
#         locs.remove(current_loc)
#         loc_idx = tuple_to_str(current_loc)
#         for rew in rew_incl:
#             for map in sol:
#                 #print(rew)
#                 new_map = map
#                 new_map[loc_idx] = rew
#                 new_sol.append(new_map)
#         map_list = map_list + all_rew_maps_rec(new_sol, locs, rew_incl)
#     return map_list



# def all_rew_maps(locs, rew_incl, goal_rew, goal_loc, starting_loc):
#     map_list = []
#     locs.remove(goal_loc)
#     locs.remove(starting_loc)
#     goal_idx = tuple_to_str(goal_loc)
#     start_idx = tuple_to_str(starting_loc)
#     map = {}
#     map[goal_idx] = goal_rew
#     map[start_idx] = 0
#     solution_array = [map]
#     return all_rew_maps_rec(solution_array, locs, rew_incl)



# """



# incl = [-1,-2,-3,-4,-5]
# not_incl = [0,100]
# locations = array_product2([0,1], [0,1,2])
# goal_loc = [1,2]
# goal_rew = 100
# start_loc = [0,0]


# def list_without_item(list, item):
#     new_list = []
#     for x in list:
#         if x != item:
#             new_list.append(x)
#     return new_list

#print(all_dist_maps(locations, start_loc, goal_loc))


#print(all_possible_distributions(incl, not_incl))

#print(all_k_length([1,2,3], 3))


