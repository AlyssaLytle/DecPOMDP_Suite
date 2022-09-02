#This file generates all the ACC.dpomdp Files for the MADP toolbox to solve
import os
import itertools
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import sys
sys.path.append("/DPOMDP_Writer")
from DPOMDP_Writer.Reader import *
import csv
from PrintMethods import *

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


### Initializing info for DecPOMDP ###




def generate_dpomdp(inp_modes, inp_mc_table, containing_folder, file_prefix):
    ### initialize variables
    human_mvmt_actions = ["accel", "decel", "maintainspeed", "none"]
    human_comm_actions = ["pushbutton","dontpushbutton"]
    human_actions = list(itertools.product(human_mvmt_actions, human_comm_actions))
    machine_mvmt_actions = ["accel", "decel", "maintainspeed", "none"]
    machine_comm_actions = ["communicate","dontcommunicate"]
    machine_actions = list(itertools.product(machine_mvmt_actions, machine_comm_actions))

    scenario_change_prob = .01
    error_prob = .01
    exit_hold_prob = .01
    switch_prob = .01

    states = inp_modes.copy()
    states.append("sink")
    machine_observations = states
    human_observations = states + ["none"] 
    human_observations.remove("sink")
    prob_dict = {"exithold": exit_hold_prob, "error":error_prob, "switch":switch_prob}

    human_movement_cost = -5
    unsafe_cost = -10
    comm_cost = -1
    automation_reward = 1

    cost_dict = {"human movement":human_movement_cost, "unsafe": unsafe_cost, "machine communication": comm_cost, "automation reward" : automation_reward}

    ### Write DPOMDP info to a csv file
    csv_name = file_prefix +  "dpomdp.csv"
    with open(csv_name, 'w', newline='') as csvfile:
        dwriter = csv.writer(csvfile)
        dwriter.writerow(machine_comm_actions)
        dwriter.writerow(machine_mvmt_actions)
        dwriter.writerow(human_comm_actions) 
        dwriter.writerow(human_mvmt_actions)
        dwriter.writerow(states)
        prob_dict_str = [(str(prob_dict).replace("'",'"'))]
        cost_dict_str = (str(cost_dict).replace("'",'"'))
        dwriter.writerow(prob_dict_str)
        dwriter.writerow([cost_dict_str])
        dwriter.writerow(human_observations) 
        dwriter.writerow(machine_observations)

    ### Get example transition table with probabilities ###
    #writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, states,prob_dict,cost_dict, 1, human_observations, machine_observations)
    #t_table = writer.get_printable_transition_table()
    #write_transition_table(t_table, "transtable.txt")



    ### Generate .dpomdp files ###
    for scenario in range(8):
        for start_state in inp_modes:
            writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, states,prob_dict,cost_dict, scenario, human_observations, machine_observations,inp_mc_table)
            filename = file_prefix + "-" + start_state + "-s" + str(scenario)
            rel_path = containing_folder + filename + ".dpomdp"
            abs_file_path = os.path.join(script_dir, rel_path)
            writer.write_to_file(abs_file_path, start_state, True, False)
        
        
    ### Generate shell file that outputs all the tree results ###
    shell_file = file_prefix + "-" + "GetResults.sh"
    file_data = ""
    for scenario in range(8):
        for start_state in inp_modes:
            filename = file_prefix + "-" + start_state + "-s" + str(scenario)
            call = "python3 GetResults.py " + filename + " " + start_state + " " + str(scenario) + " " + file_prefix + "\n"
            file_data +=  call 
    f = open(shell_file, "w")
    f.writelines(file_data)
    f.close()

modes = ["standby", "following", "speedcontrol", "error", "hold", "override"]
modes_wo_override = ["standby", "following", "speedcontrol", "error", "hold"]
mode_change_table = "DPOMDP_Writer/Transitions.csv"
mode_change_table_wo_override = "DPOMDP_Writer/MinExampleTransitions.csv"
contaning_folder = "ACC/"
contaning_folder_wo_override = "ACC-min/"
prefix = "ACC"
prefix_wo_override = "ACC-min"

generate_dpomdp(modes,mode_change_table,contaning_folder,prefix)
generate_dpomdp(modes_wo_override, mode_change_table_wo_override, contaning_folder_wo_override, prefix_wo_override)