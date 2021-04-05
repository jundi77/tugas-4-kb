# romania problem
# choose ucs, ids, dls, bidirectional: IDS
import copy
from Node import *

class IDS: # iterative deepening search
    # ini sudah disesuaikan dengan kebutuhan 8 queens, yakni tak ada queen menyerang
    def __init__(self, node):
        self.__node = node
        self.__route = None
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

    def get_route(self):
        if self.__found:
            return self.__route
        return None

    def is_found(self):
        return self.__found

    def search(self, target, max_depth):
        self.__found  = False
        self.__target = target

        if self.__route != None: del self.__route
        self.__route = []

        if self.__verbose: print('Target -> ', self.__target.name, "dari", self.__node.name)
        if self.__verbose: print('*' * 10, ' Searching ', '*' * 10)

        for depth in range(0, max_depth + 1):
            if self.__verbose: print('#' * 6, 'search untuk depth', depth, "dari", max_depth, '#' * 6)
            self.__depth = depth
            self.__visited = {}
            node_result = self.dls_search_node(self.__node)
            if self.__found == True:
                self.__node_found = node_result
                self.__route.insert(0, self.__node)
                return node_result
            del self.__visited
        if self.__verbose: print('*' * 10, ' End Searching ', '*' * 10)
        return False

    def dls_search_node(self, node, depth=0):
        if self.__verbose: print("menuju ", node.name)

        if node in self.__visited:
            if self.__verbose: print(node.name, " telah pernah dilewati")
            return False

        # cek jika telah mencapai tujuan
        if node == self.__target:
            if self.__verbose: print("Ditemukan ", node.name)
            self.__found = True
            return node

        if self.__depth == depth:
            if self.__verbose: print("depth mencapai ", self.__depth, " berhenti melakukan searching")
            return False

        depth = depth + 1
        result = False
        for child in node.child:
            if self.__verbose: print("dari ", node.name, " mencoba ke ", child.name)
            self.__visited[node] = True
            result = self.dls_search_node(child, depth)
            if result != False:
                self.__route.insert(0, child)
                break

        return result

if __name__ == "__main__":
    nodes = Node.init_simplified_romania()
    finder = IDS(nodes['Timisoara'])
    # finder.set_verbose(True)
    finder.search(nodes['Bucharest'], 4)
    if finder.is_found():
        out = "Rute ditemukan! "
        prev = None
        dist = 0
        for r in finder.get_route():
            out = out + r.name
            if prev != None:
                out = out + "(" + str(prev.child[r]['w']) + ")"
                dist = dist + prev.child[r]['w']
            prev = r
            out = out + " -> "
        out = out + "sampai"
        print(out, "jarak =", dist)
        exit()
    print("Rute tidak ditemukan")
    
