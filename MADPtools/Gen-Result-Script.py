def gen_result_make_file(prefix):
    ## makes new files to put results
    scenarios = range(8)
    output = ""
    if prefix == "ACC":
        modes = ["standby", "following", "speedcontrol", "error", "hold", "override"]
    else:
        modes = ["standby", "following", "speedcontrol", "error", "hold"]
    for start_state in modes:
        by_start_mode_value_file = "results/tree_values_" + start_state + "-" + prefix + ".csv"
        output += "touch " + by_start_mode_value_file + "\n"    
    for scenario_number in scenarios:
        by_scen_value_file = "results/tree_values_s" + str(scenario_number) + "-" + prefix + ".csv"
        output += "touch " + by_scen_value_file + "\n"  
    return output
        
shell_name = "InitializeResultFiles.sh"
output = "rm -r figs/*\n"
output += "rm -r results/*\n"
output += gen_result_make_file("ACC")
output += gen_result_make_file("ACC-min")
f = open(shell_name, "w")
f.writelines(output)
f.close()