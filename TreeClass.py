from builtins import enumerate, str
from tree_helpers import *
from NodeClass import *

#Methods that input a tree and output something
def get_leaves(tree):
    list = []
    if tree.get_root().has_children():
        children = tree.get_root().get_children()
        for child in children:
            list.append(get_leaves(child))
        return list
    else:
        return [tree.get_root()]

def replace_leaves(tree, leaves):
    #Inputs old tree. Returns new tree with leaves added on.
    #Needs to copy old tree and replace old leaves with the input "leaves"
    #TODO
    return 0


class Tree:
    def __init__(self, root):
        self.root = root #object of type Node


    def get_root(self):
        return self.root

    def Depth_First_Search(self):
        return 0

    def get_height(self):
        temp_root = self.root
        if temp_root.has_children():
            children = temp_root.get_children()
            temp_child = children[0]
            return 1 + temp_child.get_height()
        else:
            return 0

    def fully_explored(self, horizon):
        if self.get_height() >= horizon:
            return True
        else:
            return False

    def add_children(self, edge, child):
        self.root.add_child(edge, child)


    def add_children_list(self, edgelist, childlist):
        for x in range(len(edgelist)):
            self.root.add_child(edgelist[x], childlist[x])


    def tree_to_str(self):
        #ret_str = str(self.get_height()) + "\n"
        temp_root = self.root
        ret_str = str(0) + ":" + str(temp_root.get_action()) + "\n"
        #print(ret_str)
        children = temp_root.get_children()
        edges = temp_root.get_edges()
        for idx in range(len(children)):
            edge = edges[idx]
            child = children[idx]
            #print("Child")
            #print(child)
            ret_str += child.tree_to_str_rec(1, edge)

        return ret_str

    def tree_to_str_rec(self,level, edge):
        #print(level)
        temp_root = self.root
        tree_str = str(level) + ":" + str(edge) + ":" + str(temp_root.get_action()) + "\n"
        #print(tree_str)
        children = temp_root.get_children()
        if len(children)>0:
            edges = temp_root.get_edges()
            for idx in range(len(children)):
                new_edge = edges[idx]
                child = children[idx]
                #print(child)
                tree_str += child.tree_to_str_rec(level+1, new_edge)
        return tree_str

    def tree_to_str_semicolon(self):
        #ret_str = str(self.get_height()) + "\n"
        temp_root = self.root
        ret_str = str(0) + ":" + str(temp_root.get_action()) + ";"
        #print(ret_str)
        children = temp_root.get_children()
        edges = temp_root.get_edges()
        for idx in range(len(children)):
            edge = edges[idx]
            child = children[idx]
            ret_str += child.tree_to_str_rec_comma(1, edge)
        return ret_str


    def tree_to_str_rec_comma(self,level, edge):
        #print(level)
        temp_root = self.root
        tree_str = str(level) + ":" + str(edge) + ":" + str(temp_root.get_action()) + ";"
        #print(tree_str)
        children = temp_root.get_children()
        if len(children)>0:
            edges = temp_root.get_edges()
            for idx in range(len(children)):
                new_edge = edges[idx]
                child = children[idx]
                tree_str += child.tree_to_str_rec_comma(level+1, new_edge)
        return tree_str

    def output_tree_to_file(self, filename):
        with open(filename, mode='w') as writefile:
            writefile.write(self.tree_to_str())

    def get_leaves_tree_list(self,tlist):
        list = []
        for tree in tlist:
            if tree.get_root().has_children():
                list.append(self.get_leaves_tree_list(tree.get_root().get_children()))
            else:
                list.append(tree.get_root())
        return list

    def get_leaves(self):
        list = []
        if self.get_root().has_children():
            children = self.get_root().get_children()
            for child in children:
                list.append(child.get_leaves())
            return list
        else:
            return [self.get_root()]



    def copy_tree(self):
        root = self.get_root()
        root_action = root.get_action()
        if root.has_children():
            children = root.get_children()
            edges = root.get_edges()
            new_edges = []
            new_children = []
            for x in range(len(children)):
                child = children[x]
                new_edge = edges[x]
                new_child = child.copy_tree()
                new_edges.append(new_edge)
                new_children.append(new_child)
            new_root = Node(root_action,new_edges,new_children)
        else:
            new_root = Node(root_action)
        ret_tree = Tree(new_root)
        return ret_tree


    def leaf_index(self, n):
        #finds the nth leaf
        tree_str = self.tree_to_str_comma()
        height = self.get_height()
        #print("Height:" + str(height))
        #print(tree_str)
        idx = 0
        tree_arr = tree_str.split(',')
        for row in tree_arr:
            temp_arr = row.split(':')
            level = temp_arr[0]
            if len(level) == 1:
                lvl = int(level)
            if lvl == height:
                if idx == n:
                    return row
                else:
                    idx +=1



    def add_child_at_leaf_index(self, n, edgename, childname):
        height = self.get_height()
        new_level = height+1
        str_to_add = str(new_level)+ ":" + str(edgename) + ":"  + str(childname)
        #print(str_to_add)
        tree_str = self.tree_to_str_semicolon()
        height = self.get_height()
        #print("Height:" + str(height))
        #print(tree_str)
        idx = 0
        tree_arr = tree_str.split(';')
        for x in range(len(tree_arr)):
            row = tree_arr[x]
            temp_arr = row.split(':')
            level = temp_arr[0]
            if len(level) == 1:
                lvl = int(level)
            if lvl == height:
                if idx == n:
                    new_tree_1 = tree_arr[:x+1]
                    new_tree_2 = tree_arr[x+1:]
                    new_tree = new_tree_1 + [str_to_add] + new_tree_2
                idx += 1

        return new_tree


    def add_array_to_leaves(self, input_array):
        D = [self]
        idx = 0
        len_array = len(input_array)
        while len(D) > 0 & idx <= len_array:
            temp = D[0]
            D.remove(temp)
            if temp.get_root().has_children():
                for x in temp.get_root().get_children():
                    D.append(x)
            else:
                #print(idx)
                #print(input_array[idx])
                edge_list, child_list = input_array[idx]
                temp.add_children_list(edge_list, child_list)
                idx += 1


    def replace_leaves(self, input_array):
        D = [self]
        idx = 0

        while len(D) > 0:
            temp = D[0]
            #print("Temp")
            #print(temp)
            D.remove(temp)
            if temp.get_root().has_children():
                for x in temp.get_root().get_children():
                    D.append(x)
            else:
                new_tree = input_array[idx]
                edge_list = new_tree.get_root().get_edges()
                child_list = new_tree.get_root().get_children()
                #print("NEW LISTS:")
                #print(edge_list)
                #print(child_list)
                for x in range(len(edge_list)):
                    temp.root.add_child(edge_list[x], child_list[x])
                idx += 1




    def tree_to_short_str(self):
        #ret_str = str(self.get_height()) + "\n"
        temp_root = self.root
        action_number, action = temp_root.get_action()
        str_number = str(action_number)
        str_action = encode_action(action)
        ret_str = str(0) + ":" + str_number + "-" + str_action + "\n"
        #print(ret_str)
        children = temp_root.get_children()
        edges = temp_root.get_edges()
        for idx in range(len(children)):
            edge = edges[idx]
            child = children[idx]
            #print("Child")
            #print(child)
            ret_str += child.tree_to_short_str_rec(1, edge)

        return ret_str

    def tree_to_short_str_rec(self,level, edge):
        #print(level)
        temp_root = self.root
        action_number, action = temp_root.get_action()
        str_number = str(action_number)
        str_action = encode_action(action)
        edge_number, edge_val = edge
        str_edge_number = str(edge_number)
        str_edge = encode_obs(edge_val)
        obs_str = str_edge_number + "-" + str_edge
        act_str = str_number + "-" + str_action
        tree_str = str(level) + ":" + obs_str + ":" + act_str + "\n"
        #print(tree_str)
        children = temp_root.get_children()
        if len(children)>0:
            edges = temp_root.get_edges()
            for idx in range(len(children)):
                new_edge = edges[idx]
                child = children[idx]
                #print(child)
                tree_str += child.tree_to_str_rec(level+1, new_edge)
        return tree_str

    def sub_tree_rec(self,n,subtree):
        root = subtree.get_root()
        edge_list = root.get_edges()
        child_list = root.get_children()
        tree_list = []
        if n > 1:
            for x in range(len(edge_list)):
                child = child_list[x]
                child_root = child.get_root()
                action = child_root.get_action()
                new_tree = Tree(Node([action]))
                [edges,children] = self.sub_tree_rec(n-1,child)
                new_tree.add_children_list(edges,children)
                tree_list.append(new_tree)
            return [edge_list,tree_list]
        else:
            for x in range(len(edge_list)):
                child = child_list[x]
                child_root = child.get_root()
                action = child_root.get_action()
                new_tree = Tree(Node([action]))
                tree_list.append(new_tree)
            return [edge_list,tree_list]


    def sub_tree(self, n):
        #returns tree up to level n
        root = self.get_root()
        action = root.get_action()
        new_node = Node([action])
        head_tree = Tree(new_node)
        [edges,children] = self.sub_tree_rec(n-1,self)
        head_tree.add_children_list(edges,children)
        return head_tree


