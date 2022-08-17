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

#modes = ["standby", "following", "speedcontrol", "error", "hold", "override"]
modes = ["standby", "following", "speedcontrol", "error", "hold"]
#automated_modes = ["following", "speedcontrol"]
#non_automated_modes = ["canceled", "hold", "override","error"]
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

states = modes.copy()
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
with open('dpomdp-min.csv', 'w', newline='') as csvfile:
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
    for start_state in modes:
        writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, states,prob_dict,cost_dict, scenario, human_observations, machine_observations)
        filename = "ACC-" + start_state + "-s" + str(scenario)
        rel_path = "ACC/" + filename + ".dpomdp"
        abs_file_path = os.path.join(script_dir, rel_path)
        writer.write_to_file(abs_file_path, start_state, True, False)
        
        
### Generate shell file that outputs all the tree results ###
shell_file = "GetResults.sh"
file_data = ""
for scenario in range(8):
    for start_state in modes:
        filename = "ACC-" + start_state + "-s" + str(scenario)
        call = "python3 GetResults.py " + filename + " " + start_state + " " + str(scenario) + "\n"
        file_data +=  call 
f = open(shell_file, "w")
f.writelines(file_data)
f.close()