import itertools
from DPOMDPWriterMedium import DPOMDPWriterACC
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
print(machine_actions)
print(human_actions)


scenario_change_prob = .01
error_prob = .01
exit_hold_prob = .01

states = modes
machine_observations = states
human_observations = states + ["none"] 
human_observations.remove("sink")
#print(human_observations)

prob_dict = {"exithold": exit_hold_prob, "error":error_prob}

human_movement_cost = -1
unsafe_cost = -100
comm_cost = -1
cost_dict = {"human movement":human_movement_cost, "unsafe": unsafe_cost, "machine communication": comm_cost, "automation reward" : 1}


writer = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict,1, human_observations, machine_observations)

file_name = "ACC.dpomdp"
test_state = states[0]
#print(test_state)

#print(writer.eq_arrays(data,data))
#print(trans_table)
writer.write_to_file(file_name, test_state)
#print(data)
#print(data[-1])
