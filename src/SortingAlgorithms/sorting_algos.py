list_of_sorting_algos = ['quick', 'bubble', 'merge', 'insertion', 'selection']

# ---------BUBBLE SORT-------------
def bubble_sort(A: list) -> list:

    sorted = len(A)

    for i in range(len(A)):

        L = 0
        R = 1

        while R != len(A) :

            # if L > R, then swap
            if A[L] > A[R]:
                temp = A[L]
                A[L] = A[R]
                A[R] = temp

            L = L + 1
            R = R + 1

    return A


# -----------------INSERTION SORT----------------------
def shift_items_to_right(B, start, stop):
    for i in range(stop, start, -1):
        B[i] = B[i - 1]

    return B


def insertion_sort(A : list) -> list:
    sorted = 0

    while sorted != len(A):

        hole = 0

        for i in A[:sorted + 1]:
            value = A[sorted]

            if value < A[hole]:
                # move all items to the right from the hole onwards
                shift_items_to_right(A, hole, sorted)

                # store the value in the hole
                A[hole] = value

            else:
                hole = hole + 1

        sorted = sorted + 1

    return A

# ---------------------MERGE SORT--------------------------------------
def merge(A: list, B: list) -> list:
    ptr_A = 0
    ptr_B = 0

    C = []

    while ptr_A <= len(A) - 1 and ptr_B <= len(B) - 1:

        if A[ptr_A] >= B[ptr_B]:
            C.append(B[ptr_B])
            ptr_B = ptr_B + 1
        else:
            C.append(A[ptr_A])
            ptr_A = ptr_A + 1


    if ptr_A == len(A):
        for i in B[ptr_B:]:
            C.append(i)
    else:
        for i in A[ptr_A:]:
            C.append(i)

    return C

def merge_sort(A: list) -> list:
    if len(A) == 1:
        return A

    # STEP 1: Divide

    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]

    if L is not None:
        L = merge_sort(L)


    if R is not None:
        R = merge_sort(R)


    merged = merge(L, R)

    return merged


# ---------------------QUICK SORT--------------------------------------
def quick_sort(A: list) -> list:
    return _quicksort(A, 0, len(A) - 1)

def _quicksort(A: list, start: int, end: int) -> list:


    if start >= end:
        return A

    pIndex = partition(A, start, end)

    _quicksort(A, start, pIndex - 1)
    _quicksort(A, pIndex, end)

    return A

def partition(A, start: int, end: int):

    pivot = A[end]

    i = start
    pIndex = start

    while i < end:

        if pivot >= A[i]:

            # implement swap between pIndex and A[i]

            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp

            pIndex = pIndex + 1

        i = i + 1

    # once we reach the element before the pivot, we swap pivot into pIndex
    temp = A[pIndex]
    A[pIndex] = pivot
    A[end] = temp

    return pIndex


# ---------------------SELECTION SORT-------------------------------------

def find_min_not_in_place(A: list, visited) -> int:

    for i in A:
        if visited[i] == False:
            min = i
            break

    for i in A[1:]:
        # set_trace()
        if i < min and visited[i] == False:
            # set_trace()

            min = i
            # visited[min] = True

    return min


def selection_sort_not_in_place(A: list) -> list:

    B = []

    # construct a dictionary that will keep track of visited numbers
    visited = dict()
    for i in A:
        visited[i] = False


    # keep repeating the process until theere are no values in dictionary with False
    while False in visited.values():
        for i in A:

            min = find_min_not_in_place(A, visited)
            # set_trace()
            B.append(min)
            visited[min] = True
            print(B)

    return B

def find_min_in_place(A: list, sorted_index: int) -> int:
    min_index = sorted_index
    min = A[sorted_index]

    # for i in A[sorted_index:]:
    for i in range(sorted_index, len(A)):
        if A[i] < min:
            min = A[i]
            min_index = i


    return (min, min_index)



def selection_sort_in_place(A: list) -> list:

    sorted = 0

    while sorted != len(A):

        # min, min_index = find_min_in_place(A[sorted + 1:])
        min, min_index = find_min_in_place(A, sorted)

        # implement swapping
        temp = A[sorted]
        A[sorted] = min
        A[min_index] = temp

        sorted = sorted + 1

    return A