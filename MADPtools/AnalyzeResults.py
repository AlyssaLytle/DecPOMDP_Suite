import sys
from DPOMDP_Writer.Reader import *
from DPOMDP_Writer.DPOMDPWriterMedium import DPOMDPWriterACC
import csv
import os
import json 

readfile = "../lsOutput.log"
f = open(readfile, "r")
filepaths = []

#get filepath names for all results
for x in f:
    if x[-4:-1] == "Pol":
        filepaths.append(x[:-1])
        
        
with open('dpomdp.csv', newline='') as csvfile:
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

#make a DPOMDPWriter for testing purposes    
test_dpomdp = DPOMDPWriterACC(machine_comm_actions, machine_mvmt_actions, human_comm_actions, human_mvmt_actions, modes,prob_dict,cost_dict, 1, human_observations, machine_observations)


#for each file, read the file to see if it gave a result, then get value of result

successful_solvers = []
unsuccessful_solvers = []
for filename in filepaths:
    path = "/afs/cs.unc.edu/home/abyrnes1/.madp/results/GMAA/ACC-ss-standby-scen-1/" + filename
    result = get_trees(path, len(human_observations), len(machine_observations))
    if len(result) > 0:
        [h_tree, m_tree] = result
        value = test_dpomdp.get_value(h_tree, m_tree, "standby", 0, 0)
        successful_solvers.append([filename,value])
    else:
        #no solution was returned by MADP
        unsuccessful_solvers.append(filename)
        


f = open("results.txt", "w")
f.writelines(successful_solvers)
f.close()

#write shell script to erase empty results

command = ""
for fname in unsuccessful_solvers:
    command += "rm -r /afs/cs.unc.edu/home/abyrnes1/.madp/results/GMAA/ACC-ss-standby-scen-1/" + fname + "\n"

f = open("cleanresults.sh")
f.writelines(command)
f.close()   