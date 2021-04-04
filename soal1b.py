# 8 queens, 8x8 chess board
# choose ucs, ids, dls, bidirectional: IDS
import copy

class Node:
    def __init__(self, state, child=[], parent=None):
        # child adalah dict of node, state adalah state node (current 8 queens placement)
        # parent itu node di atas sekarang
        self.state  = state
        self.child  = child
        self.parent = parent

        # status expanded
        self.__expanded = False

    def expands(self):
        self.__expanded = True
        return True
    
    def is_expanded(self):
        return self.__expanded

    def print_all_parents(self, node=None):
        if node == None:
            print("self node")
        else:
            print("self")

        if self.parent != None:
            self.print_all_parents(self.parent)

class EightQueensNode(Node):
    def __init__(self, state, child=[], parent=None):
        Node.__init__(self, state, child, parent)
        self.__safe = None

    def expands(self):
        # satu queen bisa bergerak ke 8 arah, ulangi untuk queen yang lain
        # satu child satu gerakan
        for queen in range(0,8): 
            for x in range(-1,2):
                for y in range(-1,2):
                    if (self.state[queen][0] + x >= 0 and
                        self.state[queen][0] + x < 8 and
                        self.state[queen][1] + y >= 0 and
                        self.state[queen][1] + y < 8):
                        new_state = copy.deepcopy(self.state)
                        new_state[queen][0] = new_state[queen][0] + x
                        new_state[queen][1] = new_state[queen][1] + y
                        self.child.append(EightQueensNode(new_state, [], self))

        self.__expanded = True
    
    def is_safe(self):
        if self.__safe != None:
            return self.__safe
        self.check_queens_attacks()
        return self.is_safe()

    def check_queens_attacks(self):
        for queen1 in range(0,7):
            if self.__safe != None: break
            for queen2 in range(queen1+1,8):
                # cek baris
                if self.state[queen1][0] == self.state[queen2][0]:
                    self.__safe = False
                # cek kolom
                if self.state[queen1][1] == self.state[queen2][1]:
                    self.__safe = False
                # cek diagonal
                if ( self.state[queen1][0] - self.state[queen2][0] > 0 and
                   abs(
                       (self.state[queen1][1] - self.state[queen2][1]) /
                       (self.state[queen1][0] - self.state[queen2][0])
                    ) == 1):
                    print("no ", queen1, " ", queen2, " abs=", abs(
                       (self.state[queen1][1] - self.state[queen2][1]) /
                       (self.state[queen1][0] - self.state[queen2][0])
                    ))
                    self.__safe = False

                if self.__safe == None: print("no ", queen1, " ", queen2)
                if self.__safe != None: break
        if self.__safe == None:
            self.__safe = True

class TreeIterator:
    def __init__(self, tree, currentNode, child_position=None):
        self.currentNode      = currentNode
        self.__tree           = tree
        self.__child_position = child_position

    def move_to(self, node):
        self.currentNode = node
        return self
    
    def get_child_position(self):
        return self.__child_position

    def get_tree(self):
        return self.__tree

    def set_child_position(self, position):
        if position >= 0 and position < len(self.currentNode.child):
            self.currentNode      = self.currentNode.child[position]
            self.__child_position = position
            return True

        return False

    def go_up(self):
        if self.currentNode.parent != None:
            self.currentNode = self.currentNode.parent
            return True

        return False
    
    def go_down(self, child_position=0):
        if len(self.currentNode.child) > 0 and child_position < len(self.currentNode.child):
            self.currentNode = self.currentNode.child[child_position]
            return True

        return False


class Tree:
    def __init__(self, root):
        # root adalah Node
        self.root     = root

class IDS: # iterative deepening search
    # ini sudah disesuaikan dengan kebutuhan 8 queens, yakni tak ada queen menyerang
    def __init__(self, tree):
        self.__tree = tree
        self.__node_found = None
        self.__found = False
        self.__depth = 0

    def change_tree(self, tree):
        self.__tree = tree
        return self

    def get_depth(self):
        return self.__depth

    def get_node_found(self):
        if self.__found:
            return self.__node_found
        return None

    def is_found(self):
        return self.__found

    def search(self, max_depth):
        self.__found  = False
        self.__node_found = None

        for depth in (0, max_depth + 1):
            self.__depth = depth
            node_result = self.dls_search_node(self.__tree.root)
            if self.__found:
                self.__node_found = node_result
                return node_result

        return False

    def dls_search_node(self, node, depth=0):
        if self.__depth == depth:
            return False

        # cek jika tidak ada queen yang menyerang satu sama lain
        if node.is_safe():
            self.__found = True
            return node

        if(node.is_expanded): node.expands()
        depth = depth + 1

        result = False
        for child in node.child:
            result = self.dls_search_node(child, depth)
            if result != False:
                break

        return result

if __name__ == "__main__":
    # tree = Tree( EightQueensNode([
    #     # x, y
    #     [0,1],
    #     [0,2],
    #     [0,3],
    #     [0,4],
    #     [0,5],
    #     [0,6],
    #     [0,7],
    #     [0,8],
    # ]))
    test = EightQueensNode([
        # x, y
        [0,0],
        [4,1],
        [1,2],
        [5,3],
        [2,4],
        [6,5],
        [3,6],
        [7,7],
    ])
    test.expands()
    print(len(test.child))
    print(test.is_safe())
    print(1)
    # finder = IDS(tree)
    # max_depth = 25
    # finder.search(max_depth)

    # if finder.is_found():
    #     print("Ada konfigurasi queen yang tidak menyerang untuk depth {max_depth}") # TODO
    #     finder.get_node_found().print_all_parents()
    #     exit()

    # print("Tidak ada konfigurasi queen yang tidak menyerang untuk depth {max_depth}") # TODO

