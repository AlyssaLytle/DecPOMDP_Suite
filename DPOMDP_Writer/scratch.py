import itertools
import sys
import time

from reader import *
from ACCDPOMDP import ACC_DPOMDP
from ExtractCSV import latex_to_table

sys.path.append("..")
from ArrayTree import ArrayTree
from MAAstarmod import *

modes = ["standby", "following", "speedcontrol", "hold", "override", "error"]
automated_modes = ["following", "speedcontrol"]
non_automated_modes = ["canceled", "hold", "override","error"]
human_mvmt_actions = ["accel", "decel", "maintainspeed", "none"]
human_comm_actions = ["pushbutton","dontpushbutton"]
human_actions = list(itertools.product(human_mvmt_actions, human_comm_actions))
machine_mvmt_actions = ["accel", "decel", "maintainspeed", "none"]
machine_comm_actions = ["communicate","dontcommunicate"]
machine_actions = list(itertools.product(machine_mvmt_actions, machine_comm_actions))
#print(machine_actions)
#print(human_actions)


scenario_change_prob = .01
error_prob = .01
exit_hold_prob = .01

states = modes
machine_observations = states
human_observations = states + ["none"]
#print(human_observations)

prob_dict = {"exithold": exit_hold_prob, "error":error_prob}

human_movement_cost = -1
unsafe_cost = -100
comm_cost = -1
cost_dict = {"human movement":human_movement_cost, "unsafe": unsafe_cost, "machine communication": comm_cost, "automation reward" : 1}

mode_change_table = latex_to_table("TransitionLatexClean.csv")

init_h_action = human_actions[0]
init_m_action = machine_actions[0]
init_actions = {"human" : init_h_action, "machine": init_m_action}
start_state = modes[0]

horizon = 2

scenario = 3

dpomdp = ACC_DPOMDP(start_state, mode_change_table, machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict, scenario, human_observations, machine_observations,horizon, init_actions)


# start_time = time.perf_counter()
# solutions = solve(dpomdp)
# for sol in solutions:
#     [trees, f] = sol
#     [h_tree, m_tree] = trees
#     h_tree.print()
#     m_tree.print()
# print("Num solutions: " + len(solutions))
# print("Run time: " + str(start_time - time.perf_counter()))

[h_tree, m_tree] = get_trees(filename, 7, 6)
h_tree.print()
m_tree.print()
print(dpomdp.get_value(h_tree, m_tree, start_state, 0, 0))

# #print(dpomdp.get_transition_table("following", ["decel", "pushbutton"], ["none", "dontcommunicate"]))



# for a1 in human_actions:
#     for a2 in machine_actions:
#         for mode in modes:
#             table = dpomdp.get_transition_table(mode,a1,a2)
#             #print(table)
#             sum = 0
#             for elem in table:
#                 sum += elem[1]


# tlist = [0,1,2,3,4,5,6,7,8,9,10,11,12]
# tlist2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
# edges = ["a","b"] * 6
# elist = [""]+ edges
# print(elist)
# elist2 = elist + ["c"]
# print(elist2)
# test_tree1 = ArrayTree(3,tlist, elist)
# test_tree2 = ArrayTree(3,tlist2, elist2)


# test_tree2.print()

# print(test_tree1.get_children(0))

# # D = [1,2,[3,"apples"]]
# # print(D)
# # D.remove([3,"apples"])
# # print(D)
# # a = [3,"apples"]
# # D.append(a)
# # D.append([3,"apples"])
# # print(D)