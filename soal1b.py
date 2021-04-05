# romania problem
# choose ucs, ids, dls, bidirectional: IDS
import copy
from Node import *

class IDS: # iterative deepening search
    # ini sudah disesuaikan dengan kebutuhan 8 queens, yakni tak ada queen menyerang
    def __init__(self, node):
        self.__node = node
        self.__node_found = None
        self.__found = False
        self.__depth = 0
        self.__verbose = False

    def change_node(self, node):
        self.__node = node
        return self

    def set_verbose(self, verbose):
        self.__verbose = True

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
        if self.__verbose: print('Target -> ', self.__target.name)
        if self.__verbose: print('*' * 10, ' Searching ', '*' * 10)

        for depth in (0, max_depth):
            self.__depth = depth
            self.__visited = {}
            node_result = self.dls_search_node(self.__node)
            if self.__found == True:
                self.__node_found = node_result
                return node_result
            del self.__visited
        if self.__verbose: print('*' * 10, ' End Searching ', '*' * 10)
        return False

    def dls_search_node(self, node, depth=0):
        if self.__verbose: print("menuju ", node.name)
        self.__visited[node] = True
        if self.__depth == depth:
            if self.__verbose: print("depth mencapai ", self.__depth, " tidak melakukan pengecekan")
            return False

        # cek jika telah mencapai tujuan
        if node == self.__target:
            if self.__verbose: print("Ditemukan ", node.name)
            self.__found = True
            return node

        depth = depth + 1
        result = False
        for child in node.child:
            if self.__verbose: print("dari ", node.name, " mencoba ke ", child.name)
            result = self.dls_search_node(child, depth)
            if result != False:
                break

        return result

if __name__ == "__main__":
    nodes = Node.init_simplified_romania()
    finder = IDS(nodes['Timisoara'])
    finder.set_verbose(True)
    finder.search(nodes['Bucharest'], 5)
    print(finder.is_found())
    # for node in nodes['Arad'].child:
    # print(nodes['Arad'].child)