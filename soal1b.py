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

    @staticmethod
    def init_simplified_romania():
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

        nodes['Arad'].add_or_update_child({
            nodes['Sibiu']: {
                'w': 140
            },
            nodes['Timisoara']: {
                'w': 111
            },
        })
        nodes['Lugoj'].add_or_update_child({
            nodes['Timisoara']: {
                'w': 111
            },
            nodes['Mehadia']: {
                'w': 70
            },
        })
        nodes['Mehadia'].add_or_update_child({
            nodes['Lugoj']: {
                'w': 70
            },
            nodes['Drobeta']: {
                'w': 75
            },
        })
        nodes['Drobeta'].add_or_update_child({
            nodes['Mehadia']: {
                'w': 75
            },
            nodes['Craiova']: {
                'w': 120
            },
        })
        nodes['Craiova'].add_or_update_child({
            nodes['Drobeta']: {
                'w': 120
            },
            nodes['Rimnicu Vilcea']: {
                'w': 146
            },
            nodes['Pitesti']: {
                'w': 138
            },
        })
        nodes['Rimnicu Vilcea'].add_or_update_child({
            nodes['Craiova']: {
                'w': 146
            },
            nodes['Sibiu']: {
                'w': 80
            },
            nodes['Pitesti']: {
                'w': 97
            },
        })
        nodes['Pitesti'].add_or_update_child({
            nodes['Craiova']: {
                'w': 138
            },
            nodes['Rimnicu Vilcea']: {
                'w': 97
            },
            nodes['Bucharest']: {
                'w': 101
            },
        })
        nodes['Sibiu'].add_or_update_child({
            nodes['Arad']: {
                'w': 140
            },
            nodes['Rimnicu Vilcea']: {
                'w': 80
            },
            nodes['Fagaras']: {
                'w': 99
            },
        })
        nodes['Fagaras'].add_or_update_child({
            nodes['Sibiu']: {
                'w': 99
            },
            nodes['Bucharest']: {
                'w': 211
            },
        })
        nodes['Bucharest'].add_or_update_child({
            nodes['Pitesti']: {
                'w': 101
            },
            nodes['Fagaras']: {
                'w': 211
            },
        })

        return nodes

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
    test = Node.init_simplified_romania()