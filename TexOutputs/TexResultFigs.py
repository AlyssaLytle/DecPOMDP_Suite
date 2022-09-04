
def gen_fig(name, scale, label, caption):
    space = "    "
    output = "\\begin{figure}[h]\n"
    #output += space + "\centering\n"
    output += space + "\includegraphics[width=" + str(scale)
    output += "\\textwidth]{" + name + "}\n"
    output += space + "\caption{" + caption + "}\n"
    output += space + "\label{fig:" + label + "}\n"
    output += "\end{figure}\n"
    return output

def gen_figs_tex(prefix, modes, scenarios):
    output = ""
    space = "\n"
    for scenario in scenarios:
        for mode in modes:
            name = "result-figs/" + prefix 
            name += mode + "-" 
            name += "scen" + str(scenario)
            mname = name + "_mach.png"
            hname = name + "_hum.png"
            scale = ""
            label = mode + "-s" + str(scenario) + "-"
            mlabel = label + "mach"
            hlabel = label + "hum"
            caption = "Policy for Scenario 2 starting in Standby"
            hcaption = "Human " + caption
            mcaption = "Machine " + caption
            hfig = gen_fig(hname, scale, hlabel, hcaption)
            mfig = gen_fig(mname, scale, mlabel, mcaption)
            output += hfig + space
            output += mfig + space
    return output
            
modes = ["standby", "following", "speedcontrol", "error", "hold"]
scenarios = range(4)
scenarios = range(4,8)

filename = "results.tex"
f = open(filename, "w")
f.writelines(gen_figs_tex("ACC-min", modes, scenarios))
f.close()