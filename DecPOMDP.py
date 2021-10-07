
import abc

class decPOMDP(object):

    @abc.abstractmethod
    def step_forward_machine(self, action):
        pass

    @abc.abstractmethod
    def step_forward_human(self, action):
        pass

    @abc.abstractmethod
    def find_obs_in_edges(self, obs, edges):
        pass

    @abc.abstractmethod
    def one_step_value(self, state, agent1_action, agent2_action, agent1, agent2):
        pass

    @abc.abstractmethod
    def tree_value(self, init_state, tree1, tree2, agent1, agent2):
        pass


