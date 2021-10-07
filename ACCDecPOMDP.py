from DecPOMDP import *

class ACCDecPOMDP(decPOMDP):
    def __init__(self, horizon, init_state, init_actions_dict, cost_dict, states_set):
        self.horizon = horizon
        self.init_state = init_state
        self.cost_dict = cost_dict
        self.states_set = states_set
        self.init_actions = init_actions_dict

