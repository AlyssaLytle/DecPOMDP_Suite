def read_dpomdp_file(filename):
    f = open(filename, "r")
    for x in f:
        x = x.split(" ")
        if x[0] == "T:":
            h_action = x[1]
            m_action = x[2]
            start_state = x[4]
            next_state = x[6]
            prob = x[8]
            prob = prob[:-1]
            if m_action != "*":
                m_action_arr = m_action.split("-")
                print(m_action_arr[1])
            print([h_action,m_action,start_state, next_state,prob])
            #print(x)
        
read_dpomdp_file("ACC/ACC-ss-standby-scen-1.dpomdp")