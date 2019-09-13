class Stack:
    '''

    Python implementation of Stack with list.

    '''

    def __init__(self):
        self.items = []
        self.ptr = 0

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def size(self):
        return self.ptr + 1

    def put(self, value):
        self.items.append(value)
        self.ptr = self.ptr + 1
        return self.items

    def pop(self):
        self.ptr = self.ptr - 1

    def print_stack(self):
        return self.items[:self.ptr]


# if __name__ == "__main__":
#     S = Stack()
#     S.put(1)
#     S.put(2)
#     S.put(3)
#     S.put(4)
#     print(S.isEmpty())
#     print(S.peek())
#     print(S.print_stack())
#     S.pop()
#     print(S.print_stack())