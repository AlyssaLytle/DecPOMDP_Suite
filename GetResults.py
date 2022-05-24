import sys
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import csv
#Call should look like python3 GetResults.py filename start_state scenario_number
[cmd, filename, start_state, scenario_number] = sys.argv
result = "GMAA_" + filename + "_kGMAA_QMDP_h2_restarts1_k1_NoCache_BGIP-AM_AM_restarts10_JPol"
path_to_res = "~/.madp/results/" + filename + "/" + result

with open('dpomdp.csv', newline='') as csvfile:
    dreader = csv.reader(csvfile)
    machine_comm_actions = list(next(dreader))
    machine_mvmt_actions = list(next(dreader))
    human_comm_actions = list(next(dreader))
    human_mvmt_actions = list(next(dreader))
    modes = list(next(dreader))
    prob_dict = list(next(dreader))
    cost_dict = list(next(dreader))
    human_observations = list(next(dreader))
    machine_observations = list(next(dreader))

writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,scenario_number, human_observations, machine_observations)

[h_tree, m_tree] = get_trees(result, len(human_observations), len(machine_observations))
graphs = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)
print(graphs)