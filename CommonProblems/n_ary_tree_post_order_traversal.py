class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         list = self._postorder(root, [])
#         return list
#
#     def _postorder(self, root: 'Node', list):
#
#         print(list)
#
#         if root.children:
#             for child in root.children:
#                 self._postorder(child, list)
#
#         if root.children == []:
#             list.append(root.val)
#             return list
#
#         list.append(root.val)

from pdb import set_trace

if __name__ == "__main__":
    node = Node()
    set_trace()

    {"$id": "1", "children": [
        {"$id": "2", "children": [{"$id": "5", "children": [], "val": 5}, {"$id": "6", "children": [], "val": 6}],
         "val": 3}, {"$id": "3", "children": [], "val": 2}, {"$id": "4", "children": [], "val": 4}], "val": 1}