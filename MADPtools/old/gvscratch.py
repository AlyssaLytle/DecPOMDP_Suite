import graphviz
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
from ArrayTree import ArrayTree
import itertools

#from help_methods import *

modes = ["standby", "following", "speedcontrol", "hold", "override", "error", "sink"]
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
human_observations.remove("sink")
#print(human_observations)

prob_dict = {"exithold": exit_hold_prob, "error":error_prob}

human_movement_cost = -2
unsafe_cost = -100
comm_cost = -1
cost_dict = {"human movement":human_movement_cost, "unsafe": unsafe_cost, "machine communication": comm_cost, "automation reward" : 1}


writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,1, human_observations, machine_observations)

file_name = "ACC.dpomdp"
start_state = states[0]


filename = "testpolicy"

[h_tree, m_tree] = get_trees(filename, len(human_observations), len(machine_observations))
h_tree.print()
m_tree.print()
print(writer.get_value(h_tree,m_tree,start_state,0, 0))


#graphs = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)
#print(graphs)