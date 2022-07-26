import sys
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import csv
import json
import graphviz

#Call should look like python3 GetResults.py filename start_state scenario_number
[cmd, filename, start_state, scenario_number] = sys.argv
result = "GMAA_" + filename + "_MAAstar_QMDP_h2_restarts1_NoCache_BGIP-BnB_ka0_JTODescendingProbability_CCI1_JPol"
path_to_res = "/afs/cs.unc.edu/home/abyrnes1/.madp/results/GMAA/" + filename + "/" + result

print(filename)

with open('dpomdp-min.csv', newline='') as csvfile:
    dreader = csv.reader(csvfile)
    data = list(dreader)
    machine_comm_actions = data[0]
    machine_mvmt_actions = data[1]
    human_comm_actions = data[2]
    human_mvmt_actions = data[3]
    modes = data[4]
    pdict = data[5][0].replace('""','"')
    prob_dict = json.loads(pdict)
    cdict = data[6][0].replace('""','"')
    cost_dict = json.loads(cdict)
    human_observations = data[7]
    machine_observations = data[8]

writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,scenario_number, human_observations, machine_observations)

[h_tree, m_tree, value] = get_trees(path_to_res, len(human_observations), len(machine_observations))
[hgraph, mgraph] = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)
f = open("htree.dot", "w")
f.writelines(hgraph)
f.close()
g = open("mtree.dot", "w")
g.writelines(mgraph)
g.close()
h = open("tree_values.csv", "a")
line = filename + "," + str(value) + "\n"
h.write(line)
h.close()

graph = graphviz.Source.from_file('htree.dot')
graph.format = 'png'
#graph.view()
tree_name = "figs/" + start_state + "-scen" + str(scenario_number) + "_hum"
filename = graph.render(filename=tree_name)

graph = graphviz.Source.from_file('mtree.dot')
graph.format = 'png'
#graph.view()
tree_name = "figs/" + start_state + "-scen" + str(scenario_number) + "_mach"
filename = graph.render(filename=tree_name)

