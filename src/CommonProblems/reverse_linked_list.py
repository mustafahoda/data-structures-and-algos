from DataStructures.DataStructures import LinkedList

def reverse_linked_list(head: LinkedList):

    curr = head
    prev = None
    next = None

    while curr != None:
        next = curr.next # get the next node

        curr.next = prev # make the current next the previous

        # proceed to move forward both the curr and prev
        prev = curr.next
        curr = curr.next

    return prev

# if __name__ == "__main__":
#     LinkedList = LinkedList()
#     LinkedList.append(1)
#     LinkedList.append(2)
#     LinkedList.append(3)
#     LinkedList.append(4)
#     LinkedList.print()