""" Makes the solving scripts """
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

def GenerateSolvers(prefix, inp_modes, inc_clustering,inc_expansion, q_cache):
    wrap_output = "sh ClearResults.sh\n"
    for mode in inp_modes:
        
        output = "cd ..\n"
        for scenario in scenarios:
            #output += "set NOW=`date '+%T'` \n" 
            name = "ACC" + "-" + mode + "-s" + str(scenario)
            fullname = name + ".dpomdp"
            output += '''now="$(date +'%M:%S:%3N')"\n'''
            output += '''echo "Time: $now"\n'''
            output += "timeout -k 1h 1h "
            output += "../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar "
            if inc_clustering: 
                output += "--useBGclustering "
            if inc_expansion:
                output += "--BGIP_Solver=BnB --BnB-ordering=Prob " 
            output += "-Q QMDP "
            if q_cache:
                output += "--useQcache "
            output += "MADPtools/" + "ACC" + "/" + fullname + " -h2\n"
            #output += "set END=`date '+%T'` \n" 
            #output += 'echo "Start time: "$NOW " End Time: "$END\n'
        fname0 = "solvers" + prefix + "-" + mode + ".sh"
        log_path = "/afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/"
        log_name = log_path + prefix + "-" + mode + ".log"
        fpath = "scripts/"+ fname0
        g = open(fpath, "w")
        g.writelines(output)
        g.close()
        wrap_output += 'echo "Running:' + fname0 +'"\n'
        wrap_output += "timeout -k 4h 4h sh " + fname0 + " > " + log_name + "\n"
    fname = "scripts/solvers" + prefix + ".sh"
    f = open(fname, "w")
    f.writelines(wrap_output)
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
    output = "cd ..\n"
    output += "cd ../MADP2/src/utils\n"
    output += "date +%T\n"
    for mode in inp_modes:
        for scenario in scenarios:  
            name = prefix + "-" + mode + "-s" + str(scenario)
            fullname = name + ".dpomdp"
            output += 'echo "Finding q value for ' + name + '"\n'
            output += "timeout -k 1h 1h " 
            output += "./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/" + prefix + "/" + fullname + " -h2 -Q " 
            output += "QMDP"
            output += "\n"
            #output += " > QMDP-" + name + ".log" + "\n"
            output += "date +%T\n"
    
    fname =  "scripts/QGen" + prefix + ".sh"   
    f = open(fname, "w")
    f.writelines(output)
    f.close()

# GenerateSolvers("ACC", modes)   
# GenerateQ("ACC", modes)
# GenerateSolvers("ACC-min", modes_wo_override)   
# GenerateQ("ACC-min", modes_wo_override)

GenerateSolvers("ACC", modes, True, True, False)   
GenerateSolvers("ACC-noopt", modes, False, False, False)   
GenerateSolvers("ACC-cluster", modes, True, False, False)   
GenerateSolvers("ACC-incexp", modes, False, True, False)   


## TODO: Write script to analyze average runtimes
## TODO: Have something that exits if it times out