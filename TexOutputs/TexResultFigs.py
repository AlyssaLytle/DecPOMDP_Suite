
def gen_fig(name, scale, label, caption):
    space = "    "
    output = "\\begin{figure}[h]\n"
    output += space + "\centering\n"
    output += space + "\includegraphics[width=" + str(scale)
    output += "\\textwidth]{" + name + "}\n"
    output += space + "\caption{" + caption + "}\n"
    output += space + "\label{fig:" + label + "}\n"
    output += "\end{figure}\n"
    return output
'''
def gen_figs_tex(prefix, modes, scenarios):
    output = ""
    space = "\n"
    for scenario in scenarios:
        for mode in modes:
            name = "ACC-result-figs/" + prefix 
            name += mode + "-" 
            name += "scen" + str(scenario)
            mname = name + "_mach.png"
            hname = name + "_hum.png"
            scale = ""
            label = mode + "-s" + str(scenario) + "-"
            mlabel = label + "mach"
            hlabel = label + "hum"
            caption = "Policy for Scenario " + str(scenario)
            caption += " starting in " + mode
            hcaption = "Human " + caption
            mcaption = "Machine " + caption
            hfig = gen_fig(hname, scale, hlabel, hcaption)
            mfig = gen_fig(mname, scale, mlabel, mcaption)
            output += hfig + space
            output += mfig + space
    return output
'''

def gen_figs_tex_from_file(fname,prefix):
    output = ""
    space = "\n"
    f = open(fname, "r")
    lines = f.readlines()
    for l in lines:
        l = l.split(":")
        l_list = l[0].split(" + ")
        scenario = l_list[0][-1]
        mode = l_list[0][:-1]
        name = "ACC-result-figs/" + prefix 
        name += mode + "-" 
        name += "scen" + str(scenario)
        mname = name + "_mach.png"
        hname = name + "_hum.png"
        scale = ""
        label = mode + "-s" + str(scenario) + "-"
        mlabel = label + "mach"
        hlabel = label + "hum"
        caption = "Policy for " + l[0]
        hcaption = "Human " + caption
        mcaption = "Machine " + caption
        hfig = gen_fig(hname, scale, hlabel, hcaption)
        mfig = gen_fig(mname, scale, mlabel, mcaption)
        output += hfig + space
        output += mfig + space
    return output
            
modes = ["standby", "following", "speedcontrol", "error", "hold", "override"]
scenarios = range(8)
#scenarios = range(4,8)

filename = "results.tex"
f = open(filename, "w")
f.writelines(gen_figs_tex_from_file("../MADPtools/merge.csv", "ACC"))
f.close()