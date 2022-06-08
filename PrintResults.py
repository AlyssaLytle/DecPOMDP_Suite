import os

readfile = "lsOutput.log"
f = open(readfile, "r")
shell_commands = ""
for x in f:
    if x[-4:-1] == "Pol":
        file_path = "~/.madp/results/GMAA/ACC-ss-standby-scen-1/" + x
        print(x)
        if os.path.getsize(file_path) != 0:
            shell_commands += "cat " + file_path + "\n"
            
f = open("printres.sh", "w")
f.writelines(shell_commands)
f.close()
        
