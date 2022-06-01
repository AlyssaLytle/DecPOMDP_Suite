def print_ttable(table):
    for elem in table:
        [start_state, next_state, event, prob_eq, prob_num] = elem
        p_str = start_state + " -> " + next_state + ", "
        p_str += "Prob: " + prob_eq + " = " + str(prob_num)
        print(p_str)
        
def ttable_str(table):
    ret_str = ""
    for elem in table:
        [start_state, next_state, event, prob_eq, prob_num] = elem
        p_str = start_state + " -> " + next_state + ", "
        p_str += "Prob: " + prob_eq + " = " + str(prob_num)
        ret_str += p_str + "\n"
    return ret_str
        
def print_transition_table(t_table):
    errors = []
    hold_exits = []
    push_button = []
    unallowed = []
    h_accel = []
    m_decel = []
    h_none = []
    h_decel = []
    m_none = []
    same_state = []
    no_events = []
    for elem in t_table:
        [start_state, next_state, event, prob_eq, prob_num] = elem
        if event == "error event":
            errors.append(elem)
        elif event == "human: pushbutton":
            push_button.append(elem)
        elif event == "impossible transition":
            unallowed.append(elem)
        elif event == "human: accel":
            h_accel.append(elem) 
        elif event == "machine: decel":
            m_decel.append(elem)
        elif event == "human: decel":
            h_decel.append(elem)
        elif event == "human: none":
            h_none.append(elem)
        elif event == "state never changes":
            same_state.append(elem)
        elif event == "exit hold event":
            hold_exits.append(elem)
        elif event == "no events occur":
            no_events.append(elem)
        else:
            print("Didn't find match!")
            print(event)
    ## Print transitions by reason
    print("Reason: Error")
    print_ttable(errors)
    print("Reason: Automatic Hold Exit")
    print_ttable(hold_exits)
    print("Reason: Human Button Press")
    print_ttable(push_button)
    print("Reason: Human Accel")
    print_ttable(h_accel)
    print("Reason: Human Decel")
    print_ttable(h_decel)
    print("Reason: Machine Decel")
    print_ttable(m_decel)
    print("Reason: Human Does Nothing")
    print_ttable(h_none)
    print("Reason: Machine Does Nothing")
    print_ttable(m_none)
    print("State Stays The Same")
    print_ttable(same_state)
    print("State Stays The Same Given No Events")
    print_ttable(no_events)
    print("Impossible Transitions")
    print_ttable(unallowed)
    
def write_transition_table(t_table, filename):
    errors = []
    hold_exits = []
    push_button = []
    unallowed = []
    h_accel = []
    m_decel = []
    h_none = []
    h_decel = []
    m_none = []
    same_state = []
    no_events = []
    for elem in t_table:
        [start_state, next_state, event, prob_eq, prob_num] = elem
        if event == "error event":
            errors.append(elem)
        elif event == "human: pushbutton":
            push_button.append(elem)
        elif event == "impossible transition":
            unallowed.append(elem)
        elif event == "human: accel":
            h_accel.append(elem) 
        elif event == "machine: decel":
            m_decel.append(elem)
        elif event == "human: decel":
            h_decel.append(elem)
        elif event == "human: none":
            h_none.append(elem)
        elif event == "state never changes":
            same_state.append(elem)
        elif event == "exit hold event":
            hold_exits.append(elem)
        elif event == "no events occur":
            no_events.append(elem)
        else:
            print("Didn't find match!")
            print(event)
    ## Print transitions by reason
    output_str = ""
    output_str += "Reason: Error \n"
    output_str += ttable_str(errors)
    output_str +="Reason: Automatic Hold Exit \n"
    output_str += ttable_str(hold_exits)
    output_str +="Reason: Human Button Press \n"
    output_str += ttable_str(push_button)
    output_str +="Reason: Human Accel \n"
    output_str += ttable_str(h_accel)
    output_str +="Reason: Human Decel \n"
    output_str += ttable_str(h_decel)
    output_str +="Reason: Machine Decel \n"
    output_str += ttable_str(m_decel)
    output_str +="Reason: Human Does Nothing \n"
    output_str += ttable_str(h_none)
    output_str +="Reason: Machine Does Nothing \n"
    output_str += ttable_str(m_none)
    output_str +="State Stays The Same \n"
    output_str += ttable_str(same_state)
    output_str +="State Stays The Same Given No Events \n"
    output_str += ttable_str(no_events)
    output_str +="Impossible Transitions \n"
    output_str += ttable_str(unallowed)
    f = open(filename, "w")
    f.writelines(output_str)
    f.close()