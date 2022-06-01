import itertools
import sys
sys.path.append("..")
from ArrayTree import ArrayTree

class ACC_DPOMDP:

    def __init__(self,start_state, mode_change_table, mach_comm_acts, mach_move_acts,hum_comm_acts,hum_move_acts,modes,prob_dict,cost_dict, scenario_number, human_observations, machine_observations, horizon, init_actions):
        self.mode_change_table = mode_change_table
        self.states = modes
        self.human_actions = list(itertools.product(hum_move_acts, hum_comm_acts))
        self.machine_comm_actions = mach_comm_acts
        self.machine_actions = list(itertools.product(mach_move_acts, mach_comm_acts))
        #self.decpomdp = DecPOMDP_medium(mach_comm_acts, mach_move_acts,hum_comm_acts,hum_move_acts,prob_dict,modes,scenario_number, cost_dict)
        self.costs = cost_dict
        self.scenario = scenario_number
        self.prob_dict = prob_dict
        self.start_state = start_state
        self.human_observations = human_observations
        self.machine_observations = machine_observations
        self.horizon = horizon
        self.init_actions = init_actions

    def get_possible_transitions(self, start_state, hum_action, mach_action):
        #gives set of possible end states and the cause for those transitions
        transitions = []
        [hum_phys, hum_comm] = hum_action
        [mach_phys, mach_comm] = mach_action
        for row in self.mode_change_table:
            [starts, ends, cause] = row
            if start_state in starts:
                if cause[0] == "event":
                    #this means an event occurred
                    trans = [[cause, ends[0]]]
                    transitions += trans
                else:
                    if cause[0] == "human":
                        #this means it was a human action
                        if (cause[1] == hum_phys) | (cause[2] == hum_comm):
                            for end_state in ends:
                                trans = [[cause, end_state]]
                                transitions += trans
                    elif cause[0] == "machine":
                        #this means it was a machine action
                        if (cause[1] == mach_phys) | (cause[2] == mach_comm):
                            for end_state in ends:
                                trans = [[cause, end_state]]
                                transitions += trans
        #print("TRANSITIONS:" + str(transitions))
        return transitions

    def combine_duplicate_transitions(self, trans_table):
        #combines probabilities for transitions that end up in the same next-state
        
        prelen = len(trans_table)
        return_table = []
        
        while len(trans_table)>1:
            flag = True 
            j = 1
            while j < len(trans_table):
                if trans_table[0][0] == trans_table[j][0]:
                    #print("Duplicate Found")
                    flag = False
                    return_table += [[trans_table[0][0], trans_table[0][1]+trans_table[j][1]]]
                    trans_table.remove(trans_table[j])
                else:
                    j += 1
            if flag:
                return_table += [trans_table[0]]
            trans_table.remove(trans_table[0])
            if trans_table is None:
                trans_table = []
        return_table += trans_table
        return return_table
            

    def get_transition_table(self, state, human_action, machine_action):
        #Gets table of possible next states and their probability
        #[[state1,p1], [state2,p2],...]
        transition_table = []
        p_error = float(self.prob_dict["error"])
        p_hold_exit = float(self.prob_dict["exithold"])

        possible_transitions = self.get_possible_transitions(state, human_action, machine_action)
        if len(possible_transitions)>0:
            num_transitions = len(possible_transitions)
            remaining_prob = float(1/num_transitions)
            if (state == "following")|(state == "speedcontrol")|(state=="hold"):
                prob_error = float(p_error/num_transitions)
                num_transitions = num_transitions - 1
                if num_transitions > 0:
                    remaining_prob = float((1 - prob_error)/num_transitions)
                else:
                    remaining_prob = float((1 - prob_error))
            if state == "hold":
                prob_hold = p_hold_exit/num_transitions
                num_transitions = num_transitions - 1
                if num_transitions > 0:
                    remaining_prob = float((1 - prob_hold - prob_error)/num_transitions)
                else: 
                    remaining_prob = float((1 - prob_hold - prob_error))
            if num_transitions == 0:
                #state stays the same unless there's an event
                trans_line = [[state, remaining_prob]]
                transition_table += trans_line
            for transition in possible_transitions:
                [cause, end_state] = transition
                if cause[1] == "error":
                    trans_line = [[end_state, prob_error] ]
                elif cause[1] == "exit": 
                    trans_line = [[end_state, prob_hold]]
                else:
                    trans_line = [[end_state, remaining_prob]]
                transition_table += trans_line
        else:
            #state stays the same
            trans_line = [[state,float(1)]]
            transition_table += trans_line
        return self.combine_duplicate_transitions(transition_table)

    def get_allowed_machine_actions(self, mode):
        sc = (mode == "speedcontrol")
        follow = (mode == "following")
        if sc | follow :
            allowed_mvmts = ["accel", "decel", "maintainspeed"]
        else:
            allowed_mvmts = ["none"]
        return list(itertools.product(allowed_mvmts,self.machine_comm_actions))

    def get_safety(self,human_action, machine_action):
        #input PHYSICAL MOVEMENT actions as human_action and machine_action
        scenario = self.scenario
        anti_decel = ["accel", "maintainspeed"]
        anti_accel = ["decel"]
        if (scenario == 1) | (scenario == 2) | (scenario == 5):
            if (human_action == "decel"):
                return True
            elif (machine_action == "decel"): #& ~(human_action in anti_decel):
                return True
            else:
                return False
        elif (scenario == 3) | (scenario == 7):
            if (human_action == "decel"):
                return False
            elif (machine_action == "decel"): #& ~(human_action in anti_decel):
                return False
            else:
                return True
        elif (scenario == 4) | (scenario == 8):
            if human_action == "accel":
                return True
            elif (machine_action == "accel"): #& ~(human_action in anti_accel):
                return True
            else:
                return False
        elif (scenario == 6):
            return False
        else:
            print("ERROR! Unrecognized scenario!")

    def get_cost(self, human_action, machine_action):
        #print("human action")
        #print(human_action)
        [hum_mvmt, hum_comm] = human_action
        [mach_mvmt, mach_comm] = machine_action
        safety = self.get_safety(hum_mvmt, mach_mvmt)
        cost = 0
        # cost for human to move
        #if hum_mvmt != "none":
        #    cost += self.costs["human movement"]
        # cost for unsafe state
        if safety == False:
            cost += self.costs["unsafe"]
        # cost of machine updating the interface
        if mach_comm == "communicate":
            cost += self.costs["machine communication"]
        #reward for automation
        if mach_mvmt != "none":
            cost += self.costs["automation reward"]
        return cost

    def get_human_observation(self,next_state,human_action, machine_action):
        [hum_mvmt, hum_comm] = human_action
        [mach_mvmt, mach_comm] = machine_action
        if (mach_comm == "communicate") | (hum_comm == "pushbutton"):
            return next_state
        else:
            return "none"
        

    

    
    def get_one_step_value(self, state, human_action, machine_action):
        return 
    
    def get_value(self,h_tree,m_tree,state,h_idx, m_idx):
        #a state probability mapping should look like [[state1, prob1], [state2,prob2], etc...]
        #h_tree.print()
        #m_tree.print()
        val = self.get_cost(h_tree.nodes[h_idx], m_tree.nodes[m_idx])
        
        if h_tree.has_child(h_idx):
            next_state_distribution = self.get_transition_table(state, h_tree.nodes[h_idx], m_tree.nodes[m_idx])
            for elem in next_state_distribution:
                [next_state, prob] = elem
                #print("Next state + probability: ")
                #print(elem)
                h_obs = self.get_human_observation(next_state,h_tree.nodes[h_idx], m_tree.nodes[m_idx])
                m_obs = next_state
                #print("Tree size: " + str(len(h_tree.nodes)))
                #print("Child edge index: " + str(h_tree.get_child_edge_idx_with_value(h_idx, h_obs)))
                val += prob * self.get_value(h_tree, m_tree, next_state, h_tree.get_child_edge_idx_with_value(h_idx, h_obs), m_tree.get_child_edge_idx_with_value(m_idx, m_obs))
        return val
    
    def prune_check(self, tree):
        # for any node on bottom level, 
        # if human phys action is dangerous 
        # AND human comm action is NONE 
        # THEN CHECK human observation (aka edge )== none
        # if so, prune tree 
        return False
    
    def prune_check_machine(self, tree):
        #for any node on bottom level,
        # if phys action is dangerous,
        # THEN check if obs is possible,
        # if so, prune tree
        return False
        
    def prune_check_human(self, tree):
        #for any node on bottom level,
        # if phys action is dangerous,
        # THEN check if obs is not "none" & is possible,
        # if so, prune tree
        return False