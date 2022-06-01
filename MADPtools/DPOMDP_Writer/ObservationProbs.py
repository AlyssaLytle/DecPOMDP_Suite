from tracemalloc import start


info_file = "ACC.dpomdp"

def calculate_obs_probabilities(start_state):
    f = open(info_file, "r")
    for x in f:
        if x[0] == "O":
            x_arr = (x.split(":"))
            actions = x_arr[1]
            start_state_check = x_arr[2]
            obs = x_arr[3]
            prob = int(x_arr[4])
            start_state_check = start_state_check[1:-1]
            if start_state_check == start_state:
                act_arr = actions.split(" ")
                obs_arr = obs.split(" ")
                human_act = act_arr[1]
                human_obs = obs_arr[1]
                machine_act = act_arr[2]
                machine_obs = obs_arr[2]
                print("Cause for transition " + human_act + " " + machine_act)
                print("Observations: " + human_obs + " " + machine_obs)
calculate_obs_probabilities("standby")