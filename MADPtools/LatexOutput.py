modes = ["standby", "following", "speedcontrol", "error", "hold"]
scenarios = range(1,9)

output = ""
#output += "\\begin{figure}\n"
#output += "\centering\n"



for mode in modes:
    for scenario in scenarios:
        if (scenario%2 == 1):
            output += "\\begin{figure}\n"
            output += "\centering\n"
        hum_file = "result-figs/" + mode + "-scen" + str(scenario) + "_hum.png"
        hum_caption = "Human policy tree for scenario " + str(scenario) + " starting in " + mode + " mode"
        hum_label = "hum-" + mode + "-" + str(scenario)
        mach_file = "result-figs/" + mode + "-scen" + str(scenario) + "_mach.png"
        mach_caption = "Machine policy tree for scenario " + str(scenario) + " starting in " + mode + " mode"
        mach_label = "hum-" + mode + "-" + str(scenario)
        output += "\includegraphics[width=.75\\textwidth]{"+ hum_file + "}\n"
        output += "\caption{" + hum_caption + "}\n"
        #output += "\label{fig:" + hum_label + "}\n"
        output += "\includegraphics[width=.75\\textwidth]{"+ mach_file + "}\n"
        output += "\caption{" + mach_caption + "}\n"
        #output += "\label{fig:" + mach_label + "}\n"
        if (scenario%2 == 0):
            output += "\end{figure}\n\n"
#output += "\end{figure}"        

        
f = open("LatexOutput.txt", "w")
f.writelines(output)
f.close()       