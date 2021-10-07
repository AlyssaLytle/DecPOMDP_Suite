from DecPOMDP import *
import copy
import numpy as np

class GWDecPOMDP(decPOMDP):
    def __init__(self, human_agent, machine_agent, environment, horizon, init_state, communication_cost, mvmt_cost, states_set, decay_factor):
        self.human = human_agent
        self.machine = machine_agent
        self.env = environment #will be a GridWorld
        self.horizon = horizon
        self.commander = init_state[1]
        self.comm_cost = communication_cost
        self.mvmt_cost = mvmt_cost
        self.init_state = init_state
        self.states_set = states_set
        self.decay_factor = decay_factor #how likely it is that state changes randomly
        self.current_state = init_state
        self.comm_bool = False


    def belief_state_from_reality(self):
        belief_state = {self.current_state : 1}
        return belief_state

    def step_forward_human(self, action):
        #print("Env rew maps:")
        #print(self.env.get_reward_maps())
        #print("Current rew map:")
        #print(self.env.get_current_reward_map())
        self.env.move(action)
        cost = self.env.get_location_reward()
        curr_gw = self.current_state
        #print("prev state:")
        #print(curr_gw)
        rmap_list = self.env.get_reward_maps()
        gw_names = []
        for elem in self.states_set:
            if elem != curr_gw:
                gw_names.append(elem)
        possible_next_state = np.random.choice(gw_names)
        map_options = [curr_gw, possible_next_state]
        probabilities = [1-self.decay_factor, self.decay_factor]
        next_state = np.random.choice(map_options,p=probabilities)
        self.current_state = next_state
        #print("Rmap List")
        #print(rmap_list)
        #print("Current State")
        #print(self.current_state)
        new_rmap = rmap_list[self.current_state]
        #print("New Rmap:")
        #print(new_rmap)
        self.env.set_current_rew_map(new_rmap)
        #machine always knows which map they are on, even if it changes
        self.machine.new_belief_map(self.belief_state_from_reality())
        return cost


    def step_forward_machine(self, action):

        if action == "comm map 1":
            self.human.new_belief_map(self.belief_state_from_reality())
            self.comm_bool = True
            return self.comm_cost
        if action == "comm map 2":
            self.human.new_belief_map(self.belief_state_from_reality())
            self.comm_bool = True
            return self.comm_cost
        else:
            if self.comm_bool:
                self.human.decay_belief_map(self.decay_factor)
            return 0


    def find_comm_from_prob_maps(self, prob_map, prev_prob_map):
        # print("Old prob map: ")
        # print(prev_prob_map)
        # print("New prob map: ")
        # print(prev_prob_map)
        comm = ["dont_share", 0]
        for key in prob_map:
            if prob_map[key] != prev_prob_map[key]:
                loc = key
                new_dist = prev_prob_map[key]
                for val in new_dist:
                    if new_dist[val] == 1:
                        value = val
                comm = ["share_value", loc, val]
        return comm

    def get_obs_from_state(self, state, prev_state, agent):
        # look for any new communications by observing the prob maps and looking for changes
        loc, commander, human_prob_map, machine_prob_map = state
        old_loc, old_commander, old_human_prob_map, old_machine_prob_map = prev_state
        if agent.name() == "Human":
            comm = self.find_comm_from_prob_maps(human_prob_map, old_human_prob_map)
            print("Comm: ")
            print(comm)
        elif agent.name() == "Machine":
            comm = self.find_comm_from_prob_maps(machine_prob_map, old_machine_prob_map)
            print("Comm: ")
            print(comm)
        else:
            print("*** ERROR: Agent name doesn't match")
        return [loc, comm]

    def find_obs_in_edges(self, obs, edges):
        index = 0
        for observation in edges:
            if obs == observation:
                return index
            else:
                index += 1
        print("OBS NOT FOUND IN EDGES! Edges: " + str(edges) + "Obs: " + str(obs))
        return -1

    def one_step_value(self, state, human_action, machine_action):
        return self.step_forward_machine(machine_action) + self.step_forward_human(human_action)


    def tree_value(self, init_state, human_tree, machine_tree):
        machine_action = machine_tree.get_root().get_action()
        human_action = human_tree.get_root().get_action()

        value = self.one_step_value(init_state,human_action,machine_action)
        if human_tree.get_height() == 0:
            return value
        new_state = self.current_state
        human_obs = machine_action
        machine_obs = new_state

        edg_idx1 = self.find_obs_in_edges(human_obs, human_tree.root.get_edges())
        edg_idx2 = self.find_obs_in_edges(machine_obs, machine_tree.root.get_edges())
        tree1_ch = human_tree.root.get_children()
        tree2_ch = machine_tree.root.get_children()
        new_human_tree = tree1_ch[edg_idx1]
        new_machine_tree = tree2_ch[edg_idx2]
        return value + self.tree_value(new_state, new_human_tree, new_machine_tree)