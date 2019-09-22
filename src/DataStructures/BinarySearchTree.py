class BSTNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root == None:
            self.root = BSTNode(value)
        else:
            self._insert(value, self.root)


    def _insert(self,value, current_node):
        # Left
        if value < current_node.value:

            if current_node.left == None:
                current_node.left = BSTNode(value)

            else:
                self._insert(value, current_node.left)
        # Right
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = BSTNode(value)

            else:
                self._insert(value, current_node.right)

        else:
            print("Value is already in tree")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)


    def _print_tree(self, current_node):
        if current_node != None:
            self._print_tree(current_node.left)
            print(str(current_node.value))
            self._print_tree(current_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node == None:
            return current_height
        left_height = self._height(current_node.left, current_height + 1)
        right_height = self._height(current_node.right, current_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):


        if value < current_node.value and current_node.left != None:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right != None:
            return self._search(value, current_node.right)
        elif value == current_node.value:
            return True
        else:
            return False


def fill_tree(tree, num_elements = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elements):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)

    return tree

# tree = BinarySearchTree()
# # tree = fill_tree(tree)
# tree.insert(5)
# tree.insert(1)
# tree.insert(3)
# tree.insert(2)
# tree.insert(7)
# tree.insert(10)
# tree.insert(11)
# tree.insert(0)
# tree.insert(20)
#
#
# tree.print_tree()
#
# print("tree height: %s" % tree.height())
#
# print( tree.search(10))
# print(tree.search(30))