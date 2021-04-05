# romania problem
# choose ucs, ids, dls, bidirectional: IDS
import copy

class Node:
    def __init__(self, name, child={}, parent=None):
        # child adalah dict of node, yang mapping jarak current node ke child, state adalah state node 
        # parent itu node di atas sekarang
        self.name  = name
        self.child  = child

    def add_or_update_child(self, child):
        self.child.update(child)

    def remove_child(self, child):
        del self.child[child]

class IDS: # iterative deepening search
    # ini sudah disesuaikan dengan kebutuhan 8 queens, yakni tak ada queen menyerang
    def __init__(self, node):
        self.__node = node
        self.__node_found = None
        self.__found = False
        self.__depth = 0

    def change_node(self, node):
        self.__node = node
        return self

    def get_depth(self):
        return self.__depth

    def get_node_found(self):
        if self.__found:
            return self.__node_found
        return None

    def is_found(self):
        return self.__found

    def search(self, target, max_depth):
        self.__found  = False
        self.__node_found = None
        self.__target = target

        for depth in (0, max_depth + 1):
            self.__depth = depth
            node_result = self.dls_search_node(self.__node)
            if self.__found:
                self.__node_found = node_result
                return node_result

        return False

    def dls_search_node(self, node, depth=0):
        if self.__depth == depth:
            return False

        # cek jika telah mencapai tujuan
        if node == self.__target:
            self.__found = True
            return node

        depth = depth + 1
        result = False
        for child in node.child:
            result = self.dls_search_node(child, depth)
            if result != False:
                break

        return result

if __name__ == "__main__":
    nodes = {
        'Arad'          : Node('Arad'),
        'Timisoara'     : Node('Timisoara'),
        'Lugoj'         : Node('Lugoj'),
        'Mehadia'       : Node('Mehadia'),
        'Drobeta'       : Node('Drobeta'),
        'Craiova'       : Node('Craiova'),
        'Sibiu'         : Node('Sibiu'),
        'Rimnicu Vilcea': Node('Rimnicu Vilcea'),
        'Pitesti'       : Node('Pitesti'),
        'Fagaras'       : Node('Fagaras'),
        'Bucharest'     : Node('Bucharest'),
    }
