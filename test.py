from DataStructures import DataStructures
from CommonProblems import reverse_linked_list
from pdb import set_trace

if __name__ == "__main__":
    # LL = DataStructures.LinkedList(3)
    # LL.insert(3)
    # LL.insert(4)

    # stack = DataStructures.Stack()
    # stack.put(1)
    # stack.put(2)
    # stack.put(5)
    # stack.put(9)
    # stack.put(11)
    # stack.print_stack()
    # stack.pop()
    # stack.print_stack()
    # stack.put(50)
    # stack.print_stack()

    # sLinkedList = DataStructures.StackLinkedList()
    # sLinkedList.put(2)
    # from pdb import set_trace
    # set_trace()

    # my_list = DataStructures.LinkedList()
    # my_list.append(['corn', 2.38])
    # my_list.append(['apple', 1.38])
    # my_list.append(['orange', 5.23])
    # my_list.append(['bread', 10])
    # my_list.append(4)
    # my_list.print()
    # my_list.remove(1)
    # my_list.print()

    # print(my_list.get(0))

    # ll.print()

    # Q = DataStructures.Queue(10)
    # Q.print()
    # Q.push(1)
    # Q.push(3)
    # Q.push(4)
    # # Q.print()
    # # from pdb import set_trace
    # # set_trace()
    # Q.pop()
    # # Q.print()
    # print(Q.isEmpty())
    # Q.print()
    # print(Q.count())

    # table = DataStructures.HashTable(6)
    # table.add('apple', 2.31)
    # table.add('flour', 1.23)
    # table.search('flour')
    # # table.print()
    # # set_trace()

    # g = DataStructures.Graph()
    # g.print()
    # g.add_vertex('A', ['B', 'C'])
    # g.add_vertex('B', ['C', 'D'])
    # g.add_vertex('C', ['D'])
    # g.add_vertex('D', ['C'])
    # g.add_vertex('E', ['F'])
    # g.add_vertex('F', ['C'])
    # g.add_vertex(0, [2, 1])
    # g.add_vertex(1, [2])
    # g.add_vertex(2, [0, 3])
    # g.add_vertex(3, [3])
    # g.print()
    # g.DFS(2)


    # g = DataStructures.Graph()
    # g.print()
    # # g.add_vertex('A', ['B', 'C'])
    # # g.add_vertex('B', ['E', 'D', 'A'])
    # # g.add_vertex('C', ['A', 'E'])
    # # g.add_vertex('D', ['B', 'F', 'E'])
    # # g.add_vertex('E', ['B', 'D', 'F', 'C'])
    # # g.add_vertex('F', ['D', 'E'])
    # g.add_vertex(0, [2, 1, 3])
    # g.add_vertex(1, [3])
    # g.add_vertex(2, [0, 1])
    # g.add_vertex(3, [])
    # # g.add_vertex(3, [3])
    # # g.print()
    # # print(g.DFS(2))
    # print(g.find_path_between_two_nodes(2,3))

    # tree = DataStructures.BinarySearchTree()
    # tree.insert(1)
    # tree.insert(2)
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(5)
    # # tree.insert(7)
    # # tree.insert(12)
    # # tree.insert(15)
    # # tree.insert(15)
    # # tree.print_tree()
    # # tree.print_DFS(tree.root, 'in')
    # tree.print_BFS(tree.root)

    LinkedList = DataStructures.LinkedList()
    LinkedList.append(1)
    LinkedList.append(2)
    LinkedList.append(3)
    LinkedList.append(4)
    # set_trace()
    LinkedList.print()
    print(LinkedList.reverse_linked_list(LinkedList.head.next))
    LinkedList.print()
    set_trace()

    # LinkedList = DataStructures.LinkedListNode()
    # LinkedList.data



