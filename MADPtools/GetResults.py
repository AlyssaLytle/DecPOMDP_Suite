import sys
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import csv
import json
import graphviz

def arr_to_str(inp_arr):
    """ Just a shortcut mthod """
    return (',').join(inp_arr)

def equal_trees(htree, mtree, comp_dict):
    """ Returns TRUE if htree and mtree already exist in this dictionary """
    h_nodes = (arr_to_str(htree.nodes) == comp_dict["htree-nodes"])
    m_nodes = (arr_to_str(mtree.nodes) == comp_dict["mtree-nodes"])
    h_edges = (arr_to_str(htree.edges) == comp_dict["htree-edges"])
    m_edges = (arr_to_str(mtree.edges) == comp_dict["mtree-edges"])
    return (h_nodes & m_nodes & h_edges & m_edges)

def new_dict(name, h_tree, m_tree, instance):
    """ Makes a new dictionary of a tree entry """
    new_entry = {"name": name} 
    new_entry["htree-nodes"] = arr_to_str(h_tree.nodes)
    new_entry["mtree-nodes"] = arr_to_str(m_tree.nodes) 
    new_entry["htree-edges"] = arr_to_str(h_tree.edges) 
    new_entry["mtree-edges"] = arr_to_str(m_tree.edges)
    new_entry["instance"] = instance
    return new_entry

def make_full_tree_image(tree_name, h_tree, m_tree, start_state):
    [hgraph, mgraph] = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)

    f = open("htree.dot", "w")
    f.writelines(hgraph)
    f.close()
    g = open("mtree.dot", "w")
    g.writelines(mgraph)
    g.close()

    graph = graphviz.Source.from_file('htree.dot')
    graph.format = 'png'
    #graph.view()
    tree_name0 = "figs/" + tree_name + "_humfull"
    filename = graph.render(filename=tree_name0)

    graph = graphviz.Source.from_file('mtree.dot')
    graph.format = 'png'
    #graph.view()
    tree_name0 = "figs/" + tree_name + "_machfull"
    filename = graph.render(filename=tree_name0)


def make_tree_image(tree_name, h_tree, m_tree, start_state):
    [hgraph, mgraph] = writer.get_graph_viz_limit_branches(h_tree,m_tree, start_state)

    f = open("htree.dot", "w")
    f.writelines(hgraph)
    f.close()
    g = open("mtree.dot", "w")
    g.writelines(mgraph)
    g.close()

    graph = graphviz.Source.from_file('htree.dot')
    graph.format = 'png'
    #graph.view()
    tree_name0 = "figs/" + tree_name + "_hum"
    filename = graph.render(filename=tree_name0)

    graph = graphviz.Source.from_file('mtree.dot')
    graph.format = 'png'
    #graph.view()
    tree_name0 = "figs/" + tree_name + "_mach"
    filename = graph.render(filename=tree_name0)

#Call should look like python3 GetResults.py filename start_state scenario_number prefix
[cmd, filename, start_state, scenario_number, prefix] = sys.argv
#result = "GMAA_" + filename + "_MAAstar_QMDP_h2_restarts1_NoCache_BGIP-BnB_ka0_JTODescendingProbability_CCI1_JPol"
result = "GMAA_" + filename + "_MAAstar_QMDP_h2_restarts1_ClusterLossless_NoCache_BGIP-BnB_ka0_JTODescendingProbability_CCI1_JPol"
path_to_res = "/afs/cs.unc.edu/home/abyrnes1/.madp/results/GMAA/" + filename + "/" + result

instance_name = start_state + "-" + str(scenario_number)

print(filename)


csv_name = prefix +  "dpomdp.csv"
with open(csv_name, newline='') as csvfile:
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

if (prefix== "ACC"):
    mc_path = "DPOMDP_Writer/Transitions_off.csv"
#else:
    #mc_path = "DPOMDP_Writer/MinExampleTransitions.csv"

writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,scenario_number, human_observations, machine_observations, mc_path)

""" Get trees """
[h_tree, m_tree, value] = get_trees(path_to_res, len(human_observations), len(machine_observations))
name = prefix + start_state + "-scen" + str(scenario_number)
make_tree_image(name,h_tree,m_tree,start_state)
make_full_tree_image(name,h_tree,m_tree,start_state)

""" then scan a file to see if a tree has been seen before
if not, assign the tree a new name """


"""
field_names = ["name", "htree-nodes", "mtree-nodes", "htree-edges", "mtree-edges","instance"]



tfile = "tree_list.csv"

num_trees = 0
output_dicts = [] """

""" Read through to see if tree exists in file """
"""
exists = False
with open(tfile, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=field_names)
    for elem in reader:
        num_trees += 1
        if equal_trees(h_tree, m_tree, elem):
            # just add this scenario + start mode instance to this entry
            name = elem["name"]
            new_entry = elem
            new_instance = elem["instance"] + ", " + instance_name
            new_entry["instance"] = new_instance
            output_dicts += new_entry
            exists = True
        else:
            output_dicts += elem
    if exists == False:
        # tree not in file yet
        # make new dict entry
        name = "tree" + str(num_trees)
        new_entry = new_dict(name, h_tree, m_tree, instance_name)
        output_dicts += new_entry
        # make graph image
        make_tree_image(name,h_tree,m_tree,start_state)
 """       
        
""" Write new tree list to file """
"""          
with open(tfile, "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names) 
    for elem in output_dicts:
        writer.writerow(elem)      
"""


""" Write values to results """
by_scen_value_file = "results/tree_values_s" + str(scenario_number) + "-" + prefix + ".csv"
by_start_mode_value_file = "results/tree_values_" + start_state + "-" + prefix + ".csv"
value = float(value)

h = open(by_start_mode_value_file, "a")
line = "scen " + str(scenario_number) + "," + str(value) + "\n"
h.write(line)
h.close()
h = open(by_scen_value_file, "a")
line = start_state + "," + str(value) + "\n"
h.write(line)
h.close()
