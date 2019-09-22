class Node:

    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next