from pdb import set_trace

class LinkedListNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = LinkedListNode()

    def append(self, data):
        new_node = LinkedListNode(data)
        cur = self.head

        while(cur.next != None):
            cur = cur.next
        cur.next = new_node

    def length(self):
        counter = 0
        cur = self.head

        while(cur.next != None):
            counter = counter + 1
            cur = cur.next

        return counter

    def print(self):
        cur = self.head
        elems = []

        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)

        print(elems)

    def get(self, index):
        if index > self.length():
            print("Can't access this index")

        cur_idx = -1
        cur_node = self.head

        while (cur_idx != index):
            cur_idx = cur_idx + 1
            cur_node = cur_node.next

        return cur_node.data

    def remove(self, index):
        if index > self.length():
            print("Can't access this index")

        cur_idx = -1
        cur_node = self.head

        while(cur_idx != index - 1):
            cur_idx = cur_idx + 1
            cur_node = cur_node.next

        new_next = cur_node.next.next
        cur_node.next = new_next
        return



class Stack:
    '''

    Python implementation of Stack with list.

    '''

    def __init__(self):
        self.items = []
        self.ptr = -1

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def size(self):
        return self.ptr + 1

    def put(self, value):
        try:
            self.items[self.ptr + 1] = value
        except:
            self.items.append(value)
        finally:
            self.ptr = self.ptr + 1
        return self.items

    def pop(self):
        self.ptr = self.ptr - 1

    def print_stack(self):
        print(self.items[:self.ptr + 1])


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

class Queue:
    '''

    Queue implementation using python list; FIFO
    '''

    def __init__(self, value):
        self.items = [value]
        self.front = 0
        self.rear = 0

    def push(self, value):
        self.items.append(value)
        self.rear = self.rear + 1

    def pop(self):
        self.front = self.front + 1
        return self.items[self.front - 1]

    def peek(self):
        print(self.items[self.front])

    def isEmpty(self):
        if self.front - self.rear == 0:
            return True
        else:
            return False

    def count(self):
        return self.rear - self.front + 1

    def print(self):
        print(self.items[self.front: self.rear + 1])

class BinHeap:
    def __init__(self):
        self.heap_list = []
        self.current_size = 0

    def percUp(self, i):
        while i // 2 > 0:
            # if the value we have inserted is less than it's parent, swap it up!
            if self.heap_list[i] > self.heap_list[i // 2]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[i//2]
                self.heap_list[i//2] = temp
            i = i // 2

    def insert(self, val):
        self.heap_list.append(val)
        self.current_size = self.current_size + 1
        self.percUp(self.current_size)

    def delMin(self):
        pass

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

class HashTable:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size

    def add(self, key, value):

        if self.items[self.hash(key)] == None:

            # we create the linked list first
            list = LinkedList()
            list.append([key, value])

            # add the linkedlist to the value of the table
            self.items[self.hash(key)] = list

        else:
            self.items[self.hash(key)].append([key, value])

    def remove(self):
        pass

    def hash(self, key):
        return len(key) - 1

    def search(self, key):
        hash_value = self.hash(key)

        if self.items[hash_value] == None:
            print("ERROR: Couldn't find that key")

        else:
            linked_list = self.items[hash_value]
            current_node = linked_list.head
            set_trace()

            while (current_node.next != None):
                current_node = current_node.next
                if current_node.data[0] == key:
                    return print(current_node.data[1])

    def print(self):
        print(self.items)

class Vertex:
    def __init__(self, data):
        self.data = data

class Graph:

    '''
    Adjacency List Graph Implementation

    '''
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex, edges):
        self.graph[vertex] = edges

    def find_path(self, graph, start, end, path = []):
        path = path + [start]
        if start == end:
            return None

    def BFS(self, entry_point):

        # visited_dict = [False] * len(self.graph)
        visited_dict = {}

        for vertex in self.graph.keys():
            visited_dict[vertex] = False

        print(visited_dict)

        if entry_point not in self.graph.keys():
            print("ERROR: Entry point is not a vertex in the graph.")
            return

        q = list()
        q.append(entry_point)

        import time

        while len(q) != False:
            print("q: %s" % q)
            s = q.pop(0)
            print("s: %s" % s)
            visited_dict[s] = True
            time.sleep(0.5)

            adjacent = self.graph[s]
            for i in adjacent:
                if visited_dict[i] == False:
                    q.append(i)


    def print(self):
        print(self.graph)