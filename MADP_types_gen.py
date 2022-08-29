import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


solver_types = ["BFS", "AM", "CE", "MP", "BnB"]
GMAA_param = ["MAAstar", "FSPC", "kGMAA"]
q_heur = ["QMDP", "QPOMDP", "QBG", "QMDPc", "QPOMDPav", "QBGav", "QHybrid", "QPOMDPhybrid", "QBGhybrid", "QBGTreeIncPrune", "QBGTreeIncPruneBnB"]

modes = ["standby", "following", "speedcontrol", "error", "hold", "override"]
modes_wo_override = ["standby", "following", "speedcontrol", "error", "hold"]
scenarios = range(8)

count = 0

output = "date +%T \n"
for solver in solver_types:
    for gmaa_param in ["MAAstar"]:
        for q in q_heur:
            if gmaa_param == "MAAstar":
                command = "../MADP/src/solvers/GMAA --useQcache --verbose "
                command += "-G " + gmaa_param 
            elif gmaa_param == "kGMAA":
                command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
                command += "-G " + gmaa_param 
                command += " -k 1000" 
            else:
                command = "timeout -k 1m 1m ../MADP/src/solvers/GMAA "
                command += "-G " + gmaa_param 
            command += " -B " + solver 
            command += " -Q " + q
            command += " MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2"
            output += command + "\n"
            output += "date +%T \n"
            count += 1
            
'''for solver in solver_types:
    for gmaa_param in GMAA_param:
        for q in q_heur:
            if gmaa_param == "MAAstar":
                command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
                command += "-G " + gmaa_param 
            elif gmaa_param == "kGMAA":
                command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
                command += "-G " + gmaa_param 
                command += " -k 1000" 
            else:
                command = "timeout -k 1m 1m ../MADP/src/solvers/GMAA "
                command += "-G " + gmaa_param 
            command += " -B " + solver 
            command += " -Q " + q
            command += " MADPtools/ACC/ACC-ss-standby-scen-1-obs.dpomdp -h2"
            output += command + "\n"
            count += 1'''

'''output = ""

for solver in solver_types:
    for gmaa_param in ["FSPC", "kGMAA"]:
        command = "timeout -k 1m 1m ../MADP/src/solvers/GMAA "
        command += "-G " + gmaa_param 
        command += " -B " + solver 
        command += " MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2"
        output += command + "\n"
        count += 1       


for solver in solver_types:
    for q in q_heur:
        command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
        command += "-G MAAstar"
        command += " -B " + solver 
        command += " -Q " + q
        command += " MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2"
        output += command + "\n"
        #remove optimal value database
        #output += "rm ~/.madp/results/GMAA/optimalValueDatabase\n"
        count += 1
        
for solver in solver_types:
    for q in q_heur:
        command = "timeout -k 5m 5m ../MADP/src/solvers/GMAA "
        command += "-G MAAstar"
        command += " -B " + solver 
        command += " -Q " + q
        command += " MADPtools/ACC/ACC-ss-standby-scen-1-obs.dpomdp -h2"
        output += command + "\n"
        #remove optimal value database
        #output += "rm ~/.madp/results/GMAA/optimalValueDatabase\n"
        count += 1
'''

def GenerateSolvers(prefix, inp_modes):
    output = ""
    for mode in inp_modes:
        for scenario in scenarios:
            #output += "set NOW=`date '+%T'` \n" 
            name = prefix + "-" + mode + "-s" + str(scenario)
            fullname = name + ".dpomdp"
            output += "timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/" + prefix + "/" + fullname + " -h2\n"
            #output += "set END=`date '+%T'` \n" 
            #output += 'echo "Start time: "$NOW " End Time: "$END\n'
    
    fname = "solvers" + prefix + ".sh"
    f = open(fname, "w")
    f.writelines(output)
    f.close()

'''### Write evaluator for results

# Get list of all results
#command = "cd ~/.madp/results/GMAA/ACC-ss-standby-scen-1/\n"
command = "ls ~/.madp/results/GMAA/ACC-ss-standby-scen-1 >> lsOutput.log\n"

# Run python program that prints all results from this log
#command += "cd ~/public/alyssadpomdp/DecPOMDP_Suite\n"
command += "python3 PrintResults.py\n"
command += "python3 AnalyzeResults.py\n"

f = open("listresults.sh", "w")
f.writelines(command)
f.close()'''

#Generate Q Values
def GenerateQ(prefix, inp_modes):
    output = "cd ../MADP/src/utils\n"
    output += "date +%T\n"
    for mode in inp_modes:
        for scenario in scenarios:  
            name = prefix + "-" + mode + "-s" + str(scenario)
            fullname = name + ".dpomdp"
            output += 'echo "Finding q value for ' + name + '"\n'
            output += "timeout -k 1h 1h " 
            output += "./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/" + prefix + "/" + fullname + " -h2 -Q " 
            output += "QMDP"
            output += " > QMDP-" + name + ".log" + "\n"
            output += "date +%T\n"
    
    fname =  "QGen" + prefix + ".sh"   
    f = open(fname, "w")
    f.writelines(output)
    f.close()

GenerateSolvers("ACC", modes)   
GenerateQ("ACC", modes)
GenerateSolvers("ACCmin", modes_wo_override)   
GenerateQ("ACCmin", modes_wo_override)