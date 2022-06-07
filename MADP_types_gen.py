import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


solver_types = ["BFS", "AM", "CE", "MP", "BnB"]
GMAA_param = ["MAAstar", "FSPC", "kGMAA"]
q_heur = ["QMDP", "QPOMDP", "QBG", "QMDPc", "QPOMDPav", "QBGav", "QHybrid", "QPOMDPhybrid", "QBGhybrid", "QBGTreeIncPrune", "QBGTreeIncPruneBnB"]


output = ""
for solver in solver_types:
    for gmaa_param in GMAA_param:
        for q in q_heur:
            command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
            command += "-G " + gmaa_param 
            command += " -B " + solver 
            command += " -Q " + q
            command += " ACC/ACC-ss-standby-scen-1.dpomdp -h2"
            output += command + "\n"
        
output = ""
for solver in solver_types:
    for q in q_heur:
        command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
        command += "-G MAAstar"
        command += " -B " + solver 
        command += " -Q " + q
        command += " ACC/ACC-ss-standby-scen-1.dpomdp -h2"
        output += command + "\n"
        
f = open("ACCtest.sh", "w")
f.writelines(output)
f.close()

