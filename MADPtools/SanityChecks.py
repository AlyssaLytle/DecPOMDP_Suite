import json
import csv

with open('../dpomdp.csv', newline='') as csvfile:
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


def triple_in_list(inp_list, pair):
    #checks if a list of size 3 is in inp_list
    for elem in inp_list:
        if (pair[0] == elem[0]) & (pair[1] == elem[1]) & (pair[2] == elem[2]):
            return True
    return False

def check_obs_sums(filename):
    ### makes sure all possible action,next-state pairs have observations that sum to 1
    #first, find all possible action, next-state pairs
    action_state_combos = []
    observations = []
    f = open(filename, "r")
    for x in f:
        x = x.split(" ")
        if x[0] == "T:":
            h_action = x[1]
            m_action = x[2]
            next_state = x[6]
            triple = [h_action, m_action, next_state]
            if (triple_in_list(action_state_combos,triple) == False):
                action_state_combos.append(triple)
        if x[0] == "O:":
            h_action = x[1]
            m_action = x[2]
            next_state = x[4]
            h_obs = x[6]
            m_obs = x[7]
            prob = x[9]
            prob = int(prob[:-1])
            observations.append([h_action,m_action,next_state, h_obs, m_obs, prob])
    obs_sums = []
    for elem in action_state_combos:
        [h_action, m_action, next_state] = elem
        observations_list = []
        observations_sum = 0
        for obs in observations:
            [obs_h_action,obs_m_action,obs_next_state, h_obs, m_obs, prob] = obs
            if (obs_h_action == h_action) & (obs_m_action == m_action) & (obs_next_state == next_state):
                observations_list.append([h_obs, m_obs, prob])
                observations_sum += prob
                if observations_sum > 1:
                    print("ERROR! Observation sum greater than 1!")
                    print(elem)
                    print(observations_list)
        if observations_sum < 1:
            print("ERROR! Observation sum less than 1!")
            print(elem)
        obs_sums.append([elem, observations_list, observations_sum])
    return obs_sums    
        

output = check_obs_sums("ACC/ACC-ss-standby-scen-1.dpomdp")
#for l in output:
#    print(l)