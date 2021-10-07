

class Node:
    def __init__(self, actions, edges=[], children=[]):
        self.actions = actions
        self.children = children #list of trees with action as root
        self.edges = edges #list of observations

    def add_child(self,edge,child):
        self.children = self.children + [child]
        self.edges = self.edges + [edge]

    def get_edges(self):
        return self.edges

    def get_children(self):
        return self.children

    def has_children(self):
        if len(self.children) > 0:
            return True
        else:
            return False

    def get_action(self):
        return self.actions


    def copy_leaf(self):
        action = self.actions
        return Node(action)