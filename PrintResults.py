import os

readfile = "lsOutput.log"
f = open(readfile, "r")
shell_commands = ""
for x in f:
    print(x[-3:])
    if x[-3:] == "Pol":
        file_path = "~/.madp/results/GMAA/ACC-ss-standby-scen-1/" + x
        #if os.path.getsize(file_path) != 0:
        #    print()
        
