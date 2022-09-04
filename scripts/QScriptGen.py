q_heur = ["QMDP", "QPOMDP", "QBG", "QMDPc", "QPOMDPav", "QBGav", "QHybrid", "QPOMDPhybrid", "QBGhybrid", "QBGTreeIncPrune", "QBGTreeIncPruneBnB"]
modes= ["standby", "following", "speedcontrol"]
scenario = str(7)

output = "cd ..\n"
output += "cd ../MADP/src/utils\n"
command = "timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-min-"

for mode in modes:
    for q in q_heur:
        line = command + mode + "-s" + scenario + ".dpomdp -h2 -Q " + q + "\n"
        output += line

f = open("QTest.sh", "w")
f.writelines(output)
f.close()
